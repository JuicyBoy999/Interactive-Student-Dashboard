from tkinter import *
from tkinter import messagebox
import sqlite3
import os

def open_account(logged_in_id):
    global root, new_pw_entry, confirm_pw_entry

    def change_password():
        new_pw = new_pw_entry.get()
        confirm_pw = confirm_pw_entry.get()

        if new_pw == '' or confirm_pw == '':
            messagebox.showerror("Error", "Please fill all the fields.")
            return
        if new_pw != confirm_pw:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        conn = sqlite3.connect('auth/user_data.db')
        c = conn.cursor()
        c.execute("UPDATE users SET password = ? WHERE student_id = ?", (new_pw, logged_in_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Password updated successfully.")
        new_pw_entry.delete(0, END)
        confirm_pw_entry.delete(0, END)

    def delete_user_json_files():
        json_files = ["schedule.json", "todos.json", "events.json"]
        data_dir = "data"

        for filename in json_files:
            file_path = os.path.join(data_dir, filename)
            if os.path.exists(file_path):
                os.remove(file_path)

    def logout():
        root.destroy()
        from auth import login
        login.main()

    def delete_account():
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete your account?")
        if not confirm:
            return

        conn = sqlite3.connect('auth/user_data.db')
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE student_id = ?", (logged_in_id,))
        conn.commit()
        conn.close()

        delete_user_json_files()

        messagebox.showinfo("Deleted", "Your account has been deleted.")
        logout()

    root = Tk()
    root.title("Account Settings")
    root.geometry("400x400")
    root.config(bg="#f5f5f5")
    root.resizable(False, False)

    frame = Frame(root, bg="white", bd=2, relief=SOLID, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    title = Label(frame, text="👤 Account Settings", font=("Helvetica", 16, "bold"), bg="white", fg="#333")
    title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    user_label = Label(frame, text=f"Logged in as: {logged_in_id}", font=("Helvetica", 10, "italic"), bg="white", fg="gray")
    user_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

    new_pw_label = Label(frame, text="New Password:", font=("Helvetica", 12), bg="white")
    new_pw_label.grid(row=2, column=0, sticky=W, pady=5)
    new_pw_entry = Entry(frame, font=("Helvetica", 12), show="*", width=25)
    new_pw_entry.grid(row=2, column=1, pady=5)

    confirm_pw_label = Label(frame, text="Confirm Password:", font=("Helvetica", 12), bg="white")
    confirm_pw_label.grid(row=3, column=0, sticky=W, pady=5)
    confirm_pw_entry = Entry(frame, font=("Helvetica", 12), show="*", width=25)
    confirm_pw_entry.grid(row=3, column=1, pady=5)

    change_pw_btn = Button(frame, text="Change Password", font=("Helvetica", 12), bg="#2196F3", fg="white", command=change_password)
    change_pw_btn.grid(row=4, column=0, columnspan=2, pady=(15, 5))

    logout_btn = Button(frame, text="Log Out", font=("Helvetica", 12), bg="#FFA726", fg="white", command=logout)
    logout_btn.grid(row=5, column=0, columnspan=2, pady=5)

    delete_btn = Button(frame, text="Delete Account", font=("Helvetica", 12), bg="#f44336", fg="white", command=delete_account)
    delete_btn.grid(row=6, column=0, columnspan=2, pady=(5, 0))

    root.mainloop()