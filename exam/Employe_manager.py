class EmployeeManager:
    def __init__(self):
        self.employees = []   # list of dictionaries

    def add_employee(self):
        name = input("Enter employee name: ")
        dept = input("Enter department: ")
        hours = input("Enter hours worked: ")

        if not hours.isdigit():
            print("Invalid hours! Enter numeric value.\n")
            return

        emp_info = {
            "Name": name,
            "Department": dept,
            "Hours": int(hours)
        }

        self.employees.append(emp_info)
        print("Employee added successfully!\n")

    def total_hours_by_department(self):
        if not self.employees:
            print("No data available.\n")
            return

        dept_hours = {}

        for emp in self.employees:
            dept = emp["Department"]
            dept_hours[dept] = dept_hours.get(dept, 0) + emp["Hours"]

        print("\nTotal Hours by Department:")
        for dept, hours in dept_hours.items():
            print(f"{dept} : {hours}")
        print()

    def employees_above_hours(self, limit=8):
        if not self.employees:
            print("No data available.\n")
            return

        print(f"\nEmployees working more than {limit} hours:")
        found = False

        for emp in self.employees:
            if emp["Hours"] > limit:
                print(emp["Name"])
                found = True

        if not found:
            print("No employees found.\n")
        print()

    def show_departments(self):
        if not self.employees:
            print("No data available.\n")
            return

        depts = set()

        for emp in self.employees:
            depts.add(emp["Department"])

        print("\nDepartments:")
        for d in depts:
            print(d)
        print()


def main():
    manager = EmployeeManager()

    while True:
        print("1. Add Employee")
        print("2. Total Hours by Department")
        print("3. Employees above given hours")
        print("4. Show Departments")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_employee()

        elif choice == "2":
            manager.total_hours_by_department()

        elif choice == "3":
            value = input("Enter minimum hours (default 8): ")

            if value == "":
                manager.employees_above_hours()
            elif value.isdigit():
                manager.employees_above_hours(int(value))
            else:
                print("Invalid input!\n")

        elif choice == "4":
            manager.show_departments()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()