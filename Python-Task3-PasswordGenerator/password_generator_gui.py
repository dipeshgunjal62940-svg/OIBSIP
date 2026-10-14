
import tkinter as tk
from tkinter import ttk, messagebox

from password_generator import generate_password


# Password strength indicator
def calculate_strength(length, selected_types):
    if length >= 16 and selected_types >= 3:
        return "Strong", "#16803C"
    elif length >= 12 and selected_types >= 2:
        return "Medium", "#B77900"
    else:
        return "Weak", "#D93025"


# Generate password
def handle_generate():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please select a valid password length."
        )
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()
    exclude_lookalikes = exclude_var.get()

    if not any((use_upper, use_lower, use_digits, use_symbols)):
        messagebox.showerror(
            "Character Selection",
            "Please select at least one character type."
        )
        return

    selected_types = sum((
        use_upper,
        use_lower,
        use_digits,
        use_symbols
    ))

    try:
        password = generate_password(
            length,
            use_upper,
            use_lower,
            use_digits,
            use_symbols,
            exclude_lookalikes
        )
    except ValueError as error:
        messagebox.showerror("Password Error", str(error))
        return

    password_var.set(password)

    strength, color = calculate_strength(length, selected_types)
    strength_label.config(
        text=f"Password Strength: {strength}",
        foreground=color
    )

    copied_label.config(text="")


# Copy generated password
def copy_password():
    password = password_var.get()

    if not password:
        messagebox.showerror(
            "Copy Error",
            "Generate a password first."
        )
        return

    try:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update_idletasks()
        copied_label.config(
            text="Copied!",
            foreground="#16803C"
        )
    except tk.TclError:
        messagebox.showerror(
            "Clipboard Error",
            "Could not copy the password."
        )


# Show or hide password
def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# Main window
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("560x650")
root.resizable(False, False)
root.configure(bg="#F4F6FA")

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("TCheckbutton", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10))


# Header
header = tk.Frame(root, bg="#18243A", pady=22)
header.pack(fill="x")

tk.Label(
    header,
    text="SECURE PASSWORD GENERATOR",
    font=("Segoe UI", 18, "bold"),
    fg="white",
    bg="#18243A"
).pack()

tk.Label(
    header,
    text="Create a strong, random password",
    font=("Segoe UI", 10),
    fg="#D6E0F0",
    bg="#18243A"
).pack(pady=(5, 0))


# Main content
main_frame = tk.Frame(root, bg="#F4F6FA", padx=30, pady=18)
main_frame.pack(fill="both", expand=True)

# Length control
ttk.Label(
    main_frame,
    text="Password Length (4–128)"
).pack(anchor="w")

length_var = tk.IntVar(value=16)

length_spinbox = tk.Spinbox(
    main_frame,
    from_=4,
    to=128,
    textvariable=length_var,
    width=12,
    font=("Segoe UI", 11)
)
length_spinbox.pack(anchor="w", pady=(5, 15))


# Character options
ttk.Label(
    main_frame,
    text="Choose Character Types",
    font=("Segoe UI", 11, "bold")
).pack(anchor="w", pady=(0, 5))

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

ttk.Checkbutton(
    main_frame,
    text="Uppercase letters (A–Z)",
    variable=upper_var
).pack(anchor="w", pady=2)

ttk.Checkbutton(
    main_frame,
    text="Lowercase letters (a–z)",
    variable=lower_var
).pack(anchor="w", pady=2)

ttk.Checkbutton(
    main_frame,
    text="Digits (0–9)",
    variable=digits_var
).pack(anchor="w", pady=2)

ttk.Checkbutton(
    main_frame,
    text="Symbols (!@#$...)",
    variable=symbols_var
).pack(anchor="w", pady=2)


# Bonus: exclude look-alike characters
exclude_var = tk.BooleanVar(value=False)

ttk.Checkbutton(
    main_frame,
    text="Exclude look-alike characters (0, O, l, 1, I)",
    variable=exclude_var
).pack(anchor="w", pady=(8, 15))


# Generate button
ttk.Button(
    main_frame,
    text="Generate Password",
    command=handle_generate
).pack(fill="x", pady=(0, 12))


# Read-only password field
ttk.Label(
    main_frame,
    text="Generated Password",
    font=("Segoe UI", 10, "bold")
).pack(anchor="w")

password_var = tk.StringVar()

password_entry = tk.Entry(
    main_frame,
    textvariable=password_var,
    font=("Consolas", 12),
    state="readonly",
    show="*",
    readonlybackground="white",
    relief="solid",
    bd=1
)
password_entry.pack(fill="x", pady=6, ipady=7)


# Show/Hide toggle
show_var = tk.BooleanVar(value=False)

ttk.Checkbutton(
    main_frame,
    text="Show password",
    variable=show_var,
    command=toggle_password
).pack(anchor="w", pady=3)


# Copy button and copied message
ttk.Button(
    main_frame,
    text="Copy to Clipboard",
    command=copy_password
).pack(fill="x", pady=(8, 5))

copied_label = ttk.Label(
    main_frame,
    text="",
    anchor="center"
)
copied_label.pack()


# Strength indicator
strength_label = ttk.Label(
    main_frame,
    text="Password Strength: Not generated",
    font=("Segoe UI", 10, "bold")
)
strength_label.pack(pady=(8, 0))


# Start application
root.mainloop()
