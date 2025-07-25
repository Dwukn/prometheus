precmd() {
  # Get the last executed command from the history
  last_command=$(history 1 | sed 's/^[ ]*[0-9]*[ ]*//')

  # Measure the execution time of the last command if it's not empty
  if [[ -n "$last_command" ]]; then
    # Using `time` to measure execution time safely
    time_output=$( { time eval "$last_command"; } 2>&1 )

    # Extract the real time from the `time` output
    real_time=$(echo "$time_output" | grep real | awk '{print $2}')
    
    # Convert the time to seconds if it's in minutes or seconds
    if [[ "$real_time" =~ ([0-9]+)m([0-9]+\.[0-9]+)s ]]; then
      total_time=$(echo "$(((${BASH_REMATCH[1]} * 60) + ${BASH_REMATCH[2]}))")
    elif [[ "$real_time" =~ ([0-9]+\.[0-9]+)s ]]; then
      total_time="${BASH_REMATCH[1]}"
    fi

    # Show execution time if it takes more than 1 second
    if (( $(echo "$total_time > 1" | bc -l) )); then
      print -P "%F{yellow}Execution Time: $real_time%f"
    fi
  fi
}

