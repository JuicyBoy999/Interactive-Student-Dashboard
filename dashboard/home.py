from tkinter import *

def open_home(name):
    def open_todo():
        from modules import todo
        todo.open_todo()

    def open_events():
        from modules import event
        event.open_events()

    def open_schedule():
        from modules import schedule
        schedule.open_schedule()

    def open_gpa():
        from modules import GPA
        GPA.open_gpa()

    def open_account():
        from modules import account
        account.open_account()

    root = Tk()
    root.title("Interactive Student Dashboard - Home")
    root.geometry("600x500")
    root.configure(bg="#f5f5f5")

    Label(root, text="🏠 Interactive Student Dashboard", font=("Helvetica", 22, "bold"), bg="#f5f5f5", fg="#333").pack(pady=30)

    if name:
        Label(root, text=f"Logged in as: {name}", font=("Helvetica", 12), bg="#f5f5f5", fg="#555").pack(pady=5)

    Label(root, text="Choose a module below:", font=("Helvetica", 14), bg="#f5f5f5", fg="#444").pack(pady=15)

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
    Button(button_frame, text="👤 Account", command=open_account, **btn_style).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    Label(root, text="Build your academic life one step at a time ✨", font=("Helvetica", 10), bg="#f5f5f5", fg="#777").pack(side=BOTTOM, pady=20)

    root.mainloop()