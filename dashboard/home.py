from tkinter import *
from tkinter import messagebox

def open_home(name):
    def open_todo():
        todo_window = Toplevel(root)
        todo_window.title("To-Do List")
        todo_window.geometry("400x300")
        todo_window.configure(bg="#f5f5f5")
        Label(todo_window, text="📝 To-Do List Module (Coming Soon)", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=50)

    def open_events():
        events_window = Toplevel(root)
        events_window.title("Events & Reminders")
        events_window.geometry("400x300")
        events_window.configure(bg="#f5f5f5")
        Label(events_window, text="📅 Events & Reminders Module (Coming Soon)", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=50)

    def open_schedule():
        schedule_window = Toplevel(root)
        schedule_window.title("Class Schedule")
        schedule_window.geometry("400x300")
        schedule_window.configure(bg="#f5f5f5")
        Label(schedule_window, text="📚 Schedule Module (Coming Soon)", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=50)

    def open_gpa():
        gpa_window = Toplevel(root)
        gpa_window.title("GPA Calculator")
        gpa_window.geometry("400x300")
        gpa_window.configure(bg="#f5f5f5")
        Label(gpa_window, text="📊 GPA Calculator Module (Coming Soon)", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=50)

    root = Tk()
    root.title("Student Dashboard - Home")
    root.geometry("600x500")
    root.configure(bg="#f5f5f5")

    # Header
    Label(root, text="🏠 Student Dashboard", font=("Helvetica", 22, "bold"), bg="#f5f5f5", fg="#333").pack(pady=30)

    if name:
        Label(root, text=f"Logged in as: {name}", font=("Helvetica", 12), bg="#f5f5f5", fg="#555").pack(pady=5)

    Label(root, text="Choose a module below:", font=("Helvetica", 14), bg="#f5f5f5", fg="#444").pack(pady=15)

    # Buttons Frame
    button_frame = Frame(root, bg="#f5f5f5")
    button_frame.pack(pady=10)

    btn_style = {
        "font": ("Helvetica", 12),
        "bg": "#4CAF50",
        "fg": "white",
        "activebackground": "#45a049",
        "activeforeground": "white",
        "width": 20,
        "bd": 0,
        "highlightthickness": 0,
        "relief": "flat",
        "padx": 5,
        "pady": 10
    }

    Button(button_frame, text="📝 To-Do List", command=open_todo, **btn_style).grid(row=0, column=0, padx=10, pady=10)
    Button(button_frame, text="📅 Events", command=open_events, **btn_style).grid(row=0, column=1, padx=10, pady=10)
    Button(button_frame, text="📚 Class Schedule", command=open_schedule, **btn_style).grid(row=1, column=0, padx=10, pady=10)
    Button(button_frame, text="📊 GPA Calculator", command=open_gpa, **btn_style).grid(row=1, column=1, padx=10, pady=10)

    # Footer
    Label(root, text="Build your academic life one step at a time ✨", font=("Helvetica", 10), bg="#f5f5f5", fg="#777").pack(side=BOTTOM, pady=20)

    root.mainloop()
