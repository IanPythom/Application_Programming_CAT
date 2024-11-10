# Employee Model
# Create an `Employee` class with attributes `name`, `employee_id`, and `salary'
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

# Department Model
# Department class to manage employees in a department
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []


# Implement methods in `Employee` to display details
# Method to display employee details
def display_details(self):
    print(f"Employee ID: {self.employee_id}, \nName: {self.name}, \nSalary: ${self.salary}")


# Implement methods in `Employee` to update salary
# Method to update salary
def update_salary(self, new_salary):
    self.salary = new_salary
    print(f"{self.name}'s with the ID: {self.employee_id} has had their salary updated to ${self.salary}.")


# Implement methods in `Department` to add an employee to the department
# Method to add an employee to the department
def add_employee(self, employee):
    self.employees.append(employee)
    print(
        f"Employee {employee.name} (ID: {employee.employee_id}) added to the {self.department_name} department."
    )


# Implement methods in `Department` to calculate and display the total salary expenditure for the department
# Method to calculate and display the total salary expenditure for the department
def calculate_total_salary_expenditure(self):
    total_salary = sum(employee.salary for employee in self.employees) # # This method gets the sum
    print(
        f"The total salary expenditure for {self.department_name} department is: {total_salary}USD."
    )


# Implement methods in `Department` to display all employees
def display_all_employees(self):
    print(f"\nEmployees in {self.department_name} Department:")
    if self.employees:
        for employee in self.employees:
            employee.display_details()
    else:
        print("No employees in this department.")


# Use interactive input to add employees to a department and display total expenditure
def main():
    department = Department("IT")

    while True:
        print("\nEmployee and Department Management System")
        print("1. Add Employee")
        print("2. Update Employees Salary")
        print("3. Display All Employees")
        print("4. Display Total Salary Expenditure")
        print("5. Exit")

        # Get user choice for the action to perform
        choice = input("Enter your choice: ")

        if choice == "1":
            # Option 1 to add an employee
            name = input("Enter employee's name: ")
            employee_id = input("Enter employee ID: ")
            salary = float(input("Enter employee's salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            # Option 2 to update employee salary
            employee_id = input("Enter the employee ID to update salary amount: ")
            employee = next(
                (emp for emp in department.employees if emp.employee_id == employee_id),
                None,
            )
            if employee:
                new_salary = float(input("Enter new salary: "))
                employee.update_salary(new_salary)
            else:
                print(f"No employee found with ID {employee_id}.")

        elif choice == "3":
             # Option to update employee salary
            department.display_all_employees()

        elif choice == "4":
            # Option to display total salary expenditure
            department.calculate_total_salary_expenditure()

        elif choice == "5":
            # Exit the management system
            print("Exiting the Employee and Department Management System.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
