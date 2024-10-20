# Zeotap-Intern-Assignment
This repository contains the projects developed as part of the Zeotap Software Engineer Intern assignment. The projects demonstrate practical applications of real-time data processing and rule engine logic, focusing on two key systems:

#1. Rule Engine with AST
This project implements a 3-tier Rule Engine that utilizes Abstract Syntax Trees (AST) to manage dynamic rule creation and evaluation. The system is designed to determine user eligibility based on attributes like age, department, income, and spending patterns. The main features include:

**Dynamic Rule Creation: Users can create, modify, and combine rules.
**AST-Based Representation: Rules are represented using AST for efficient processing and evaluation.
**APIs and Simple UI: APIs for rule management and a UI for interaction.
**Error Handling and Validation: Robust error handling ensures smooth rule processing.

##Key Functionalities:
**create_rule: Create new rules dynamically.
**combine_rules: Combine multiple rules to form complex logical conditions.
**evaluate_rule: Evaluate rules based on user attributes and provide results.

#2. Real-Time Weather Monitoring System
The Real-Time Weather Monitoring System is a data-driven application that monitors and processes weather data in real-time. It retrieves weather data from the OpenWeatherMap API at regular intervals for cities in India and includes features for:

**Weather Data Processing: Fetch and store weather data every 5 minutes.
**Daily Summaries: Generate daily weather summaries, including average, max, and min temperatures.
**Alerts and Thresholds: Set alert thresholds for weather conditions and trigger alerts based on them.
**Data Visualizations: Graphical representation of the weather data over time.

#Features:
**Fetching live weather data using APIs.
**Processing weather information for multiple cities.
**Storing daily weather summaries.
**Providing configurable alerts based on weather conditions.
