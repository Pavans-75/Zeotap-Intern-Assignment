import unittest
from weather_data import kelvin_to_celsius, fetch_weather_data, fetch_weather_forecast
from data_processing import update_weather_data, calculate_daily_summary
from alerts import check_alerts

class TestWeatherMonitoring(unittest.TestCase):

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)
        self.assertAlmostEqual(kelvin_to_celsius(0), -273.15)

    def test_fetch_weather_data(self):
        city = "Delhi"
        result = fetch_weather_data(city)
        self.assertIsNotNone(result)
        self.assertIn("temp", result)
        self.assertIn("humidity", result)
        self.assertIn("wind_speed", result)

    def test_fetch_weather_forecast(self):
        city = "Mumbai"
        forecasts = fetch_weather_forecast(city)
        self.assertIsNotNone(forecasts)
        self.assertGreater(len(forecasts), 0)
        self.assertIn("temp", forecasts[0])
        self.assertIn("humidity", forecasts[0])
        self.assertIn("wind_speed", forecasts[0])

    def test_daily_summary(self):
        update_weather_data()
        summary = calculate_daily_summary()
        self.assertIsNotNone(summary)
        self.assertIn("temp", summary.columns)
        self.assertIn("humidity", summary.columns)
        self.assertIn("wind_speed", summary.columns)

    def test_alerts(self):
        pass  # Alerts test to be added here

if __name__ == '__main__':
    unittest.main()
