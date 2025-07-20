from tkinter import *
from tkinter import messagebox

def calculate_gpa():
    try:
        total_credits = 0
        total_grade_points = 0

        for i in range(len(subject_entries)):
            grade = grade_entries[i].get().strip().upper()
            credit_text = credit_entries[i].get().strip()

            if not grade and not credit_text:
                continue 

            if grade not in grade_point_map:
                messagebox.showerror("Invalid Grade", f"'{grade}' is not a valid grade.")
                return

            credit = float(credit_text)
            total_credits += credit
            total_grade_points += grade_point_map[grade] * credit

        if total_credits == 0:
            messagebox.showerror("No Data", "Please enter at least one subject with valid grade and credit.")
            return

        gpa = total_grade_points / total_credits
        gpa_var.set(f"{gpa:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for credits.")


def open_gpa():
    global subject_entries, grade_entries, credit_entries, grade_point_map, gpa_var

    grade_point_map = {
        "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "F": 0.0
    }

    gpa_window = Toplevel()
    gpa_window.title("Interactive Student Dashboard - GPA Calculator")
    gpa_window.geometry("600x500")
    gpa_window.config(bg="#f5f5f5")
    gpa_window.resizable(False, False)

    Label(gpa_window, text="📊 GPA Calculator", font=("Segoe UI", 18, "bold"), bg="#f5f5f5").pack(pady=10)

    frame = Frame(gpa_window, bg="#f5f5f5")
    frame.pack(pady=10)

    Label(frame, text="Subject", font=("Segoe UI", 11, "bold"), bg="#f5f5f5").grid(row=0, column=0, padx=15)
    Label(frame, text="Grade", font=("Segoe UI", 11, "bold"), bg="#f5f5f5").grid(row=0, column=1, padx=15)
    Label(frame, text="Credit", font=("Segoe UI", 11, "bold"), bg="#f5f5f5").grid(row=0, column=2, padx=15)

    subject_entries = []
    grade_entries = []
    credit_entries = []

    for i in range(6):
        subject = Entry(frame, font=("Segoe UI", 10), width=15)
        grade = Entry(frame, font=("Segoe UI", 10), width=10)
        credit = Entry(frame, font=("Segoe UI", 10), width=10)

        subject.grid(row=i+1, column=0, padx=10, pady=5)
        grade.grid(row=i+1, column=1, padx=10, pady=5)
        credit.grid(row=i+1, column=2, padx=10, pady=5)

        subject_entries.append(subject)
        grade_entries.append(grade)
        credit_entries.append(credit)

    Button(gpa_window, text="Calculate GPA", command=calculate_gpa, bg="#aed9e0", font=("Segoe UI", 10, "bold"), relief="flat", padx=15, pady=5).pack(pady=20)

    gpa_var = StringVar()
    gpa_var.set("0.00")
    Label(gpa_window, text="Your GPA:", font=("Segoe UI", 12, "bold"), bg="#f0f4f8").pack()
    Label(gpa_window, textvariable=gpa_var, font=("Segoe UI", 14), bg="#f0f4f8", fg="#0077b6").pack()