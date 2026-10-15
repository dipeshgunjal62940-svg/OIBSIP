# Secure Password Generator

A Python-based password generator with both a Command-Line Interface (CLI) and a Graphical User Interface (GUI). It generates random passwords using Python's built-in `secrets` module.

## Features

- Generate passwords from 4 to 128 characters.
- Choose uppercase letters, lowercase letters, digits, and symbols.
- Include at least one character from each selected character type.
- Exclude confusing characters such as `0`, `O`, `l`, `1`, and `I`.
- Generate passwords through the CLI or GUI.
- Copy passwords to the clipboard using the GUI.
- Show or hide the generated password.
- Basic password strength indicator in the GUI.
- Validate password length and character selections.
- Automated tests for password generation and validation.

## Technologies Used

- Python
- Tkinter for the GUI
- `secrets` for secure random selection
- `string` for character sets
- `unittest` for automated testing

## Project Structure

```text
Password-Generator/
├── .gitignore
├── password_generator.py
├── password_generator_gui.py
├── test_password_generator.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8 or newer recommended.
- Tkinter, usually included with standard Windows Python installations.
- No third-party Python packages are required.

## How to Run

Open a terminal in the `Password-Generator` directory.

### CLI Version

```bash
python password_generator.py
```

Follow the prompts to choose the password length, character types, and whether to exclude look-alike characters.

### GUI Version

```bash
python password_generator_gui.py
```

Choose the password length and character types, then click **Generate Password**. Use the available controls to copy or show/hide the generated password.

## Run Automated Tests

```bash
python -m unittest -v test_password_generator.py
```

The tests verify password generation, length validation, character selection, and other supported rules.

## Security Notes

- Password generation uses Python's `secrets` module.
- Do not share generated passwords or commit real passwords to GitHub.
- The GUI's strength indicator is an estimate, not a formal security audit.

## Author

**Dipesh Gunjal**

Python Programming — Oasis Infobyte Internship, Task 3: Password Generator