import tkinter as tk
from tkinter import messagebox
import os
import json

DATA_FILE = os.path.join("data", "schedule.json")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods = ["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"]
entries = {}

def open_schedule():
    def submit_schedule():
        schedule = {}
        for day in days:
            schedule[day] = [entries[(day, i)].get() for i in range(len(periods))]
        
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(schedule, f, indent=4)
        
        messagebox.showinfo("Success", "Schedule saved successfully!")

    def load_schedule():
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                schedule = json.load(f)
                for day in days:
                    for i in range(len(periods)):
                        entries[(day, i)].delete(0, tk.END)
                        entries[(day, i)].insert(0, schedule.get(day, [""] * 5)[i])
            messagebox.showinfo("Loaded", "Schedule loaded from saved file.")
        else:
            messagebox.showinfo("No Schedule", "No saved schedule found.")

    def clear_schedule():
        for entry in entries.values():
            entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("Interactive Student Dashboard - Class Schedule")
    root.geometry("820x500")
    root.config(bg="#f5f5f5")

    tk.Label(root, text="📚 Weekly Class Schedule", font=("Helvetica", 18, "bold"), bg="#f5f5f5").grid(row=0, column=0, columnspan=6, pady=20)

    tk.Label(root, text="Day / Period", bg="#d9ead3", width=15, font=("Helvetica", 10, "bold"), relief="ridge").grid(row=1, column=0, padx=2, pady=2)
    for i, period in enumerate(periods):
        tk.Label(root, text=period, bg="#d9ead3", width=15, font=("Helvetica", 10, "bold"), relief="ridge").grid(row=1, column=i+1, padx=2, pady=2)

    for row, day in enumerate(days):
        tk.Label(root, text=day, bg="#fce5cd", width=15, font=("Helvetica", 10, "bold"), relief="ridge").grid(row=row+2, column=0, padx=2, pady=2)
        for col in range(len(periods)):
            entry = tk.Entry(root, width=18, justify="center", font=("Helvetica", 10))
            entry.grid(row=row+2, column=col+1, padx=1, pady=1)
            entries[(day, col)] = entry

    btn_frame = tk.Frame(root, bg="#f5f5f5")
    btn_frame.grid(row=len(days)+3, column=0, columnspan=6, pady=20)

    tk.Button(btn_frame, text="💾 Save", command=submit_schedule, bg="#b6d7a8", font=("Helvetica", 10), width=12).pack(side="left", padx=10)
    tk.Button(btn_frame, text="📤 Load", command=load_schedule, bg="#cfe2f3", font=("Helvetica", 10), width=12).pack(side="left", padx=10)
    tk.Button(btn_frame, text="🧹 Clear", command=clear_schedule, bg="#f4cccc", font=("Helvetica", 10), width=12).pack(side="left", padx=10)

    root.mainloop()