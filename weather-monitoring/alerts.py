from weather_data import fetch_weather_data, CITIES

THRESHOLDS = {
    "temp_high": 35,  # degrees Celsius
    "consecutive_updates": 2
}
ALERTS = []

def check_alerts():
    temp_alert_count = {city: 0 for city in CITIES}
    while True:
        for city in CITIES:
            weather_data = fetch_weather_data(city)
            if weather_data:
                temp = weather_data["temp"]
                if temp > THRESHOLDS["temp_high"]:
                    temp_alert_count[city] += 1
                    if temp_alert_count[city] >= THRESHOLDS["consecutive_updates"]:
                        ALERTS.append(f"Alert! Temperature in {city} exceeds {THRESHOLDS['temp_high']}°C for consecutive updates.")
                        print(ALERTS[-1])
                else:
                    temp_alert_count[city] = 0

if __name__ == "__main__":
    check_alerts()
