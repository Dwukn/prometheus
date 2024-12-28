#!/bin/bash
# /* ---- 💫 https://github.com/Dwukn 💫 ---- */
# A bash script designed to run only once after dotfiles installation.

# This script runs once after the first boot and can be safely deleted once executed.
# The marker file: ~/.config/hypr/.initial_startup_done prevents the script from running more than once.

# Variables
scriptsDir="$HOME/.config/hypr/scripts"
wallpaper="$HOME/.config/hypr/wallpaper_effects/.wallpaper_modified"
waybar_style="$HOME/.config/waybar/style/[Dark] Latte-Wallust combined.css"
kvantum_theme="Catppuccin-Mocha"
color_scheme="prefer-dark"
gtk_theme="Andromeda-dark"
icon_theme="Flat-Remix-Blue-Dark"
cursor_theme="Bibata-Modern-Ice"
swww="swww img"
effect="--transition-bezier .43,1.19,1,.4 --transition-fps 30 --transition-type grow --transition-pos 0.925,0.977 --transition-duration 2"

# Check if the marker file exists; if not, proceed with the script execution.
if [ ! -f "$HOME/.config/hypr/.initial_startup_done" ]; then
    sleep 1  # Short delay to ensure everything is ready.

    # Initialize Wallust and set the wallpaper, if the wallpaper file exists.
    if [ -f "$wallpaper" ]; then
        wallust run -s "$wallpaper" > /dev/null
        swww query || swww-daemon && $swww "$wallpaper" "$effect"
        "$scriptsDir/WallustSwww.sh" > /dev/null 2>&1 &
    fi

    # Apply GTK themes and icon/cursor themes.
    gsettings set org.gnome.desktop.interface color-scheme "$color_scheme" > /dev/null 2>&1 &
    gsettings set org.gnome.desktop.interface gtk-theme "$gtk_theme" > /dev/null 2>&1 &
    gsettings set org.gnome.desktop.interface icon-theme "$icon_theme" > /dev/null 2>&1 &
    gsettings set org.gnome.desktop.interface cursor-theme "$cursor_theme" > /dev/null 2>&1 &
    gsettings set org.gnome.desktop.interface cursor-size 24 > /dev/null 2>&1 &

    # Apply Kvantum theme.
    kvantummanager --set "$kvantum_theme" > /dev/null 2>&1 &

    # Initialize the keyboard layout (since Waybar might not handle this).
    "$scriptsDir/SwitchKeyboardLayout.sh" > /dev/null 2>&1 &

    # Apply initial Waybar style.
    if [ -f "$waybar_style" ]; then
        ln -sf "$waybar_style" "$HOME/.config/waybar/style.css"
        # Refresh Waybar, Sway, Rofi, etc.
        "$scriptsDir/Refresh.sh" > /dev/null 2>&1 &
    fi

    # Create a marker file to indicate the script has run.
    touch "$HOME/.config/hypr/.initial_startup_done"

    exit  # Exit after running the script once.
fi

