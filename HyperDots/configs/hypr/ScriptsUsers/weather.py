# /* ---- 💫 https://github.com/Dwukn 💫 ---- */  
# Weather script using Python and pyquery

import subprocess
import json
import os
from pyquery import PyQuery

# Weather icons dictionary
weather_icons = {
    "sunnyDay": "󰖙",
    "clearNight": "󰖔",
    "cloudyFoggyDay": "",
    "cloudyFoggyNight": "",
    "rainyDay": "",
    "rainyNight": "",
    "snowyIcyDay": "",
    "snowyIcyNight": "",
    "severe": "",
    "default": "",
}

# Function to fetch weather data
def fetch_weather(location_id):
    url = f"https://weather.com/en-IN/weather/today/l/{location_id}"
    try:
        html_data = PyQuery(url=url)
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

    return html_data

# Function to extract weather details
def extract_weather_details(html_data):
    try:
        # Current temperature
        temp = html_data("span[data-testid='TemperatureValue']").eq(0).text()

        # Current weather status
        status = html_data("div[data-testid='wxPhrase']").text()
        status = f"{status[:16]}.." if len(status) > 16 else status

        # Status code and icon
        status_code = html_data("#regionHeader").attr("class").split(" ")[2].split("-")[2]
        icon = weather_icons.get(status_code, weather_icons["default"])

        # Temperature feels like
        temp_feel = html_data("div[data-testid='FeelsLikeSection'] > span > span[data-testid='TemperatureValue']").text()
        temp_feel_text = f"Feels like {temp_feel}°C"

        # Min-max temperatures
        temp_min = html_data("div[data-testid='wxData'] > span[data-testid='TemperatureValue']").eq(1).text()
        temp_max = html_data("div[data-testid='wxData'] > span[data-testid='TemperatureValue']").eq(0).text()
        temp_min_max = f" {temp_min}  {temp_max}"

        # Wind speed
        wind_speed = html_data("span[data-testid='Wind']").text().split("\n")[1]
        wind_text = f" {wind_speed}"

        # Humidity
        humidity = html_data("span[data-testid='PercentageValue']").text()
        humidity_text = f" {humidity}"

        # Visibility
        visibility = html_data("span[data-testid='VisibilityValue']").text()
        visibility_text = f" {visibility}"

        # Air quality index
        air_quality_index = html_data("text[data-testid='DonutChartValue']").text()

        # Hourly rain prediction
        prediction = html_data("section[aria-label='Hourly Forecast'] div[data-testid='SegmentPrecipPercentage'] > span").text()
        prediction = prediction.replace("Chance of Rain", "").strip()
        hourly_prediction = f"\n\n (hourly) {prediction}" if prediction else ""

        return {
            "temp": temp,
            "status": status,
            "status_code": status_code,
            "icon": icon,
            "temp_feel_text": temp_feel_text,
            "temp_min_max": temp_min_max,
            "wind_text": wind_text,
            "humidity_text": humidity_text,
            "visibility_text": visibility_text,
            "air_quality_index": air_quality_index,
            "hourly_prediction": hourly_prediction,
        }
    except Exception as e:
        print(f"Error extracting weather data: {e}")
        return None

# Function to format and print the output
def format_output(weather_data):
    if not weather_data:
        return

    tooltip_text = (
        f"\t\t{weather_data['temp']}\t\t\n"
        f"<big>{weather_data['icon']}</big>\n"
        f"<b>{weather_data['status']}</b>\n"
        f"<small>{weather_data['temp_feel_text']}</small>\n"
        f"<b>{weather_data['temp_min_max']}</b>\n"
        f"{weather_data['wind_text']}\t{weather_data['humidity_text']}\n"
        f"{weather_data['visibility_text']}\tAQI {weather_data['air_quality_index']}\n"
        f"<i>{weather_data['hourly_prediction']}</i>"
    )

    # Simple weather display
    simple_weather = (
        f"{weather_data['icon']}  {weather_data['status']}\n"
        f"  {weather_data['temp']} ({weather_data['temp_feel_text']})\n"
        f"  Wind Speed: {weather_data['wind_text']}\n"
        f"  Humidity: {weather_data['humidity_text']}\n"
        f"  Visibility: {weather_data['visibility_text']}\n"
        f"AQI: {weather_data['air_quality_index']}\n"
    )

    # Output JSON for Waybar module
    out_data = {
        "text": f"{weather_data['icon']}  {weather_data['temp']}",
        "alt": weather_data['status'],
        "tooltip": tooltip_text,
        "class": weather_data['status_code'],
    }

    print(json.dumps(out_data))

    # Save to weather cache file
    try:
        with open(os.path.expanduser("~/.cache/.weather_cache"), "w") as file:
            file.write(simple_weather)
    except Exception as e:
        print(f"Error writing weather data to cache: {e}")

# Main function to get the weather information
def main():
  # get location_id
# to get your own location_id, go to https://weather.com & search your location.
# once you choose your location, you can see the location_id in the URL(64 chars long hex string)
# like this: https://weather.com/en-IN/weather/today/l/bca47d1099e762a012b9a139c36f30a0b1e647f69c0c4ac28b537e7ae9c1c200
    location_id = "dc224dd10da9029e8170833dc5f304c65eb432381c1d2f014c1c7daeb5b4b3a5"  # Example location ID
    weather_data = fetch_weather(location_id)

    if weather_data:
        weather_details = extract_weather_details(weather_data)
        format_output(weather_details)

if __name__ == "__main__":
    main()
