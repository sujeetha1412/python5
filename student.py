class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def get_average(self):
        return sum(self.marks) / len(self.marks)
    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "Fail"
n = int(input("Enter no. of students: "))
for i in range(n):
    name_input = input("Enter student name: ")
    roll_no_input = int(input("Enter roll no: "))
    marks_list = []
    for j in range(1, 6):
        m = float(input("Enter marks for subject " + str(j) + ": "))
        marks_list.append(m)
    s1 = Student(name_input, roll_no_input, marks_list)
    print("\n--- Student Report ---")
    print("Name:          ", s1.name)
    print("Roll no:       ", s1.roll_no)
    print("Average Marks: ", s1.get_average())
    print("Final Grade:   ", s1.get_grade())
