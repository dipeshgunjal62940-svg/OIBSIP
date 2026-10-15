
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load API key from the .env file
load_dotenv(Path(__file__).with_name(".env"), override=True)


API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data for a city using the OpenWeather API."""

    api_key = os.environ.get("OWM_API_KEY")

    if not api_key:
        return {"error": "API key not found. Please set OWM_API_KEY."}

    try:
        response = requests.get(
            API_URL,
            params={
                "q": city,
                "appid": api_key,
                "units": "metric"
            },
            timeout=10
        )

        if response.status_code == 401:
            return {
                "error": "API key is invalid or not activated yet. Please check your key."
            }

        if response.status_code == 404:
            return {
                "error": f"City '{city}' was not found. Please check the spelling."
            }

        response.raise_for_status()
        data = response.json()

        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "condition": data["weather"][0]["main"],
            "wind_speed": data["wind"]["speed"]
        }

    except requests.exceptions.ConnectionError:
        return {"error": "Connection failed. Please check your internet."}

    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Please try again."}

    except requests.exceptions.RequestException:
        return {"error": "Unable to fetch weather data. Please try again."}

    except (KeyError, IndexError, TypeError, ValueError):
        return {"error": "The weather service returned unexpected data."}


def display_weather(weather):
    """Display weather information in a readable format."""

    if "error" in weather:
        print(f"\nError: {weather['error']}")
        return

    condition = weather["condition"].lower()

    if condition == "clear":
        emoji = "☀️"
    elif condition == "clouds":
        emoji = "☁️"
    elif "rain" in condition or "drizzle" in condition:
        emoji = "🌧️"
    elif "snow" in condition:
        emoji = "❄️"
    elif "thunderstorm" in condition:
        emoji = "⛈️"
    else:
        emoji = "🌤️"

    print("\n" + "=" * 40)
    print(f" WEATHER REPORT: {weather['city']}, {weather['country']}")
    print("=" * 40)
    print(f"Condition    : {emoji} {weather['description'].title()}")
    print(f"Temperature  : {weather['temperature']} °C")
    print(f"Feels Like   : {weather['feels_like']} °C")
    print(f"Humidity     : {weather['humidity']}%")
    print(f"Wind Speed   : {weather['wind_speed']} m/s")
    print("=" * 40)


def main():
    print("=" * 40)
    print("       WEATHER APP")
    print("=" * 40)

    while True:
        city = input("\nEnter city name: ").strip()

        while not city:
            print("City name cannot be empty. Please try again.")
            city = input("Enter city name: ").strip()

        weather = get_weather(city)
        display_weather(weather)

        another = input("\nSearch another city? (y/n): ").strip().lower()

        if another not in ("y", "yes"):
            print("\nThank you for using Weather App!")
            break


if __name__ == "__main__":
    main()
