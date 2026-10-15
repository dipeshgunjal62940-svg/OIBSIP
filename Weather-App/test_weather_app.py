import os
import unittest
from unittest.mock import Mock, patch

import requests
import weather_app


class TestWeatherApp(unittest.TestCase):

    def setUp(self):
        self.env_patcher = patch.dict(
            os.environ,
            {"OWM_API_KEY": "test-api-key"}
        )
        self.env_patcher.start()
        self.addCleanup(self.env_patcher.stop)

    def create_response(self, status_code, data=None):
        response = Mock()
        response.status_code = status_code
        response.json.return_value = data or {}
        return response

    @patch("weather_app.requests.get")
    def test_successful_weather_response(self, mock_get):
        mock_get.return_value = self.create_response(
            200,
            {
                "name": "Indore",
                "sys": {"country": "IN"},
                "main": {
                    "temp": 30.5,
                    "feels_like": 32.0,
                    "humidity": 55
                },
                "weather": [
                    {
                        "description": "clear sky",
                        "main": "Clear"
                    }
                ],
                "wind": {"speed": 3.5}
            }
        )

        result = weather_app.get_weather("Indore")

        self.assertEqual(result["city"], "Indore")
        self.assertEqual(result["country"], "IN")
        self.assertEqual(result["temperature"], 30.5)
        self.assertEqual(result["humidity"], 55)
        self.assertEqual(result["wind_speed"], 3.5)

        mock_get.assert_called_once_with(
            weather_app.API_URL,
            params={
                "q": "Indore",
                "appid": "test-api-key",
                "units": "metric"
            },
            timeout=10
        )

    @patch("weather_app.requests.get")
    def test_invalid_city_returns_404_error(self, mock_get):
        mock_get.return_value = self.create_response(404)

        result = weather_app.get_weather("Indoree")

        self.assertIn("error", result)
        self.assertIn("not found", result["error"].lower())

    @patch("weather_app.requests.get")
    def test_invalid_api_key_returns_401_error(self, mock_get):
        mock_get.return_value = self.create_response(401)

        result = weather_app.get_weather("Indore")

        self.assertIn("error", result)
        self.assertIn("api key", result["error"].lower())

    @patch("weather_app.requests.get")
    def test_missing_api_key(self, mock_get):
        with patch.dict(os.environ, {}, clear=True):
            result = weather_app.get_weather("Indore")

        self.assertIn("error", result)
        self.assertIn("api key not found", result["error"].lower())
        mock_get.assert_not_called()

    @patch("weather_app.requests.get")
    def test_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError

        result = weather_app.get_weather("Indore")

        self.assertIn("error", result)
        self.assertIn("connection failed", result["error"].lower())

    @patch("weather_app.requests.get")
    def test_timeout_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout

        result = weather_app.get_weather("Indore")

        self.assertIn("error", result)
        self.assertIn("timed out", result["error"].lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)