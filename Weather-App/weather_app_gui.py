import tkinter as tk
from threading import Thread
from queue import Queue, Empty

from weather_app import get_weather


# Theme
BG = "#F1F5F9"
CARD = "#FFFFFF"
TEXT = "#172033"
MUTED = "#64748B"
BLUE = "#2563EB"

result_queue = Queue()

root = tk.Tk()
root.title("Weather App")
root.geometry("500x570")
root.resizable(False, False)
root.configure(bg=BG)


# Header
title = tk.Label(
    root,
    text="Weather App",
    font=("Segoe UI", 25, "bold"),
    bg=BG,
    fg=TEXT
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Check the weather in any city",
    font=("Segoe UI", 11),
    bg=BG,
    fg=MUTED
)
subtitle.pack(pady=(0, 20))


# Main card
card = tk.Frame(root, bg=CARD, padx=25, pady=22)
card.pack(fill="x", padx=25)

city_label = tk.Label(
    card,
    text="Enter City Name",
    font=("Segoe UI", 11, "bold"),
    bg=CARD,
    fg=TEXT
)
city_label.pack(anchor="w")

city_entry = tk.Entry(
    card,
    font=("Segoe UI", 13),
    relief="solid",
    bd=1
)
city_entry.pack(fill="x", pady=(8, 14), ipady=8)


# Status message
status_label = tk.Label(
    card,
    text="Enter a city to get started.",
    font=("Segoe UI", 10),
    bg=CARD,
    fg=MUTED,
    wraplength=390
)
status_label.pack(pady=(0, 12))


# Search button
search_button = tk.Button(
    card,
    text="Search Weather",
    font=("Segoe UI", 12, "bold"),
    bg=BLUE,
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=lambda: search_weather(),
    pady=9
)
search_button.pack(fill="x")


# Weather result area
result_frame = tk.Frame(root, bg=CARD, padx=22, pady=18)
result_frame.pack(fill="x", padx=25, pady=18)

location_label = tk.Label(
    result_frame,
    text="Weather Report",
    font=("Segoe UI", 17, "bold"),
    bg=CARD,
    fg=TEXT
)
location_label.pack()

condition_label = tk.Label(
    result_frame,
    text="🌤️ Condition: --",
    font=("Segoe UI", 12),
    bg=CARD,
    fg=BLUE
)
condition_label.pack(pady=7)

temperature_label = tk.Label(
    result_frame,
    text="Temperature: -- °C",
    font=("Segoe UI", 13, "bold"),
    bg=CARD,
    fg=TEXT
)
temperature_label.pack(pady=3)

feels_label = tk.Label(
    result_frame,
    text="Feels Like: -- °C",
    font=("Segoe UI", 10),
    bg=CARD,
    fg=MUTED
)
feels_label.pack(pady=3)

humidity_label = tk.Label(
    result_frame,
    text="Humidity: -- %",
    font=("Segoe UI", 10),
    bg=CARD,
    fg=MUTED
)
humidity_label.pack(pady=3)

wind_label = tk.Label(
    result_frame,
    text="Wind Speed: -- m/s",
    font=("Segoe UI", 10),
    bg=CARD,
    fg=MUTED
)
wind_label.pack(pady=3)


def search_weather():
    city = city_entry.get().strip()

    if not city:
        status_label.config(
            text="Please enter a city name.",
            fg="#DC2626"
        )
        city_entry.focus_set()
        return

    search_button.config(state="disabled", text="Searching...")
    status_label.config(text="Fetching weather data...", fg=BLUE)

    def fetch_data():
        try:
            result = get_weather(city)
        except Exception:
            result = {
                "error": "Something went wrong. Please try again."
            }

        result_queue.put(result)

    Thread(target=fetch_data, daemon=True).start()


def display_weather(data):
    search_button.config(state="normal", text="Search Weather")

    if "error" in data:
        status_label.config(
            text=f"Error: {data['error']}",
            fg="#DC2626"
        )
        return

    condition = data.get("condition", "").lower()

    if condition == "clear":
        emoji, color = "☀️", "#D97706"
    elif condition == "clouds":
        emoji, color = "☁️", "#64748B"
    elif "thunderstorm" in condition:
        emoji, color = "⛈️", "#4338CA"
    elif "rain" in condition or "drizzle" in condition:
        emoji, color = "🌧️", "#2563EB"
    elif "snow" in condition:
        emoji, color = "❄️", "#0891B2"
    else:
        emoji, color = "🌤️", "#0F766E"

    location_label.config(
        text=f"{data['city']}, {data['country']}"
    )
    condition_label.config(
        text=f"{emoji} {data['description'].title()}",
        fg=color
    )
    temperature_label.config(
        text=f"Temperature: {data['temperature']} °C"
    )
    feels_label.config(
        text=f"Feels Like: {data['feels_like']} °C"
    )
    humidity_label.config(
        text=f"Humidity: {data['humidity']}%"
    )
    wind_label.config(
        text=f"Wind Speed: {data['wind_speed']} m/s"
    )

    status_label.config(
        text="Weather updated successfully!",
        fg="#15803D"
    )


def check_result_queue():
    try:
        result = result_queue.get_nowait()
    except Empty:
        pass
    else:
        display_weather(result)

    root.after(100, check_result_queue)


# Press Enter to search
city_entry.bind("<Return>", lambda event: search_weather())

root.after(100, check_result_queue)
city_entry.focus_set()
root.mainloop()