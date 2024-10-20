import pandas as pd
from weather_data import fetch_weather_data, CITIES

WEATHER_DATA = []

def update_weather_data():
    for city in CITIES:
        weather_data = fetch_weather_data(city)
        if weather_data:
            WEATHER_DATA.append(weather_data)

def calculate_daily_summary():
    df = pd.DataFrame(WEATHER_DATA)
    df['dt'] = pd.to_datetime(df['dt'])
    daily_summary = df.groupby(df['dt'].dt.date).agg({
        "temp": ["mean", "max", "min"],
        "humidity": "mean",
        "wind_speed": "mean",
        "main": lambda x: x.mode()[0]  # Dominant weather condition
    })
    return daily_summary

if __name__ == "__main__":
    update_weather_data()
    summary = calculate_daily_summary()
    print(summary)
