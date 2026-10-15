
# Weather App

A Python-based Weather Application that fetches current weather information for a city using the OpenWeather API. It includes both a command-line interface (CLI) and a graphical user interface (GUI).

## Features

- Search current weather by city name
- Display temperature in Celsius
- Show feels-like temperature, humidity, and wind speed
- Display weather conditions with emojis
- Handle invalid city names and API errors
- Handle connection errors and request timeouts
- Secure API key configuration using an environment file
- GUI built with Python Tkinter
- Automated unit tests using Python unittest and mocked API responses

## Technologies Used

- Python
- Tkinter
- Requests
- python-dotenv
- OpenWeather API
- unittest

## Project Structure

```text
Weather-App/
├── .env
├── .gitignore
├── requirements.txt
├── weather_app.py
├── weather_app_gui.py
├── test_weather_app.py
└── README.md
```

The `.env` file is local configuration and must not be uploaded to GitHub.

## Requirements

- Python 3
- An OpenWeather account and API key
- Internet connection

## Installation

Open a terminal in the project directory and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## API Key Setup

1. Create an account at https://openweathermap.org/.
2. Generate an API key from your OpenWeather account.
3. Create a file named `.env` in the project directory.
4. Add the following line to the file:

```text
OWM_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key.

The application loads the key from `.env` using `python-dotenv`. Never hardcode your API key in Python files or publish it on GitHub.

## Run the CLI Application

```bash
python weather_app.py
```

Enter a city name when prompted. You can search for another city by answering `y` when asked.

## Run the GUI Application

```bash
python weather_app_gui.py
```

Enter a city name, click **Search Weather**, and view the weather report in the application window.

## Run Automated Tests

```bash
python -m unittest -v test_weather_app.py
```

The tests cover successful weather responses, invalid cities, invalid API keys, missing API keys, connection errors, and timeout errors. Mock responses are used to test the weather logic without making real API requests.

## Error Handling

- **404:** City not found
- **401:** API key invalid or not activated
- **Connection error:** Internet connection problem
- **Timeout:** Request took too long
- **Missing API key:** Configure `OWM_API_KEY` in the `.env` file

## Author

Dipesh Gunjal

## Project

Python Programming — Weather App
