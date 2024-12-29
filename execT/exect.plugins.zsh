# zsh-timer.plugin.zsh
# Enhanced plugin to time command execution in Zsh with threshold and exclusions

# User-configurable threshold in milliseconds (default: 1000ms = 1 second)
ZSH_TIMER_THRESHOLD=${ZSH_TIMER_THRESHOLD:-5000}

# Excluded commands (commands you don't want to time)
EXCLUDED_COMMANDS=("cd" "history" "exit")

# Function to capture the start time before the command is executed
function preexec() {
  # Check if the command is in the excluded list
  for cmd in "${EXCLUDED_COMMANDS[@]}"; do
    if [[ "$1" == "$cmd"* ]]; then
      return 0  # Skip timing this command
    fi
  done

  # Record the start time in milliseconds
  START_TIME=$(date +%s%3N)
}

# Function to calculate and display the elapsed time after the command is executed
function precmd() {

  if [[ -n "$START_TIME" ]]; then
    END_TIME=$(date +%s%3N)
    DIFF_TIME=$((END_TIME - START_TIME))

    # Only show time if the command execution time exceeds the threshold
    if [[ $DIFF_TIME -gt $ZSH_TIMER_THRESHOLD ]]; then
      SECONDS=$((DIFF_TIME / 1000))
      MILLISECONDS=$((DIFF_TIME % 1000))

      # Show time in seconds and milliseconds
      echo "Took $SECONDS.$MILLISECONDS s"
    fi
  fi
}

