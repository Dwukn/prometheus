#!/bin/bash
# Clipboard Manager. This script uses cliphist, rofi, and wl-copy.

# Actions:
# CTRL Del to delete an entry
# ALT Del to wipe clipboard contents and reset counts

while true; do
    result=$(
        rofi -i -dmenu \
            -kb-custom-1 "Control-Delete" \
            -kb-custom-2 "Alt-Delete" \
            -config ~/.config/rofi/config-clipboard.rasi < <(cliphist list)
    )

    case "$?" in
        1)
            exit  # Exit if rofi is closed
            ;;
        0)
            case "$result" in
                "")
                    continue  # No selection, continue the loop
                    ;;
                *)
                    cliphist decode <<<"$result" | wl-copy  # Decode the selected item and copy it to clipboard
                    exit  # Exit after copying
                    ;;
            esac
            ;;
    esac

    # Handle custom key actions
    if [[ "$result" == *"Control-Delete"* ]]; then
        cliphist delete <<<"$result"  # Delete the selected entry
    elif [[ "$result" == *"Alt-Delete"* ]]; then
        # Wipe clipboard contents and reset counts
        cliphist wipe
        # Implement reset counts if needed
        echo "Resetting counts is not implemented in cliphist."
        # If you have a separate command for resetting counts, add it here.
    fi
done
