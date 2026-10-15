 # BMI Calculator

A Python-based Body Mass Index (BMI) Calculator that helps users calculate their BMI using their weight and height. The project includes a Command-Line Interface (CLI) and a Graphical User Interface (GUI).

## Features

- Calculate BMI using weight and height.
- Display the calculated BMI value.
- Show a BMI category based on the application's classification logic.
- Command-Line Interface for text-based interaction.
- Graphical User Interface built with Tkinter.
- Input validation and error handling.
- Save BMI records locally using SQLite, if database functionality is enabled in the application.

## Technologies Used

- Python
- Tkinter for the graphical interface
- SQLite3 for local database storage
- Python standard library

## Project Structure

```text
BMI-Calculator/
├── bmi_cli.py
├── bmi_gui.py
├── README.md
└── requirements.txt
```

The SQLite database file may be created automatically when the application runs.

## Requirements

- Python 3.13 or another compatible Python 3 version.
- Tkinter for the GUI.
- SQLite3, included with standard Python installations.

No third-party Python packages are required for the standard implementation.

## Installation

1. Download or clone the repository.
2. Open a terminal in the `BMI-Calculator` directory.
3. Make sure Python is installed.

Check your Python installation:

```bash
python --version
```

## How to Run

### CLI Version

Run the following command:

```bash
python bmi_cli.py
```

Follow the prompts to enter your weight and height.

### GUI Version

Run the following command:

```bash
python bmi_gui.py
```

Enter the required details in the application window and use the available controls to calculate BMI.

## BMI Formula

BMI is calculated using the following formula when weight is in kilograms and height is in metres:

**BMI = Weight (kg) / Height (m)²**

For example, if weight is 60 kg and height is 1.70 m:

BMI = 60 / (1.70 × 1.70) ≈ 20.76

BMI categories and validation rules depend on the application's implementation.

## Database

If database functionality is enabled, the GUI stores BMI records in a local SQLite database. The application can use the database to retain entered details and calculated results.

The local database should not be committed if it contains personal information.

## Error Handling

The application should validate inputs and handle cases such as:

- Empty fields.
- Non-numeric values.
- Zero or negative weight.
- Zero or negative height.

## Future Improvements

- Add BMI history and record management.
- Improve the GUI design.
- Add charts to visualize BMI history.
- Export records to CSV.

## Author

**Dipesh Gunjal**

Python Programming — OIBSIP Internship Project: BMI Calculator