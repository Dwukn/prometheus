#!/bin/bash
# /* ---- 💫 https://github.com/Dwukn 💫 ---- */  ##
# for rainbow borders animation

# Function to generate a random hex color
random_hex() {
    printf "0xff%s" "$(openssl rand -hex 3)"
}

# Generate 10 random rainbow colors
colors=()
for i in {1..10}; do
    colors+=("$(random_hex)")
done

# Set the active window border colors using the generated random colors
hyprctl keyword general:col.active_border "${colors[@]}" 270deg

# rainbow colors for inactive window (uncomment to take effect)
#hyprctl keyword general:col.inactive_border $(random_hex) $(random_hex) $(random_hex) $(random_hex) $(random_hex) $(random_hex) $(random_hex) $(random_hex) $(random_hex) $(random_hex) 270deg
