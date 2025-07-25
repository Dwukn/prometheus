// Controls Sound when trackpoint is used

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <libinput.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include <linux/input.h>
#include <time.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>

#define SOUND_FILE ".config/hypr/feat/audio/Kitten.mp3"
#define COOLDOWN_SECONDS 5
#define PID_FILE "/var/run/tpsd/tpsd.pid"

volatile sig_atomic_t running = 1;

int volume_level = 10;  // Default volume level (10%)

// Signal handler
void handle_signal(int signum) {
    running = 0;
}

// Interface functions required by libinput
static int open_restricted(const char *path, int flags, void *user_data) {
    int fd = open(path, flags);
    return fd < 0 ? -errno : fd;
}

static void close_restricted(int fd, void *user_data) {
    close(fd);
}

static const struct libinput_interface interface = {
    .open_restricted = open_restricted,
    .close_restricted = close_restricted,
};

// Function to convert percentage to mpg123 volume value
int convert_percentage_to_mpg123(int percentage) {
    if (percentage < 1) percentage = 1;  // Minimum allowed volume is 1%
    if (percentage > 100) percentage = 100;  // Maximum allowed volume is 100%
    return (int)((float)percentage / 100 * 32770);  // Convert to mpg123 volume
}

// void play_sound() {
//     int mpg123_volume = convert_percentage_to_mpg123(volume_level);
//     char command[256];
//
//     // Debugging line: Print the command that is being executed
//     printf("Executing command: mpg123 -q -f %d \"%s\"\n", mpg123_volume, SOUND_FILE);
//
//     snprintf(command, sizeof(command), "mpg123 -q -f %d \"%s\" &", mpg123_volume, SOUND_FILE);
//
//     // Debugging line: Check if system call is successful
//     int result = system(command);
//     if (result != 0) {
//         fprintf(stderr, "Error executing mpg123 command: %d\n", result);
//     }
// }

void play_sound() {
    int mpg123_volume = convert_percentage_to_mpg123(volume_level);
    char command[256];

    snprintf(command, sizeof(command), "mpg123 -q -f %d \"%s\" 2>&1", mpg123_volume, SOUND_FILE);

    // Debugging line: Show the exact command being run
    printf("Executing command: %s\n", command);

    FILE *fp = popen(command, "r");
    if (!fp) {
        fprintf(stderr, "Error executing mpg123 command\n");
        return;
    }

    char output[256];
    while (fgets(output, sizeof(output), fp) != NULL) {
        printf("mpg123 output: %s", output);
    }

    int result = pclose(fp);
    if (result != 0) {
        fprintf(stderr, "mpg123 returned an error: %d\n", result);
        snprintf(command, sizeof(command), "mpg123 -v -q -f %d \"%s\" &", mpg123_volume, SOUND_FILE);
    }
}



// Function to write PID file
void write_pid_file() {
    FILE *f = fopen(PID_FILE, "w");
    if (f) {
        fprintf(f, "%d", getpid());
        fclose(f);
    }
}

void handle_libinput_events(struct libinput *li) {
    struct libinput_event *event;
    time_t last_trigger = 0;

    if (access(SOUND_FILE, F_OK) == -1) {
        fprintf(stderr, "Error: Sound file not found at %s\n", SOUND_FILE);
        exit(1);
    }

    printf("Sound file found. Ready to play on TrackPoint movement (Volume: %d%%, Cooldown: %d seconds)\n",
           volume_level, COOLDOWN_SECONDS);

    while (running) {
        libinput_dispatch(li);

        while ((event = libinput_get_event(li)) != NULL) {
            enum libinput_event_type event_type = libinput_event_get_type(event);
            time_t current_time = time(NULL);

            if ((event_type == LIBINPUT_EVENT_POINTER_MOTION ||
                 event_type == LIBINPUT_EVENT_POINTER_BUTTON) &&
                (current_time - last_trigger >= COOLDOWN_SECONDS)) {
                    play_sound();
                    last_trigger = current_time;
            }

            libinput_event_destroy(event);
        }

        usleep(10000);  // 10ms sleep
    }
}

int main(int argc, char *argv[]) {
    struct libinput *li;
    struct libinput_device *device;
    const char *device_path = "/dev/input/event5";

    // Parse command-line arguments for custom volume
    if (argc == 2) {
        volume_level = atoi(argv[1]);
        if (volume_level < 1 || volume_level > 100) {
            fprintf(stderr, "Error: Volume must be between 1 and 100\n");
            return 1;
        }
    }

    // Set up signal handlers
    signal(SIGTERM, handle_signal);
    signal(SIGINT, handle_signal);

    // Write PID file
    write_pid_file();

    li = libinput_path_create_context(&interface, NULL);
    if (!li) {
        fprintf(stderr, "Failed to create libinput context: %s\n", strerror(errno));
        return 1;
    }

    device = libinput_path_add_device(li, device_path);
    if (!device) {
        fprintf(stderr, "Failed to open device: %s\n", strerror(errno));
        libinput_unref(li);
        return 1;
    }

    printf("TrackPoint sound service started with volume: %d%%.\n", volume_level);
    handle_libinput_events(li);

    // Cleanup
    printf("Unreferencing libinput context and device...\n");
    if (li) {
        libinput_unref(li);
    }
    if (device) {
        libinput_device_unref(device);
    }
    printf("Finished unreferencing.\n");

    // libinput_device_unref(device);
    // libinput_unref(li);
    unlink(PID_FILE);  // Remove PID file on exit

    return 0;
}
