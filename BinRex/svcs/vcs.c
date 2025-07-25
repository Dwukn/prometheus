// simple_vcs.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "vcs.h"
#include <sys/stat.h>
#include <sys/types.h>
#include <dirent.h>
#include <unistd.h>


int check_vcs_exists(void) {
    DIR* dir = opendir(VCS_DIR);
    if (dir) {
        closedir(dir);
        return 1;
    }
    return 0;
}

int vcs_init(void) {
    // Check if repository already exists
    if (check_vcs_exists()) {
        printf("Repository already initialized in %s\n", VCS_DIR);
        return 0;
    }

    // Create .simple_vcs directory
    if (mkdir(VCS_DIR, 0755) != 0) {
        printf("Error: Failed to create %s directory\n", VCS_DIR);
        return -1;
    }

    // Create objects directory
    if (mkdir(OBJECTS_DIR, 0755) != 0) {
        printf("Error: Failed to create %s directory\n", OBJECTS_DIR);
        rmdir(VCS_DIR);
        return -1;
    }

    // Create empty index file
    FILE* index = fopen(INDEX_FILE, "w");
    if (!index) {
        printf("Error: Failed to create index file\n");
        rmdir(OBJECTS_DIR);
        rmdir(VCS_DIR);
        return -1;
    }
    fclose(index);

    printf("Initialized empty version control repository in %s\n", VCS_DIR);
    return 0;
}

int vcs_add(const char* path) {
    // Check if repository exists
    if (!check_vcs_exists()) {
        printf("Error: Not a version control repository (run 'init' first)\n");
        return -1;
    }

    struct stat file_stat;
    if (stat(path, &file_stat) != 0) {
        printf("Error: File '%s' does not exist\n", path);
        return -1;
    }

    // Calculate file hash
    char* hash = calculate_file_hash(path);
    if (!hash) {
        printf("Error: Failed to calculate file hash\n");
        return -1;
    }

    // Create file entry
    FileEntry entry;
    strncpy(entry.path, path, MAX_PATH - 1);
    strncpy(entry.hash, hash, 40);
    entry.timestamp = file_stat.st_mtime;

    // Copy file to objects directory
    char obj_path[MAX_PATH];
    snprintf(obj_path, MAX_PATH, "%s/%s", OBJECTS_DIR, entry.hash);
    if (copy_file(path, obj_path) != 0) {
        printf("Error: Failed to copy file to objects directory\n");
        free(hash);
        return -1;
    }
    free(hash);

    // Save to index
    if (save_to_index(&entry) != 0) {
        printf("Error: Failed to update index\n");
        return -1;
    }

    printf("Added '%s' to index\n", path);
    return 0;
}

int vcs_commit(const char* message) {
    // Check if repository exists
    if (!check_vcs_exists()) {
        printf("Error: Not a version control repository (run 'init' first)\n");
        return -1;
    }

    FileEntry* entries;
    int count;

    if (read_from_index(&entries, &count) != 0) {
        printf("Error: Failed to read index\n");
        return -1;
    }

    if (count == 0) {
        printf("Nothing to commit (add files first)\n");
        free(entries);
        return 0;
    }

    // Create commit file with message and file list
    time_t now = time(NULL);
    char commit_path[MAX_PATH];
    snprintf(commit_path, MAX_PATH, "%s/commit_%ld", OBJECTS_DIR, now);

    FILE* commit_file = fopen(commit_path, "w");
    if (!commit_file) {
        printf("Error: Failed to create commit file\n");
        free(entries);
        return -1;
    }

    // Write commit header
    fprintf(commit_file, "Commit: %ld\n", now);
    fprintf(commit_file, "Message: %s\n", message);
    fprintf(commit_file, "Files:\n");

    // Write file entries in a clear format
    for (int i = 0; i < count; i++) {
        fprintf(commit_file, "%s %s\n", entries[i].hash, entries[i].path);
    }

    fclose(commit_file);
    free(entries);

    // Clear index after successful commit
    FILE* index = fopen(INDEX_FILE, "w");
    if (index) {
        fclose(index);
    }

    printf("Created commit with timestamp: %ld\n", now);
    return 0;
}



// Utility functions remain the same
char* calculate_file_hash(const char* path) {
    char* hash = malloc(41);
    snprintf(hash, 41, "%020ld", (long)time(NULL));
    return hash;
}

int copy_file(const char* source, const char* destination) {
    FILE *src = fopen(source, "rb");
    if (!src) return -1;

    FILE *dst = fopen(destination, "wb");
    if (!dst) {
        fclose(src);
        return -1;
    }

    char buffer[4096];
    size_t bytes;
    while ((bytes = fread(buffer, 1, sizeof(buffer), src)) > 0) {
        fwrite(buffer, 1, bytes, dst);
    }

    fclose(src);
    fclose(dst);
    return 0;
}

int save_to_index(FileEntry* entry) {
    FILE* index = fopen(INDEX_FILE, "a");
    if (!index) return -1;

    fprintf(index, "%s %s %ld\n", entry->path, entry->hash, entry->timestamp);
    fclose(index);
    return 0;
}

