import re
import tkinter as tk
from tkinter import messagebox

MAIL = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

def is_valid(input_mail):
    return re.match(MAIL, input_mail) is not None

def check_validity():
    email = entry.get().strip()
    if is_valid(email):
        messagebox.showinfo("Result", f"'{email}' is a valid mail address")
    else:
        messagebox.showerror("Result", f"'{email}' is an invalid mail address")

# Create the main window
root = tk.Tk()
root.title("Email ID Checker")

# Set window size and position
window_width = 400
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a label
label = tk.Label(root, text="Enter an email address to validate:")
label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create a "Check" button
check_button = tk.Button(root, text="Check", command=check_validity)
check_button.pack(pady=10)

# Run the application
root.mainloop()
