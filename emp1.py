class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def display(self):
        print("id:", self.emp_id, "name:", self.name, "salary:", self.salary)
n = int(input("Enter number of employees: "))
employees = []
for i in range(n):
    print(f"\nEnter details for Employee {i+1}")
    emp_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))
    emp = Employee(emp_id, name, salary)
    employees.append(emp)
print("\nEmployee Details:")
for emp in employees:
    emp.display()
search_id = int(input("\nEnter employee id to search: "))
found = False
for emp in employees:
    if emp.emp_id == search_id:
        print("Employee found:")
        emp.display()
        found = True
        break
if not found:
    print("Employee not found")
highest = employees[0]
for emp in employees:
    if emp.salary > highest.salary:
        highest = emp
print("\nEmployee with highest salary:")
highest.display()
print("\nEmployee with salary greater than 50000:")
for emp in employees:
    if emp.salary > 50000:
        emp.display()
