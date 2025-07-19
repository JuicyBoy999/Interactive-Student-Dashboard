import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

JSON_FILE = "GPA_DATA.json"

GRADE_POINTS = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}

class GPACalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bachelor's GPA Calculator")
        self.root.geometry("700x450")
        self.root.minsize(650, 400)
        self.root.configure(bg="#2c3e50")  

        self.courses = []
        self.setup_gui()
        self.load_courses()

    def setup_gui(self):
        label_font = ("Segoe UI", 11, "bold")
        entry_font = ("Segoe UI", 11)
        button_font = ("Segoe UI", 10, "bold")

        
        tk.Label(self.root, text="Course Name:", bg="#2c3e50", fg="white", font=label_font).grid(row=0, column=0, padx=15, pady=12, sticky="e")
        tk.Label(self.root, text="Credits:", bg="#2c3e50", fg="white", font=label_font).grid(row=1, column=0, padx=15, pady=12, sticky="e")
        tk.Label(self.root, text="Grade (e.g., A, B+, C-):", bg="#2c3e50", fg="white", font=label_font).grid(row=2, column=0, padx=15, pady=12, sticky="e")

        
        self.course_name_entry = tk.Entry(self.root, width=40, font=entry_font)
        self.course_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.credits_entry = tk.Entry(self.root, width=15, font=entry_font)
        self.credits_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.grade_entry = tk.Entry(self.root, width=15, font=entry_font)
        self.grade_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        
        self.add_button = tk.Button(self.root, text="Add Course", command=self.add_course,
                                    bg="#27ae60", fg="white", font=button_font, activebackground="#2ecc71",
                                    relief="flat", padx=10, pady=5, cursor="hand2")
        self.add_button.grid(row=3, column=0, padx=15, pady=15, sticky="e")

        self.modify_button = tk.Button(self.root, text="Modify Selected", command=self.modify_course,
                                       bg="#2980b9", fg="white", font=button_font, activebackground="#3498db",
                                       relief="flat", padx=10, pady=5, cursor="hand2")
        self.modify_button.grid(row=3, column=1, padx=(10,80), pady=15, sticky="w")

        self.delete_button = tk.Button(self.root, text="Delete Selected", command=self.delete_course,
                                       bg="#c0392b", fg="white", font=button_font, activebackground="#e74c3c",
                                       relief="flat", padx=10, pady=5, cursor="hand2")
        self.delete_button.grid(row=3, column=1, padx=(180,10), pady=15, sticky="w")

        
        self.course_listbox = tk.Listbox(self.root, width=80, height=12, font=("Consolas", 11),
                                         bg="#34495e", fg="white", selectbackground="#16a085", selectforeground="white",
                                         relief="flat", activestyle="none", borderwidth=0)
        self.course_listbox.grid(row=4, column=0, columnspan=2, padx=15, pady=10, sticky="nsew")

        
        scrollbar = tk.Scrollbar(self.root, orient="vertical", bg="#34495e", troughcolor="#2c3e50", borderwidth=0)
        scrollbar.config(command=self.course_listbox.yview)
        scrollbar.grid(row=4, column=2, sticky="ns", pady=10, padx=(0,15))
        self.course_listbox.config(yscrollcommand=scrollbar.set)

        
        self.gpa_label = tk.Label(self.root, text="Overall GPA: N/A", font=("Segoe UI", 16, "bold"),
                                  bg="#2c3e50", fg="#f39c12")
        self.gpa_label.grid(row=5, column=0, columnspan=3, pady=20)

        
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        
        self.course_name_entry.focus_set()


    def add_course(self):
        name = self.course_name_entry.get().strip()
        credits = self.credits_entry.get().strip()
        grade = self.grade_entry.get().strip().upper()

        if not name:
            messagebox.showerror("Input Error", "Course name cannot be empty.")
            return
        try:
            credits = float(credits)
            if credits <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Credits must be a positive number.")
            return
        if grade not in GRADE_POINTS:
            messagebox.showerror("Input Error", f"Grade must be one of: {', '.join(GRADE_POINTS.keys())}")
            return

        grade_point = GRADE_POINTS[grade]

        course = {
            "name": name,
            "credits": credits,
            "grade": grade,
            "grade_point": grade_point,
            "course_gpa": grade_point
        }
        self.courses.append(course)

        self.update_course_list()
        self.calculate_and_display_gpa()
        self.save_courses()

        self.course_name_entry.delete(0, tk.END)
        self.credits_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self.course_name_entry.focus_set()

    def update_course_list(self):
        self.course_listbox.delete(0, tk.END)
        for idx, course in enumerate(self.courses, start=1):
            name = course.get('name', 'N/A')
            credits = course.get('credits', 'N/A')
            grade = course.get('grade', 'N/A')
            grade_point = course.get('grade_point', 'N/A')
            display_text = f"{idx}. {name} - Credits: {credits}, Grade: {grade}, Grade Point: {grade_point}"
            self.course_listbox.insert(tk.END, display_text)

    def calculate_and_display_gpa(self):
        if not self.courses:
            self.gpa_label.config(text="Overall GPA: N/A")
            return

        total_weighted_points = 0
        total_credits = 0
        for course in self.courses:
            try:
                total_weighted_points += course['grade_point'] * course['credits']
                total_credits += course['credits']
            except KeyError:
                continue

        overall_gpa = total_weighted_points / total_credits if total_credits else 0
        self.gpa_label.config(text=f"Overall GPA: {overall_gpa:.2f}")

    def delete_course(self):
        selected_index = self.course_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "No course selected to delete.")
            return
        index = selected_index[0]
        del self.courses[index]
        self.update_course_list()
        self.calculate_and_display_gpa()
        self.save_courses()

    def modify_course(self):
        selected_index = self.course_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "No course selected to modify.")
            return
        index = selected_index[0]
        course = self.courses[index]

        new_name = simpledialog.askstring("Modify Course", "Course Name:", initialvalue=course.get('name', ''), parent=self.root)
        if new_name is None:
            return
        new_name = new_name.strip()
        if not new_name:
            messagebox.showerror("Input Error", "Course name cannot be empty.")
            return

        new_credits = simpledialog.askstring("Modify Course", "Credits:", initialvalue=str(course.get('credits', '')), parent=self.root)
        if new_credits is None:
            return
        try:
            new_credits = float(new_credits)
            if new_credits <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Credits must be a positive number.")
            return

        new_grade = simpledialog.askstring("Modify Course", f"Grade (one of {', '.join(GRADE_POINTS.keys())}):",
                                           initialvalue=course.get('grade', ''), parent=self.root)
        if new_grade is None:
            return
        new_grade = new_grade.strip().upper()
        if new_grade not in GRADE_POINTS:
            messagebox.showerror("Input Error", f"Grade must be one of: {', '.join(GRADE_POINTS.keys())}")
            return

        course['name'] = new_name
        course['credits'] = new_credits
        course['grade'] = new_grade
        course['grade_point'] = GRADE_POINTS[new_grade]
        course['course_gpa'] = GRADE_POINTS[new_grade]

        self.update_course_list()
        self.calculate_and_display_gpa()
        self.save_courses()

    def load_courses(self):
        if not os.path.exists(JSON_FILE):
            self.courses = []
            return

        try:
            with open(JSON_FILE, "r") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError("Data is not a list")
                valid_courses = []
                for course in data:
                    if (isinstance(course, dict) and
                        'name' in course and isinstance(course['name'], str) and course['name'].strip() != '' and
                        'credits' in course and isinstance(course['credits'], (int, float)) and course['credits'] > 0 and
                        'grade' in course and course['grade'] in GRADE_POINTS and
                        'grade_point' in course and isinstance(course['grade_point'], (int, float))):
                        valid_courses.append(course)
                self.courses = valid_courses
                self.update_course_list()
                self.calculate_and_display_gpa()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load courses: {e}")
            self.courses = []

    def save_courses(self):
        try:
            with open(JSON_FILE, "w") as f:
                json.dump(self.courses, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save courses: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GPACalculatorApp(root)
    root.mainloop()