int read_from_index(FileEntry** entries, int* count) {
    FILE* index = fopen(INDEX_FILE, "r");
    if (!index) return -1;

    *count = 0;
    *entries = malloc(sizeof(FileEntry) * 100);  // Assume max 100 files

    while (!feof(index) && *count < 100) {
        FileEntry* entry = &(*entries)[*count];
        if (fscanf(index, "%s %s %ld\n", entry->path, entry->hash, &entry->timestamp) == 3) {
            (*count)++;
        }
    }

    fclose(index);
    return 0;
}


// Add these new functions to simple_vcs.c
int is_hidden_file(const char* path) {
    const char* filename = strrchr(path, '/');
    if (filename) {
        filename++; // Skip the slash
    } else {
        filename = path;
    }
    return filename[0] == '.';
}

int is_vcs_directory(const char* path) {
    return strstr(path, VCS_DIR) != NULL;
}

int vcs_add_multiple(int count, char** files) {
    if (!check_vcs_exists()) {
        printf("Error: Not a version control repository (run 'init' first)\n");
        return -1;
    }

    int success_count = 0;
    for (int i = 0; i < count; i++) {
        if (vcs_add(files[i]) == 0) {
            success_count++;
        }
    }

    printf("Successfully added %d out of %d files\n", success_count, count);
    return (success_count == count) ? 0 : -1;
}

// In vcs_add_all function, replace the previous implementation with this:
int vcs_add_all(void) {
    if (!check_vcs_exists()) {
        printf("Error: Not a version control repository (run 'init' first)\n");
        return -1;
    }

    DIR *dir;
    struct dirent *entry;
    struct stat path_stat;
    int files_added = 0;
    int total_files = 0;

    dir = opendir(".");
    if (!dir) {
        printf("Error: Cannot open current directory\n");
        return -1;
    }

    // First pass: count total eligible files
    while ((entry = readdir(dir)) != NULL) {
        // Skip . and .. directories
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }

        // Get file status
        if (stat(entry->d_name, &path_stat) != 0) {
            continue;
        }

        // Check if it's a regular file and not hidden/vcs file
        if (S_ISREG(path_stat.st_mode) &&
            !is_hidden_file(entry->d_name) &&
            !is_vcs_directory(entry->d_name)) {
            total_files++;
        }
    }

    if (total_files == 0) {
        printf("No files found to add\n");
        closedir(dir);
        return 0;
    }

    // Reset directory stream
    rewinddir(dir);

    // Second pass: add files
    while ((entry = readdir(dir)) != NULL) {
        // Skip . and .. directories
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }

        // Get file status
        if (stat(entry->d_name, &path_stat) != 0) {
            continue;
        }

        // Check if it's a regular file and not hidden/vcs file
        if (S_ISREG(path_stat.st_mode) &&
            !is_hidden_file(entry->d_name) &&
            !is_vcs_directory(entry->d_name)) {
            if (vcs_add(entry->d_name) == 0) {
                files_added++;
            }
        }
    }

    closedir(dir);
    printf("Added %d out of %d files\n", files_added, total_files);
    return (files_added > 0) ? 0 : -1;
}


int list_commits(CommitEntry** commits, int* count) {
    DIR *dir;
    struct dirent *entry;
    *count = 0;

    // Allocate initial space for commits
    *commits = malloc(sizeof(CommitEntry) * 100);  // Maximum 100 commits
    if (!*commits) return -1;

    dir = opendir(OBJECTS_DIR);
    if (!dir) return -1;

    while ((entry = readdir(dir)) != NULL) {
        if (strncmp(entry->d_name, "commit_", 7) == 0) {
            char commit_path[MAX_PATH];
            snprintf(commit_path, MAX_PATH, "%s/%s", OBJECTS_DIR, entry->d_name);

            FILE* commit_file = fopen(commit_path, "r");
            if (commit_file) {
                CommitEntry* current = &(*commits)[*count];
                char line[MAX_MSG_LEN];

                // Read timestamp
                if (fgets(line, sizeof(line), commit_file)) {
                    sscanf(line, "Commit: %ld", &current->timestamp);
                }

                // Read message
                if (fgets(line, sizeof(line), commit_file)) {
                    sscanf(line, "Message: %[^\n]", current->message);
                }

                // Generate simple hash from timestamp
                snprintf(current->hash, 41, "%020ld", current->timestamp);

                (*count)++;
                fclose(commit_file);
            }
        }
    }
    closedir(dir);
    return 0;
}

int vcs_log(void) {
    if (!check_vcs_exists()) {
        printf("Error: Not a version control repository\n");
        return -1;
    }

    CommitEntry* commits;
    int count;

    if (list_commits(&commits, &count) != 0) {
        printf("Error: Failed to read commit history\n");
        return -1;
    }

    if (count == 0) {
        printf("No commits found\n");
        free(commits);
        return 0;
    }

    printf("\nCommit History:\n");
    printf("---------------\n");
    for (int i = count - 1; i >= 0; i--) {
        char date[26];
        ctime_r(&commits[i].timestamp, date);
        date[24] = '\0';  // Remove newline

        printf("Commit: %s\n", commits[i].hash);
        printf("Date: %s\n", date);
        printf("Message: %s\n\n", commits[i].message);
    }

    free(commits);
    return 0;
}


