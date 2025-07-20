from tkinter import *
from tkinter import messagebox, simpledialog
import json
import os

tasks = []
JSON_FILE = "data/todos.json"

def load_tasks():
    tasks.clear()
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            try:
                data = json.load(f)
                tasks.extend(data)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Failed to load tasks (invalid JSON format).")

def save_tasks():
    try:
        with open(JSON_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")

def update_task_list(listbox):
    listbox.delete(0, END)
    for i, task in enumerate(tasks, 1):
        listbox.insert(END, f"{i}. {task}")

def add_task(entry, listbox):
    task = entry.get().strip()
    if not task:
        messagebox.showwarning("Input Error", "Please enter a task.")
        return
    tasks.append(task)
    entry.delete(0, END)
    update_task_list(listbox)
    save_tasks()

def edit_task(listbox):
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Selection Error", "Please select a task to edit.")
        return
    index = selected[0]
    current_task = tasks[index]
    new_task = simpledialog.askstring("Edit Task", "Update the task:", initialvalue=current_task)
    if new_task:
        tasks[index] = new_task.strip()
        update_task_list(listbox)
        save_tasks()

def delete_task(listbox):
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Selection Error", "Please select a task to delete.")
        return
    index = selected[0]
    confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete:\n{tasks[index]}?")
    if confirm:
        tasks.pop(index)
        update_task_list(listbox)
        save_tasks()

def open_todo():
    window = Toplevel()
    window.title("Interactive Student Dashboard - To-Do List")
    window.geometry("500x550")
    window.configure(bg="#f5f5f5")
    window.resizable(False, False)

    Label(window, text="📝 To-Do List", font=("Segoe UI", 20, "bold"), bg="#f5f5f5").pack(pady=15)

    frame = Frame(window, bg="#f5f5f5")
    frame.pack(pady=10)

    entry_task = Entry(frame, font=("Segoe UI", 12), width=30)
    entry_task.grid(row=0, column=0, padx=10)

    add_btn = Button(frame, text="➕ Add Task", command=lambda: add_task(entry_task, listbox_tasks), bg="#64b5f6", fg="white", font=("Segoe UI", 10, "bold"))
    add_btn.grid(row=0, column=1)

    listbox_tasks = Listbox(window, width=50, height=15, font=("Segoe UI", 11), selectbackground="#90caf9")
    listbox_tasks.pack(pady=15)

    btn_edit = Button(window, text="✏ Edit Task", command=lambda: edit_task(listbox_tasks), bg="#fff59d", font=("Segoe UI", 10))
    btn_edit.pack(pady=5)

    btn_delete = Button(window, text="🗑 Delete Task", command=lambda: delete_task(listbox_tasks), bg="#ef9a9a", font=("Segoe UI", 10))
    btn_delete.pack(pady=5)

    Label(window, text="Double-click a task to edit", font=("Segoe UI", 9), bg="#e3f2fd", fg="#555").pack(pady=5)

    def on_double_click(event):
        edit_task(listbox_tasks)

    listbox_tasks.bind("<Double-1>", on_double_click)

    load_tasks()
    update_task_list(listbox_tasks)