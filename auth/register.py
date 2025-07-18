from tkinter import *
from tkinter import messagebox
import sqlite3

def register():
    name = full_name_entry.get()
    sid = student_id_entry.get()
    pw = password_entry.get()
    cpw = confirm_password_entry.get()

    if name == '' or sid == '' or pw == '' or cpw == '':
        messagebox.showerror("Error", "Please fill all the fields")
    elif pw != cpw:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        try:
            conn = sqlite3.connect('auth/user_data.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS users (
                full_name TEXT,
                student_id TEXT PRIMARY KEY,
                password TEXT
            )''')
            c.execute('INSERT INTO users (full_name, student_id, password) VALUES (?, ?, ?)', (name, sid, pw))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration Successful")
            root.destroy()
            from auth import login
            login.main()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Student ID already exists")

def go_back():
    root.destroy()
    from auth import login
    login.main()

def main():
    global root, full_name_entry, student_id_entry, password_entry, confirm_password_entry

    root = Tk()
    root.title("Student Registration")
    root.geometry("450x500")
    root.config(bg="#f0f4f7")
    root.resizable(False, False)

    frame = Frame(root, bg="white", bd=2, relief=SOLID, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    title = Label(frame, text="Register Account", font=("Helvetica", 18, "bold"), bg="white", fg="#333")
    title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    full_name_label = Label(frame, text="Full Name:", font=("Helvetica", 12), bg="white")
    full_name_label.grid(row=1, column=0, sticky=W, pady=5)
    full_name_entry = Entry(frame, font=("Helvetica", 12), width=25)
    full_name_entry.grid(row=1, column=1, pady=5)

    student_id_label = Label(frame, text="Student ID:", font=("Helvetica", 12), bg="white")
    student_id_label.grid(row=2, column=0, sticky=W, pady=5)
    student_id_entry = Entry(frame, font=("Helvetica", 12), width=25)
    student_id_entry.grid(row=2, column=1, pady=5)

    password_label = Label(frame, text="Password:", font=("Helvetica", 12), bg="white")
    password_label.grid(row=3, column=0, sticky=W, pady=5)
    password_entry = Entry(frame, font=("Helvetica", 12), show="*", width=25)
    password_entry.grid(row=3, column=1, pady=5)

    confirm_password_label = Label(frame, text="Confirm Password:", font=("Helvetica", 12), bg="white")
    confirm_password_label.grid(row=4, column=0, sticky=W, pady=5)
    confirm_password_entry = Entry(frame, font=("Helvetica", 12), show="*", width=25)
    confirm_password_entry.grid(row=4, column=1, pady=5)

    register_button = Button(frame, text="Register", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=20, command=register)
    register_button.grid(row=5, column=0, columnspan=2, pady=20)

    back_button = Button(frame, text="← Back to Login", font=("Helvetica", 10), bg="white", fg="#0066cc", bd=0, cursor="hand2", command=go_back)
    back_button.grid(row=6, column=0, columnspan=2)

    root.mainloop()