int restore_file_from_objects(const char* hash, const char* path) {
    char source_path[MAX_PATH];
    snprintf(source_path, MAX_PATH, "%s/%s", OBJECTS_DIR, hash);

    // Check if source file exists
    if (access(source_path, F_OK) == -1) {
        printf("Error: Object file %s not found\n", hash);
        return -1;
    }

    // Copy file from objects to working directory
    if (copy_file(source_path, path) != 0) {
        printf("Error: Failed to restore %s\n", path);
        return -1;
    }

    printf("Restored: %s (hash: %s)\n", path, hash);
    return 0;
}


int restore_file_from_commit(const char* commit_hash) {
    char commit_path[MAX_PATH];
    snprintf(commit_path, MAX_PATH, "%s/commit_%s", OBJECTS_DIR, commit_hash);

    FILE* commit_file = fopen(commit_path, "r");
    if (!commit_file) {
        printf("Error: Commit %s not found\n", commit_hash);
        return -1;
    }

    // Skip header lines
    char line[MAX_PATH];
    while (fgets(line, sizeof(line), commit_file) && strcmp(line, "Files:\n") != 0);

    // Restore each file
    while (fgets(line, sizeof(line), commit_file)) {
        char hash[41], path[MAX_PATH];
        if (sscanf(line, "%s %s", hash, path) == 2) {
            char source[MAX_PATH], destination[MAX_PATH];
            snprintf(source, MAX_PATH, "%s/%s", OBJECTS_DIR, hash);
            strncpy(destination, path, MAX_PATH);

            if (copy_file(source, destination) != 0) {
                printf("Warning: Failed to restore %s\n", path);
            } else {
                printf("Restored: %s\n", path);
            }
        }
    }

    fclose(commit_file);
    return 0;
}

int vcs_restore(const char* commit_timestamp) {
    if (!check_vcs_exists()) {
        printf("Error: Not a version control repository\n");
        return -1;
    }

    // Convert timestamp to long
    long target_timestamp = atol(commit_timestamp);
    if (target_timestamp == 0) {
        printf("Error: Invalid commit timestamp\n");
        return -1;
    }

    char commit_path[MAX_PATH];
    snprintf(commit_path, MAX_PATH, "%s/commit_%ld", OBJECTS_DIR, target_timestamp);

    FILE* commit_file = fopen(commit_path, "r");
    if (!commit_file) {
        printf("Error: Commit with timestamp %ld not found\n", target_timestamp);
        return -1;
    }

    printf("Restoring files from commit %ld...\n", target_timestamp);

    char line[MAX_PATH * 2];
    int files_restored = 0;

    // Skip the header lines
    while (fgets(line, sizeof(line), commit_file)) {
        if (strstr(line, "Files:") != NULL) {
            break;
        }
    }

    // Read and restore each file
    while (fgets(line, sizeof(line), commit_file)) {
        char hash[41];
        char path[MAX_PATH];

        // Parse the line to get hash and path
        if (sscanf(line, "%s %s", hash, path) == 2) {
            if (restore_file_from_objects(hash, path) == 0) {
                files_restored++;
            }
        }
    }

    fclose(commit_file);

    if (files_restored > 0) {
        printf("Successfully restored %d files\n", files_restored);
        return 0;
    } else {
        printf("No files were restored\n");
        return -1;
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <command> [arguments]\n", argv[0]);
        printf("Commands:\n");
        printf("  init                Initialize new repository\n");
        printf("  add <file>          Add specific file to version control\n");
        printf("  add-multiple <files> Add multiple specific files\n");
        printf("  add-all            Add all files in current directory\n");
        printf("  commit <msg>        Commit changes\n");
        printf("  log                 Show commit history\n");
        printf("  restore <hash>    Restore files to a specific commit\n");
        return 1;
    }

    if (strcmp(argv[1], "init") == 0) {
        return vcs_init();
    }

    else if (strcmp(argv[1], "add") == 0) {
        if (argc < 3) {
            printf("Error: No file specified\n");
            return 1;
        }
        return vcs_add(argv[2]);
    }

    else if(strcmp(argv[1], "add-multiple") == 0) {
        if (argc < 3) {
            printf("Error: No files specified\n");
            return 1;
        }
        return vcs_add_multiple(argc - 2, argv + 2);
    }

    else if (strcmp(argv[1], "add .") == 0) {
        return vcs_add_all();
    }

    // else if (strcmp(argv[1], "") == 0) {
    //     return vcs_add_all();
    // }

    else if (strcmp(argv[1], "commit") == 0) {
        if (argc < 3) {
            printf("Error: No commit message provided\n");
            return 1;
        }
        return vcs_commit(argv[2]);
    }

    else if(strcmp(argv[1], "log") == 0) {
        return vcs_add_all();
    }

    else if(strcmp(argv[1], "restore") == 0) {
        return vcs_add_all();
    }
    else {
        printf("Unknown command: %s\n", argv[1]);
        return 1;
    }
}
