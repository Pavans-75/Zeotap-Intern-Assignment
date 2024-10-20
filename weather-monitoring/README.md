# Weather Monitoring System

## Description
A real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system retrieves data from the OpenWeatherMap API for major Indian cities.

## Features
- Real-time weather data retrieval
- Daily weather summaries
- Alerting system based on user-configurable thresholds
- Support for additional weather parameters (humidity, wind speed)
- Forecast data retrieval

## Requirements
- Python 3.x
- Dependencies: `requests`, `pandas`, `python-dotenv`
- Docker (optional for running web servers and databases)

## Setup


1. Install dependencies:

	pip install requests pandas python-dotenv

2. Set up your OpenWeatherMap API key:
Get a free API key from OpenWeatherMap.
Create a .env file in the project root directory and add your API key:
	
	OPENWEATHER_API_KEY=your_openweathermap_api_key

3. Make sure to add .env to your .gitignore file to keep your API key secure:
	
	echo ".env" >> .gitignore

#Running the Application
Without Virtual Environment

1. Run the weather data script:	
	python weather_data.py
2. Run the data processing script:
	python data_processing.py
3. Run the alert system:
	python alerts.py

#With Virtual Environment
1. Create and activate a virtual environment:
	python -m venv env
	source env/bin/activate  # On Windows use `env\Scripts\activate`
2. Install dependencies in the virtual environment:
	pip install requests pandas python-dotenv
3. Run the scripts as described above.

# Testing
Run unit tests using:
	python -m unittest test_weather_monitoring.py

# Design Choices:

Language: Python was chosen for its simplicity and powerful libraries.
Data Processing: pandas is used for efficient data manipulation and aggregation.
Real-time Fetching: requests library is used for API calls.
Alerts: Custom logic to handle user-defined thresholds and alerts.
Extensions: Support for additional weather parameters and forecast data to enhance insights.
