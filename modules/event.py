import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime, timedelta
import threading

EVENT_FILE = os.path.join("data", "events.json")
event_list = []

def load_events():
    if os.path.exists(EVENT_FILE):
        with open(EVENT_FILE, "r") as file:
            return json.load(file)
    return []

def save_events():
    with open(EVENT_FILE, "w") as file:
        json.dump(event_list, file, indent=4)

def check_reminders():
    while True:
        now = datetime.now()
        for event in event_list:
            event_time = datetime.strptime(event["date"] + " " + event["time"], "%Y-%m-%d %H:%M")
            if now >= event_time and not event.get("notified", False):
                messagebox.showinfo("Reminder", f"⏰ Reminder for: {event['title']}")
                event["notified"] = True
                save_events()
        threading.Event().wait(60)

def open_events():
    global title_entry, date_entry, time_entry, desc_entry, event_display
    global root

    root = tk.Tk()
    root.title("Interactive Student Dashboard - Event Manager")
    root.geometry("700x550")
    root.config(bg="#f5f5f5")

    tk.Label(root, text="📅 Event Manager", font=("Helvetica", 18, "bold"), bg="#f5f5f5").pack(pady=10)

    form_frame = tk.Frame(root, bg="#f5f5f5")
    form_frame.pack(pady=5)

    tk.Label(form_frame, text="Title:", bg="#f5f5f5").grid(row=0, column=0, sticky="e")
    title_entry = tk.Entry(form_frame, width=30)
    title_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Date (YYYY-MM-DD):", bg="#f5f5f5").grid(row=1, column=0, sticky="e")
    date_entry = tk.Entry(form_frame, width=30)
    date_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Time (HH:MM):", bg="#f5f5f5").grid(row=2, column=0, sticky="e")
    time_entry = tk.Entry(form_frame, width=30)
    time_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Description:", bg="#f5f5f5").grid(row=3, column=0, sticky="ne")
    desc_entry = tk.Text(form_frame, width=30, height=3)
    desc_entry.grid(row=3, column=1, padx=10, pady=5)

    event_display = tk.Listbox(root, width=80, height=12)
    event_display.pack(pady=10)

    btn_frame = tk.Frame(root, bg="#f5f5f5")
    btn_frame.pack()

    tk.Button(btn_frame, text="Add Event", command=add_event, bg="#c9f7c3", width=15).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Edit Selected", command=edit_event, bg="#fff2cc", width=15).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Delete Selected", command=delete_event, bg="#f4cccc", width=15).grid(row=0, column=2, padx=5)
    tk.Button(btn_frame, text="Clear Form", command=clear_form, bg="#d9d2e9", width=15).grid(row=0, column=3, padx=5)

    load_and_display_events()

    threading.Thread(target=check_reminders, daemon=True).start()

    root.mainloop()

def load_and_display_events():
    global event_list
    event_list = load_events()
    event_display.delete(0, tk.END)
    for event in event_list:
        display_text = f"{event['date']} {event['time']} - {event['title']} | {event['desc']}"
        event_display.insert(tk.END, display_text)

def add_event():
    title = title_entry.get().strip()
    date = date_entry.get().strip()
    time = time_entry.get().strip()
    desc = desc_entry.get("1.0", tk.END).strip()

    if not title or not date or not time:
        messagebox.showwarning("Input Error", "Title, Date, and Time are required.")
        return

    try:
        datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M")
    except ValueError:
        messagebox.showerror("Invalid Format", "Enter valid date and time.")
        return

    new_event = {
        "title": title,
        "date": date,
        "time": time,
        "desc": desc,
        "notified": False
    }

    event_list.append(new_event)
    save_events()
    load_and_display_events()
    clear_form()

def clear_form():
    title_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    desc_entry.delete("1.0", tk.END)

def edit_event():
    selected = event_display.curselection()
    if not selected:
        messagebox.showwarning("Select Event", "Please select an event to edit.")
        return

    index = selected[0]
    event = event_list[index]

    title_entry.delete(0, tk.END)
    title_entry.insert(0, event["title"])
    date_entry.delete(0, tk.END)
    date_entry.insert(0, event["date"])
    time_entry.delete(0, tk.END)
    time_entry.insert(0, event["time"])
    desc_entry.delete("1.0", tk.END)
    desc_entry.insert("1.0", event["desc"])

    del event_list[index]
    save_events()
    load_and_display_events()

def delete_event():
    selected = event_display.curselection()
    if not selected:
        messagebox.showwarning("Select Event", "Please select an event to delete.")
        return

    index = selected[0]
    if messagebox.askyesno("Confirm", "Delete selected event?"):
        del event_list[index]
        save_events()
        load_and_display_events()
