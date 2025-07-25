#!/bin/bash
# /* ---- 💫 https://github.com/Dwukn 💫 ---- */  ##
# Source: https://wiki.archlinux.org/title/Hyprland#Using_a_script_to_change_wallpaper_every_X_minutes

# This script randomly selects an image from a specified directory
# and sets it as the wallpaper at regular intervals.
#
# Note: This script is written in Bash (not POSIX shell) for using the RANDOM variable.

# Refresh script to update wallpaper on specific events
wallust_refresh="$HOME/.config/hypr/scripts/RefreshNoWaybar.sh"

# Get the name of the currently focused monitor using Hyprland's `hyprctl`
focused_monitor=$(hyprctl monitors | awk '/^Monitor/ {name=$2} /focused: yes/ {print name}')

# Ensure the user has provided a valid directory as an argument
if [[ $# -lt 1 ]] || [[ ! -d $1 ]]; then
    echo "Usage: $0 <dir containing images>"
    exit 1
fi

# Configuration options for wallpaper transition
export SWWW_TRANSITION_FPS=60          # Frame rate for transition
export SWWW_TRANSITION_TYPE="simple"   # Type of transition

# Interval in seconds between wallpaper changes (default: 1800 seconds / 30 minutes)
INTERVAL=1800

# Infinite loop to continuously change the wallpaper at intervals
while true; do
    # Find all image files in the specified directory
    find "$1" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" -o -iname "*.bmp" \) \
    | while read -r img; do
        # Assign a random number to each image to shuffle the order
        echo "$((RANDOM % 1000)):$img"
    done \
    | sort -n | cut -d':' -f2- \   # Sort the images by random number and remove the random part
    | while read -r img; do
        # Set the selected image as the wallpaper for the focused monitor
        swww img -o "$focused_monitor" "$img"

        # Call the refresh script to trigger any necessary updates in the environment
        "$wallust_refresh"

        # Wait for the specified interval before changing the wallpaper
        sleep "$INTERVAL"
    done
done
