# Student Model
# Create a student class with `name`, `student_id`, and `assignments`
# a (dictionary with assignment names as keys and grades as values)
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

# Instructor Model
# Create an `Instructor` class with `name`, `course_name`, and a list of `students`
class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []


# Implement methods in `Student` to add an assignment and grade
# Method to add an assignment and grade
def add_assignment(self, assignment_name, grade):
    self.assignments[assignment_name] = grade
    print(f"Assignment '{assignment_name}' added with a grade of {grade} for {self.name}.")


# Implement methods in `Student` to display grades
# Method to display grades for the student
def display_grades(self):
    print(f"\nGrades for {self.name} and students ID (ID: {self.student_id}):")
    if self.assignments:
        for assignment, grade in self.assignments.items():
            print(f"- {assignment}: {grade}")
    else:
        print("No assignments found.")


# Implement methods in `Instructor` to add a student to the course
# Method to add a student to the course
def add_student(self, student):
    self.students.append(student)
    print(
        f"Student with the name {student.name} with Student ID (ID: {student.student_id}) has been added to the course '{self.course_name}' successfully."
    )


# Implement methods in `Instructor` to assign a grade to a student
# Method to assign a grade to a student based on student_id
def assign_grade(self, student_id, assignment_name, grade):
    # Find the student by their  Students ID
    student = None  # Default value
    for s in self.students:
        if s.student_id == student_id:
            student = s  # Found student
            break  # Exit the loop
    if student:
        student.add_assignment(assignment_name, grade)
    else:
        print(f"Student with ID {student_id} has not been found.")


# Implement methods in `Instructor` to display all students and their grades
# Method to display all students and their grades
def display_students_grades(self):
    print(f"\nGrades for students in '{self.course_name}':")
    if self.students:
        for student in self.students:
            student.display_grades()
    else:
        print("No students found in this course.")


# Implement methods in `Instructor` to Write code to allow an instructor to add students and assign grades interactively
def main():
    # Initialize the instructor and course
    instructor = Instructor("Mr. Njoroge", "Python Bootcamp")

    while True:
        print("\nOnline Course Management System")
        print("1. Add Student")
        print("2. Assign Grade to Student")
        print("3. Display All Students and Grades")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)

        elif choice == "3":
            instructor.display_students_grades()

        elif choice == "4":
            print("Exiting the Online Course Management System.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
