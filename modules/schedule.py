import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Student Class Schedule Dashboard")
root.geometry("750x470")
root.config(bg="white")

# Days of the week (Sunday to Friday only)
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods = ["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"]

# Title label
tk.Label(root, text="Class Schedule", font=("Helvetica", 16, "bold"), bg="white").grid(row=0, column=0, columnspan=6, pady=10)

# Grid headers
tk.Label(root, text="Day / Period", bg="#d9ead3", width=15, font=("Helvetica", 10, "bold")).grid(row=1, column=0)
for j, period in enumerate(periods):
    tk.Label(root, text=period, bg="#d9ead3", width=15, font=("Helvetica", 10, "bold")).grid(row=1, column=j+1)

# Entry widgets storage
entries = {}

# Create input grid
for i, day in enumerate(days):
    tk.Label(root, text=day, bg="#fce5cd", width=15, font=("Helvetica", 10, "bold")).grid(row=i+2, column=0)
    for j in range(5):
        entry = tk.Entry(root, width=15, justify="center")
        entry.grid(row=i+2, column=j+1, padx=2, pady=2)
        entries[(day, j)] = entry

# Function to show schedule
def submit_schedule():
    schedule = ""
    for day in days:
        row_data = [entries[(day, j)].get() for j in range(5)]
        schedule += f"{day}: {', '.join(row_data)}\n"
    messagebox.showinfo("Schedule Submitted", f"Your schedule has been saved:\n\n{schedule}")

# Function to clear all entries
def clear_schedule():
    for entry in entries.values():
        entry.delete(0, tk.END)

# Buttons
tk.Button(root, text="Submit Schedule", command=submit_schedule, bg="#b6d7a8", font=("Helvetica", 10)).grid(row=9, column=1, pady=10)
tk.Button(root, text="Clear All", command=clear_schedule, bg="#f4cccc", font=("Helvetica", 10)).grid(row=9, column=3, pady=10)

# Run the app
root.mainloop()
