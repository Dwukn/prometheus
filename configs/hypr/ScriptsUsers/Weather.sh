#!/bin/bash
# /* ---- 💫 https://github.com/Dwukn 💫 ---- */
# Weather info from wttr.in (https://github.com/chubin/wttr.in)
# Remember to add the city!

city=
cachedir=~/.cache/rbn
cachefile=${0##*/}-$1

# Ensure the cache directory exists
if [ ! -d "$cachedir" ]; then
    mkdir -p "$cachedir"
fi

# Ensure the cache file exists
if [ ! -f "$cachedir/$cachefile" ]; then
    touch "$cachedir/$cachefile"
fi

# Save current IFS (Internal Field Separator)
SAVEIFS=$IFS
# Change IFS to newline for handling data correctly
IFS=$'\n'

# Check the cache age (in seconds)
cacheage=$(($(date +%s) - $(stat -c '%Y' "$cachedir/$cachefile")))

# If the cache is older than 29 minutes or empty, fetch new data
if [ "$cacheage" -gt 1740 ] || [ ! -s "$cachedir/$cachefile" ]; then
    data=($(curl -s "https://en.wttr.in/$city$1?0qnT" 2>&1))
    echo ${data[0]} | cut -f1 -d, > "$cachedir/$cachefile"
    echo ${data[1]} | sed -E 's/^.{15}//' >> "$cachedir/$cachefile"
    echo ${data[2]} | sed -E 's/^.{15}//' >> "$cachedir/$cachefile"
fi

# Read the cached weather data
weather=($(cat "$cachedir/$cachefile"))

# Restore IFS
IFS=$SAVEIFS

# Format the temperature range
temperature=$(echo ${weather[2]} | sed -E 's/([[:digit:]]+)\.\./\1 to /g')

# Default weather icon and condition
condition=""
case "$(echo ${weather[1]##*,} | tr '[:upper:]' '[:lower:]')" in
    "clear" | "sunny")
        condition=""
        ;;
    "partly cloudy")
        condition="󰖕"
        ;;
    "cloudy")
        condition=""
        ;;
    "overcast")
        condition=""
        ;;
    "fog" | "freezing fog")
        condition=""
        ;;
    "patchy rain possible" | "patchy light drizzle" | "light drizzle" | "patchy light rain" | "light rain" | "light rain shower" | "mist" | "rain")
        condition="󰼳"
        ;;
    "moderate rain at times" | "moderate rain" | "heavy rain at times" | "heavy rain" | "moderate or heavy rain shower" | "torrential rain shower" | "rain shower")
        condition=""
        ;;
    "patchy snow possible" | "patchy sleet possible" | "patchy freezing drizzle possible" | "freezing drizzle" | "heavy freezing drizzle" | "light freezing rain" | "moderate or heavy freezing rain" | "light sleet" | "ice pellets" | "light sleet showers" | "moderate or heavy sleet showers")
        condition="󰼴"
        ;;
    "blowing snow" | "moderate or heavy sleet" | "patchy light snow" | "light snow" | "light snow showers")
        condition="󰙿"
        ;;
    "blizzard" | "patchy moderate snow" | "moderate snow" | "patchy heavy snow" | "heavy snow" | "moderate or heavy snow with thunder" | "moderate or heavy snow showers")
        condition=""
        ;;
    "thundery outbreaks possible" | "patchy light rain with thunder" | "moderate or heavy rain with thunder" | "patchy light snow with thunder")
        condition=""
        ;;
    *)
        condition=""
        ;;
esac

# Format the output in JSON for Waybar or other status bar tools
echo -e "{\"text\":\"$temperature $condition\", \"alt\":\"${weather[0]}\", \"tooltip\":\"${weather[0]}: $temperature ${weather[1]}\"}"

# Generate the simple cached weather output for cache file
cached_weather=" $temperature\n$condition ${weather[1]}"

# Write the cached weather data to a file
echo -e "$cached_weather" > ~/.cache/.weather_cache
