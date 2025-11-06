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
            "Computer Science": 60000,
            "Electrical Engineering": 60000,
            "Business": 60000,
            "Arts": 60000
        }
        self.duration = {
            "Computer Science": "4 years",
            "Engineering": "4 years",
            "Business": "4 years",
            "Arts": "4 years"
        }
        self.hostel_fee = 30000
        self.transport_fee = 15000

    def calculate_fee(self, student):
        base_fee = self.fees.get(student.course, 40000)

        percentage = (student.marks / 1100) * 100

        # Scholarship system
        if percentage >= 90:   # 90% or above
            scholarship = 0.5   # 50% discount
        else:
            scholarship = 0     # no scholarship

        fee_after_scholarship = base_fee - (base_fee * scholarship) # (60000 * 0.5) = 30000

        # Add hostel fee if opted
        if student.hostel:
            fee_after_scholarship += self.hostel_fee

        # Add transport fee if opted
        if student.transport:
            fee_after_scholarship += self.transport_fee

        return fee_after_scholarship, scholarship, percentage

    def get_duration(self, course):
        return self.duration.get(course, "N/A")

class AdmissionForm:
    def __init__(self, student, university):
        self.student = student
        self.university = university
        self.fee, self.scholarship, self.percentage = university.calculate_fee(student)

    def display_form(self):
        print("\n--- University Admission Form ---")
        print(f"Name: {self.student.name}")
        print(f"Age: {self.student.age}")
        print(f"Gender: {self.student.gender}")
        print(f"Course: {self.student.course}")
        print(f"Course Duration: {self.university.get_duration(self.student.course)}")
        print(f"Marks: {self.student.marks}/1100")
        print("Percentage:", self.percentage, "%")
        
        if self.scholarship > 0:
            print(f"Scholarship Applied: {int(self.scholarship * 100)}% (for 90%+ marks)")
        else:
            print("Scholarship Applied: None")
        
        if self.student.hostel:
            print("Hostel Facility: Yes")
        else:
            print("Hostel Facility: No")

        if self.student.transport:
            print("Transport Facility: Yes")
        else:
            print("Transport Facility: No")

        print(f"Total Payable Fee: Rs. {self.fee}")
        print("---------------------------------")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (Male/Female): ")
course = input("Enter your desired course (Computer Science, Electrical Engineering, Business, Arts): ")
marks = int(input("Enter your marks out of 1100: "))

hostel = input("Do you want hostel facility? (yes/no): ").lower() == "yes"
transport = input("Do you want transport facility? (yes/no): ").lower() == "yes"

student = Student(name, age, gender, course, marks, hostel, transport)
uni = University()
form = AdmissionForm(student, uni)
form.display_form()