#!/bin/bash
# /* ---- 💫 https://github.com/Dwukn 💫 ---- */  ##
# Rofi menu for Quick Edit/View of Settings (SUPER E)

# Define preferred text editor and terminal
edit=${EDITOR:-nano}
tty=kitty

# Paths to configuration directories
configs="$HOME/.config/hypr/configs"
UserConfigs="$HOME/.config/hypr/UserConfigs"

# Function to display the menu options
menu() {
    cat <<EOF
1. Edit Decorations & Animations
2. Edit Keybinds
3. Edit System - Keybinds
4. Edit Monitors
5. Edit laptop configs
6. Edit Environment variables
7. Edit Startup_Apps
8. Edit User-Settings
9. Edit Window Rules
10. Edit Work-space Rules
EOF
}

# Main function to handle menu selection
main() {
    # Display the menu with rofi and allow multi-column layout
    choice=$(menu | rofi -i -dmenu -config ~/.config/rofi/config-compact.rasi -columns 2 | cut -d. -f1)

    # Map choices to corresponding files
    case $choice in
    # left side
        1) file="$UserConfigs/Animations.conf" ;;
        2) file="$configs/Keybinds.conf" ;;
        3) file="$UserConfigs/UserKeybinds.conf" ;;
        4) file="$UserConfigs/Monitors.conf" ;;
        5) file="$UserConfigs/Laptops.conf" ;;
        # right side
        6) file="$UserConfigs/EnvVariables.conf" ;;
        7) file="$UserConfigs/Startup_Apps.conf" ;;
        8) file="$UserConfigs/UserSettings.conf" ;;
        9) file="$UserConfigs/WorkspaceRules.conf" ;;
        10) file="$configs/Settings.conf" ;;
        *) return ;;  # Do nothing for invalid choices
    esac

    # Open the selected file in the terminal with the text editor
    $tty -e $edit "$file"
}

main
