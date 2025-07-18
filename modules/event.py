import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Student Event Manager Dashboard")
root.geometry("600x500")
root.config(bg="white")

# List to store events
event_list = []

# Heading
tk.Label(root, text="Event Manager", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

# Event form frame
form_frame = tk.Frame(root, bg="white")
form_frame.pack(pady=5)

# Title
tk.Label(form_frame, text="Event Title:", bg="white").grid(row=0, column=0, sticky="e")
title_entry = tk.Entry(form_frame, width=30)
title_entry.grid(row=0, column=1, padx=10, pady=5)

# Date
tk.Label(form_frame, text="Date (YYYY-MM-DD):", bg="white").grid(row=1, column=0, sticky="e")
date_entry = tk.Entry(form_frame, width=30)
date_entry.grid(row=1, column=1, padx=10, pady=5)

# Time
tk.Label(form_frame, text="Time (HH:MM):", bg="white").grid(row=2, column=0, sticky="e")
time_entry = tk.Entry(form_frame, width=30)
time_entry.grid(row=2, column=1, padx=10, pady=5)

# Description
tk.Label(form_frame, text="Description:", bg="white").grid(row=3, column=0, sticky="ne")
desc_entry = tk.Text(form_frame, width=30, height=4)
desc_entry.grid(row=3, column=1, padx=10, pady=5)

# Event Display Box
event_display = tk.Listbox(root, width=70, height=10)
event_display.pack(pady=10)

# Function to add event
def add_event():
    title = title_entry.get().strip()
    date = date_entry.get().strip()
    time = time_entry.get().strip()
    desc = desc_entry.get("1.0", tk.END).strip()

    if not title or not date or not time:
        messagebox.showwarning("Input Error", "Title, Date, and Time are required.")
        return

    event = f"{date} {time} - {title} | {desc}"
    event_list.append(event)
    event_display.insert(tk.END, event)
    clear_form()

# Function to clear input fields
def clear_form():
    title_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    desc_entry.delete("1.0", tk.END)

# Function to delete all events
def delete_all_events():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete all events?"):
        event_list.clear()
        event_display.delete(0, tk.END)

# Buttons
btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Event", command=add_event, bg="#c9f7c3", width=15).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear Form", command=clear_form, bg="#ffe599", width=15).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Delete All Events", command=delete_all_events, bg="#f4cccc", width=15).grid(row=0, column=2, padx=10)

# Run the app
root.mainloop()
 