# Zeotap-Intern-Assignment
# Rule Engine with AST

## Overview

This project implements a simple 3-tier rule engine application using an Abstract Syntax Tree (AST) to determine user eligibility based on attributes like age, department, income, spend, etc. The system allows for dynamic creation, combination, and modification of these rules through a web-based interface.

## Features

- **Create Rules**: Define eligibility rules using conditions on attributes.
- **Combine Rules**: Combine multiple rules into a single comprehensive rule.
- **Evaluate Rules**: Evaluate user data against combined rules to determine eligibility.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, JavaScript
- **Database**: SQLite
- **Testing**: Unittest

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLite

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/rule-engine.git
   cd rule-engine

2. **Install dependencies**:
	pip install Flask

3. **Initialize the database**:
	python database.py

### Running the Application

1. **Start the Flask server**:
	python api/app.py

2. Open the application in your browser: Go to http://localhost:5000

### Usage

**Create a Rule**:

1. Enter a rule in the format: (age > 30 AND department == 'Sales')
2. Click on "Create Rule"

**Combine Rules**:

1. Enter multiple rules separated by commas: (age > 30 AND department == 'Sales'), (salary > 50000), (experience > 5)
2. Click on "Combine Rules"

**Evaluate Rule**

1. Enter user data in JSON format:
	{
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
}
2. Click on "Evaluate Rule"

### Running Tests

1. **Run the tests**:
	python -m unittest test/test_ast_rule.py


