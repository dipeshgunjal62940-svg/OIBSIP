 
import sqlite3
import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

DB_NAME = "bmi_records.db"


# 1. Create database table
def create_table():
    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    weight REAL NOT NULL,
                    height REAL NOT NULL,
                    bmi REAL NOT NULL,
                    category TEXT NOT NULL,
                    date TEXT NOT NULL
                )
            """)
        return True

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))
        return False


# 2. Save BMI record
def save_record(username, weight, height, bmi, category):
    try:
        record_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("""
                INSERT INTO records
                (username, weight, height, bmi, category, date)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                username, weight, height,
                bmi, category, record_date
            ))

        return True

    except sqlite3.Error as e:
        messagebox.showerror(
            "Database Error",
            f"Could not save record: {e}"
        )
        return False


# 3. Determine BMI category and color
def get_category(bmi):
    if bmi < 18.5:
        return "Underweight", "orange"
    elif bmi < 25:
        return "Normal", "green"
    elif bmi < 30:
        return "Overweight", "#CC8400"
    else:
        return "Obese", "red"


# 4. Calculate BMI
def calculate_bmi():
    name = name_entry.get().strip()

    if not name:
        messagebox.showerror(
            "Input Error", "Please enter your name."
        )
        return

    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Enter numeric weight and height."
        )
        return

    # Convert centimetres to metres if necessary
    if height > 3:
        height = height / 100

    if weight <= 0 or height <= 0:
        messagebox.showerror(
            "Input Error",
            "Weight and height must be greater than zero."
        )
        return

    bmi = round(weight / (height ** 2), 2)
    category, color = get_category(bmi)

    # Save before showing the successful result
    if not save_record(name, weight, height, bmi, category):
        return

    result_label.config(
        text=f"Hello {name}!\nBMI: {bmi}\nCategory: {category}",
        fg=color
    )

    # Refresh history after saving
    load_history(show_message=False)


# 5. Show selected user's history
def load_history(show_message=True):
    username = name_entry.get().strip()

    if not username:
        messagebox.showerror(
            "Input Error", "Please enter a name."
        )
        return

    # Clear existing rows
    for item in history_tree.get_children():
        history_tree.delete(item)

    try:
        with sqlite3.connect(DB_NAME) as conn:
            rows = conn.execute("""
                SELECT date, weight, height, bmi, category
                FROM records
                WHERE username = ? COLLATE NOCASE
                ORDER BY date DESC, id DESC
            """, (username,)).fetchall()

        for row in rows:
            history_tree.insert(
                "",
                tk.END,
                values=(
                    row[0],
                    f"{row[1]:.2f}",
                    f"{row[2]:.2f}",
                    f"{row[3]:.2f}",
                    row[4]
                )
            )

        if not rows and show_message:
            messagebox.showinfo(
                "History", "No records found for this user."
            )

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))


# 6. Display BMI trend chart
def show_trend():
    username = name_entry.get().strip()

    if not username:
        messagebox.showerror(
            "Input Error", "Please enter a name."
        )
        return

    try:
        with sqlite3.connect(DB_NAME) as conn:
            rows = conn.execute("""
                SELECT date, bmi
                FROM records
                WHERE username = ? COLLATE NOCASE
                ORDER BY date ASC, id ASC
            """, (username,)).fetchall()

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))
        return

    if len(rows) < 2:
        messagebox.showinfo(
            "BMI Trend",
            "At least 2 records are required to show the trend."
        )
        return

    dates = [row[0] for row in rows]
    bmi_values = [row[1] for row in rows]

    plt.figure(figsize=(9, 5))
    plt.plot(dates, bmi_values, marker="o")
    plt.title(f"BMI Trend for {username}")
    plt.xlabel("Date and Time")
    plt.ylabel("BMI")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# 7. Create main application window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("900x680")
root.minsize(800, 600)

title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=12)


# 8. Input fields
form_frame = tk.Frame(root)
form_frame.pack(pady=5)

tk.Label(form_frame, text="Name:").grid(
    row=0, column=0, padx=8, pady=6, sticky="w"
)
name_entry = tk.Entry(form_frame, width=25)
name_entry.grid(row=0, column=1, padx=8, pady=6)

tk.Label(form_frame, text="Weight (kg):").grid(
    row=1, column=0, padx=8, pady=6, sticky="w"
)
weight_entry = tk.Entry(form_frame, width=25)
weight_entry.grid(row=1, column=1, padx=8, pady=6)

tk.Label(form_frame, text="Height (meters or cm):").grid(
    row=2, column=0, padx=8, pady=6, sticky="w"
)
height_entry = tk.Entry(form_frame, width=25)
height_entry.grid(row=2, column=1, padx=8, pady=6)


# 9. Calculate button
tk.Button(
    form_frame,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="#2563EB",
    fg="white",
    font=("Arial", 11, "bold")
).grid(row=3, column=0, columnspan=2, pady=10)


# 10. Result label
result_label = tk.Label(
    root,
    text="Your result will appear here",
    font=("Arial", 14, "bold"),
    fg="black"
)
result_label.pack(pady=5)


# 11. History and trend buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=8)

tk.Button(
    button_frame,
    text="Show History",
    command=load_history
).pack(side="left", padx=8)

tk.Button(
    button_frame,
    text="Show Trend",
    command=show_trend
).pack(side="left", padx=8)


# 12. History table
history_frame = tk.Frame(root)
history_frame.pack(fill="both", expand=True, padx=15, pady=10)

columns = ("Date", "Weight (kg)", "Height (m)", "BMI", "Category")

history_tree = ttk.Treeview(
    history_frame,
    columns=columns,
    show="headings",
    height=10
)

for column in columns:
    history_tree.heading(column, text=column)
    history_tree.column(
        column, width=150, anchor="center"
    )

scrollbar = ttk.Scrollbar(
    history_frame,
    orient="vertical",
    command=history_tree.yview
)

history_tree.configure(yscrollcommand=scrollbar.set)
history_tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# 13. Initialize database and start application
create_table()
root.mainloop()