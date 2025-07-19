from tkinter import *
from tkinter import messagebox, simpledialog
import json
import os


tasks = []
JSON_FILE = "todos.json"

def load_tasks():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            try:
                data = json.load(f)
                tasks.extend(data)
                update_task_list()
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Failed to load tasks (invalid JSON format).")


def save_tasks():
    try:
        with open(JSON_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")


def update_task_list():
    listbox_tasks.delete(0, END)
    for i, task in enumerate(tasks, 1):
        listbox_tasks.insert(END, f"{i}. {task}")


def add_task():
    task = entry_task.get().strip()
    if not task:
        messagebox.showwarning("Input Error", "Please enter a task.")
        return
    tasks.append(task)
    entry_task.delete(0, END)
    update_task_list()
    save_tasks()

def edit_task():
    selected = listbox_tasks.curselection()
    if not selected:
        messagebox.showinfo("Selection Error", "Please select a task to edit.")
        return
    index = selected[0]
    current_task = tasks[index]
    new_task = simpledialog.askstring("Edit Task", "Update the task:", initialvalue=current_task)
    if new_task:
        tasks[index] = new_task.strip()
        update_task_list()
        save_tasks()

def delete_task():
    selected = listbox_tasks.curselection()
    if not selected:
        messagebox.showinfo("Selection Error", "Please select a task to delete.")
        return
    index = selected[0]
    confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete:\n{tasks[index]}?")
    if confirm:
        tasks.pop(index)
        update_task_list()
        save_tasks()

root = Tk()
root.title("To-Do List App")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="#f0f8ff")  

Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#333").pack(pady=10)

frame = Frame(root, bg="#f0f8ff")
frame.pack(pady=5)

entry_task = Entry(frame, font=("Arial", 12), width=30)
entry_task.grid(row=0, column=0, padx=10)

Button(frame, text="Add Task", command=add_task, bg="#b2dfdb", font=("Arial", 11)).grid(row=0, column=1)

listbox_tasks = Listbox(root, width=50, height=15, font=("Arial", 11))
listbox_tasks.pack(pady=15)

Button(root, text="Edit Task", command=edit_task, bg="#fff9c4", font=("Arial", 11)).pack(pady=5)
Button(root, text="Delete Task", command=delete_task, bg="#ffcdd2", font=("Arial", 11)).pack(pady=5)

Label(root, text="Double-click a task to edit", font=("Arial", 9), bg="#f0f8ff", fg="#555").pack(pady=5)

def on_double_click(event):
    edit_task()

listbox_tasks.bind("<Double-1>", on_double_click)

load_tasks()
root.mainloop()
