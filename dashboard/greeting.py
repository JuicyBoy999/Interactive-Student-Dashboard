from tkinter import *
from datetime import datetime

def greeting(name):
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return f"Good morning, {name}!\nHave a great day!"
    elif 12 <= hour < 16:
        return f"Good afternoon, {name}!\nHope you're doing well!"
    elif 16 <= hour < 20:
        return f"Good evening, {name}!\nWelcome to your student dashboard!"
    else:
        return f"Good night, {name}!\nTake some rest and sleep well!"

def show_greeting(name):

    def go_to_home():
        root.destroy()
        from dashboard.home import open_home
        open_home(name)

    global root
    root = Tk()
    root.title("Welcome")
    root.geometry("600x300")
    root.configure(bg="#e8f0fe") 
    root.resizable(False, False)

    frame = Frame(root, bg="white", bd=2, relief=SOLID, padx=30, pady=30)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    title = Label(frame, text="👋 Welcome!", font=("Helvetica", 20, "bold"), bg="white", fg="#333")
    title.pack(pady=(0, 10))

    message = greeting(name)
    message_label = Label(frame, text=message, font=("Helvetica", 14), bg="white", fg="#555", justify="center")
    message_label.pack()

    continue_btn = Button(frame, text="Continue", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", padx=20, pady=5, command = go_to_home)
    continue_btn.pack(pady=20)

    root.mainloop()