import tkinter as tk
from tkinter import ttk, messagebox

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, name, age, gender, course, marks, hostel=False, transport=False):
        super().__init__(name, age, gender)
        self.course = course
        self.marks = marks  # out of 1100
        self.hostel = hostel
        self.transport = transport

class University:
    def __init__(self):
        self.fees = {
            "BS Computer Science": 60000,
            "BS Electrical Engineering": 60000,
            "BS Business": 60000,
            "BS Arts": 60000
        }
        self.duration = {
            "BS Computer Science": "4 years",
            "BS Electrical Engineering": "4 years",
            "BS Business": "4 years",
            "BS Arts": "4 years"
        }
        self.hostel_fee = 30000
        self.transport_fee = 15000

    def calculate_fee(self, student):
        base_fee = self.fees.get(student.course, 40000)

        # Convert marks out of 1100 to percentage
        percentage = (student.marks / 1100) * 100

        # Scholarship system
        if percentage >= 90:   # 90% or above
            scholarship = 0.5   # 50% discount
        else:
            scholarship = 0     # no scholarship

        fee_after_scholarship = base_fee - (base_fee * scholarship)

        # Add hostel fee if opted
        if student.hostel:
            fee_after_scholarship += self.hostel_fee

        # Add transport fee if opted
        if student.transport:
            fee_after_scholarship += self.transport_fee

        return fee_after_scholarship, scholarship, percentage

    def get_duration(self, course):
        return self.duration.get(course, "N/A")


# GUI 
class AdmissionFormGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 University Admission Form")
        self.root.geometry("650x720")
        self.root.config(bg="#e3f2fd")

        # Title
        title = tk.Label(root, text="✨ University Admission Form ✨",
                         font=("Times New Roman", 22, "bold"), bg="#1565c0", fg="white", pady=10)
        title.pack(fill="x")

        # Frame
        frame = tk.Frame(root, bg="#bbdefb", padx=20, pady=20, relief="ridge", bd=5)
        frame.pack(pady=15, padx=20, fill="both", expand=True)

        # Name
        tk.Label(frame, text="Full Name:", font=("Arial", 12, "bold"), bg="#bbdefb").grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(frame, font=("Arial", 12), width=25)
        self.name_entry.grid(row=0, column=1, pady=5)

        # Age
        tk.Label(frame, text="Age:", font=("Arial", 12, "bold"), bg="#bbdefb").grid(row=1, column=0, sticky="w", pady=5)
        self.age_entry = tk.Entry(frame, font=("Arial", 12), width=25)
        self.age_entry.grid(row=1, column=1, pady=5)

        # Gender
        tk.Label(frame, text="Gender:", font=("Arial", 12, "bold"), bg="#bbdefb").grid(row=2, column=0, sticky="w", pady=5)
        self.gender_var = tk.StringVar(value="Male")
        ttk.Combobox(frame, textvariable=self.gender_var, 
                     values=["Male", "Female"], state="readonly",
                     font=("Arial", 12), width=22).grid(row=2, column=1, pady=5)

        # Program
        tk.Label(frame, text="Program:", font=("Arial", 12, "bold"), bg="#bbdefb").grid(row=3, column=0, sticky="w", pady=5)
        self.program_var = tk.StringVar(value="BS Computer Science")
        ttk.Combobox(frame, textvariable=self.program_var,
                     values=["BS Computer Science", "BS Electrical Engineering", "BS Arts", "BS Business"],
                     state="readonly", font=("Arial", 12), width=22).grid(row=3, column=1, pady=5)

        # Hostel
        tk.Label(frame, text="Hostel Facility:", font=("Arial", 12, "bold"), bg="#bbdefb").grid(row=4, column=0, sticky="w", pady=5)
        self.hostel_var = tk.StringVar(value="No")
        ttk.Combobox(frame, textvariable=self.hostel_var,
                     values=["Yes", "No"], state="readonly",
                     font=("Arial", 12), width=22).grid(row=4, column=1, pady=5)

        # Transport
        tk.Label(frame, text="Transport Facility:", font=("Arial", 12, "bold"), bg="#bbdefb").grid(row=5, column=0, sticky="w", pady=5)
        self.transport_var = tk.StringVar(value="No")
        ttk.Combobox(frame, textvariable=self.transport_var,
                     values=["Yes", "No"], state="readonly",
                     font=("Arial", 12), width=22).grid(row=5, column=1, pady=5)

        # Marks
        tk.Label(frame, text="Marks (out of 1100):", font=("Arial", 12, "bold"), bg="#bbdefb").grid(row=6, column=0, sticky="w", pady=5)
        self.marks_entry = tk.Entry(frame, font=("Arial", 12), width=25)
        self.marks_entry.grid(row=6, column=1, pady=5)

        # Submit Button
        submit_btn = tk.Button(root, text="✅ Submit Form", font=("Arial", 14, "bold"),
                               bg="#2e7d32", fg="white", relief="raised", padx=10, pady=5,
                               command=self.submit_form)
        submit_btn.pack(pady=15)

    def submit_form(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_var.get()
        program = self.program_var.get()
        hostel = self.hostel_var.get()
        transport = self.transport_var.get()
        marks = self.marks_entry.get()

        if not name or not age or not marks:
            messagebox.showwarning("⚠️ Missing Info", "Please fill all required fields!")
            return

        try:
            age = int(age)
            marks = int(marks)
        except:
            messagebox.showerror("❌ Invalid Input", "Age and Marks must be numbers!")
            return

        # Create Student + University
        student = Student(name, age, gender, program, marks, hostel == "Yes", transport == "Yes")
        uni = University()
        fee, scholarship, percentage = uni.calculate_fee(student)

        # Build output
        output = f"""
        🎓 University Admission Form 🎓
        
        Name: {student.name}
        Age: {student.age}
        Gender: {student.gender}
        Program: {student.course}
        Course Duration: {uni.get_duration(student.course)}
        
        Marks: {student.marks}/1100
        Percentage: {percentage:.2f}%
        
        Scholarship: {"50% Scholarship" if scholarship > 0 else "None"}
        Hostel Facility: {"Yes" if student.hostel else "No"}
        Transport Facility: {"Yes" if student.transport else "No"}
        
        Total Payable Fees: Rs. {int(fee)}
        """

        messagebox.showinfo("📜 Admission Details", output)


# Run App
root = tk.Tk()
app = AdmissionFormGUI(root)
root.mainloop()
