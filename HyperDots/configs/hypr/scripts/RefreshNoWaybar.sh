#!/bin/bash
# /* ---- 💫 https://github.com/Dwukn 💫 ---- */  ##

# Modified version of Refresh.sh for automatic wallpaper change.
# This script refreshes rofi background, Wallust, and SwayNC only.
# Waybar refresh is not included.

SCRIPTSDIR="$HOME/.config/hypr/scripts"
UserScripts="$HOME/.config/hypr/UserScripts"

# Function to check if a file exists
file_exists() {
    [[ -e "$1" ]] && return 0 || return 1
}

# Kill already running rofi processes (if any)
kill_running_process() {
    local process="$1"
    if pidof "$process" >/dev/null; then
        pkill "$process"
    fi
}

# List of processes to terminate
processes_to_kill=(rofi)

# Kill each process in the list
for process in "${processes_to_kill[@]}"; do
    kill_running_process "$process"
done

# Quit ags gracefully
ags -q

# Refresh Wallust (trigger wallpaper update)
"${SCRIPTSDIR}/WallustSwww.sh" &

# Relaunch Rainbow Borders script if it exists
sleep 1
if file_exists "${UserScripts}/RainbowBorders.sh"; then
    "${UserScripts}/RainbowBorders.sh" &
fi

exit 0
