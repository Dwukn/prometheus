# ~/.oh-my-zsh/custom/plugins/wallpaper-theme/wallpaper-theme.plugin.zsh

# Function to read the wallpaper color from the file
get_wallpaper_color() {
  if [ -f "$ZSH_CUSTOM/plugins/wallpaper-theme/.wallpaper_color" ]; then
    cat "$ZSH_CUSTOM/plugins/wallpaper-theme/.wallpaper_color"
  else
    echo "ffffff"  # Default color if the file doesn't exist
  fi
}

# Function to extract the dominant color from the wallpaper
extract_wallpaper_color() {
  # Wallpaper path (you can adjust this path as needed)
  WALLPAPER_PATH="$HOME/.config/hypr/wallpaper_effects/.wallpaper_current"

  # Extract the dominant color from the wallpaper using ImageMagick
  if [ -f "$WALLPAPER_PATH" ]; then
    COLOR=$(convert "$WALLPAPER_PATH" -resize 100x100^ -gravity center -crop 100x100+0+0 -format "%[pixel:p{0,0}]" info:-)
    COLOR=$(echo $COLOR | sed 's/#[0-9a-fA-F]*\(.*\)/\1/')  # Clean color code
    echo $COLOR > "$ZSH_CUSTOM/plugins/wallpaper-theme/.wallpaper_color"
  fi
}

# Initialize: set color based on wallpaper
if [[ -f "$HOME/.config/hypr/wallpaper_effects/.wallpaper_current" ]]; then
  extract_wallpaper_color
fi

# Set the prompt color dynamically
autoload -U colors && colors
wallpaper_color=$(get_wallpaper_color)

PROMPT='%F{#'$wallpaper_color'}%n@%m %F{green}%~ %F{reset}'
