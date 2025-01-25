#!/bin/bash

# ~/.oh-my-zsh/custom/plugins/wallpaper-theme/wallpaper_color.sh

WALLPAPER_PATH="$HOME/.config/hypr/wallpaper_effects/.wallpaper_current"

# Check if the wallpaper file exists
if [ -f "$WALLPAPER_PATH" ]; then
  # Extract the dominant color from the wallpaper
  COLOR=$(convert "$WALLPAPER_PATH" -resize 100x100^ -gravity center -crop 100x100+0+0 -format "%[pixel:p{0,0}]" info:-)

  # Clean up color code and save it to a file
  COLOR=$(echo $COLOR | sed 's/#[0-9a-fA-F]*\(.*\)/\1/')
  echo $COLOR > "$ZSH_CUSTOM/plugins/wallpaper-theme/.wallpaper_color"
fi
