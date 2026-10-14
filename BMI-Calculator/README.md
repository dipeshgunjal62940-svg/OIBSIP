# BMI Calculator Using Python

A Python-based BMI Calculator featuring a command-line interface (CLI), graphical user interface (GUI), SQLite database, and BMI trend visualization.

## Project Overview

This project calculates Body Mass Index (BMI) using a person's weight and height. It provides both a terminal-based calculator and a desktop GUI built with Tkinter. BMI calculation records can be stored in SQLite and reviewed through a history table and a trend chart.

## Features

* **CLI Calculator:** Calculate BMI from the terminal.
* **GUI Calculator:** User-friendly desktop application using Tkinter.
* **Input Validation:** Handles non-numeric, zero, and negative values.
* **BMI Categories:** Underweight, Normal, Overweight, and Obese.
* **Category Colors:** Displays results with category-based colors.
* **SQLite Database:** Saves username, weight, height, BMI, category, and date.
* **Calculation History:** Displays records for a selected username.
* **BMI Trend Chart:** Visualizes BMI against date using Matplotlib when at least two records exist.
* **Error Handling:** Handles invalid input and SQLite database errors.

## Technologies Used

* Python 3
* Tkinter
* SQLite3
* Matplotlib
* Git and GitHub

## Project Structure

```text
BMI-Calculator/
├── bmi_cli.py
├── bmi_gui.py
├── README.md
├── requirements.txt
└── screenshots/
    ├── bmi_cli.png
    └── bmi_gui.png
```

The `bmi_records.db` file is created automatically when the GUI application runs. The local database is excluded from Git tracking to help protect personal records.

## Installation

### 1. Check Python

Install Python 3 if it is not already installed.

Verify your installation:

```bash
python --version
```

### 2. Install the dependency

Open a terminal in the `BMI-Calculator` folder and run:

```bash
python -m pip install -r requirements.txt
```

Tkinter and SQLite3 are included with most standard Windows Python installations.

## How to Run

### Command-Line Version

```bash
python bmi_cli.py
```

Enter your weight in kilograms and height in meters when prompted. Follow the instructions to calculate BMI again or exit.

### GUI Version

```bash
python bmi_gui.py
```

Enter your name, weight, and height, then click **Calculate BMI**.

Use **Show History** to review saved records and **Show Trend** to visualize changes in BMI over time. The trend chart requires at least two records.

Height can be entered in meters or centimeters, according to the application's input handling.

## Screenshots

Screenshots of the CLI and GUI will be added to the `screenshots/` directory.

### CLI Calculator

![CLI Calculator](screenshots/bmi_cli.png)

### GUI Calculator

![GUI Calculator](screenshots/bmi_gui.png)

## Learning Outcomes

Through this project, I practised:

* Python functions, loops, and conditional statements
* Input validation and exception handling
* Desktop GUI development with Tkinter
* SQLite database creation and parameterized SQL queries
* Data visualization with Matplotlib
* Organizing and documenting a Python project using Git and GitHub

## Disclaimer

BMI is a screening measure and does not diagnose health conditions. The categories used here are standard adult BMI ranges and may not be appropriate for every individual.

## Author

**Dipesh Gunjal**

Python Developer | Data Analytics Enthusiast

GitHub: [dipeshgunjal62940-svg](https://github.com/dipeshgunjal62940-svg)
