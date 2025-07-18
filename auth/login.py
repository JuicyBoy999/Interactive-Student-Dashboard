from tkinter import *
from tkinter import messagebox
import sqlite3

def login():
    sid = student_id_entry.get()
    pw = password_entry.get()

    if sid == '' or pw == '':
        messagebox.showerror("Error", "Please fill all the fields.")
        return

    conn = sqlite3.connect('auth/user_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE student_id = ? AND password = ?", (sid, pw))
    result = c.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()

        from dashboard import greeting
        greeting.show_greeting(result[0])
    else:
        messagebox.showerror("Login Failed", "Student ID or Password is incorrect.\nPlease try again or register first.")

def go_to_register():
    root.destroy()
    from auth import register
    register.main()

def main():
    global root, student_id_entry, password_entry

    root = Tk()
    root.title("Student Dashboard Login")
    root.geometry("400x400")
    root.config(bg="#f0f4f7")
    root.resizable(False, False)

    frame = Frame(root, bg="white", bd=2, relief=SOLID, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    title = Label(frame, text="Welcome Back!", font=("Helvetica", 18, "bold"), bg="white", fg="#333")
    title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    student_id_label = Label(frame, text="Student ID:", font=("Helvetica", 12), bg="white")
    student_id_label.grid(row=1, column=0, sticky=W, pady=5)
    student_id_entry = Entry(frame, font=("Helvetica", 12), width=25)
    student_id_entry.grid(row=1, column=1, pady=5)

    password_label = Label(frame, text="Password:", font=("Helvetica", 12), bg="white")
    password_label.grid(row=2, column=0, sticky=W, pady=5)
    password_entry = Entry(frame, font=("Helvetica", 12), show="*", width=25)
    password_entry.grid(row=2, column=1, pady=5)

    login_button = Button(frame, text="Login", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=20, command=login)
    login_button.grid(row=3, column=0, columnspan=2, pady=20)

    register_label = Label(frame, text="Don't have an account?", font=("Helvetica", 10), bg="white")
    register_label.grid(row=4, column=0, columnspan=2)
    register_button = Button(frame, text="Register", font=("Helvetica", 10, "underline"), fg="#0066cc", bg="white", bd=0, cursor="hand2", command=go_to_register)
    register_button.grid(row=5, column=0, columnspan=2)

    root.mainloop()