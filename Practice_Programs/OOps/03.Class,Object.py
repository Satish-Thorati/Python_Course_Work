#3. Student Grade Evaluator
'''Problem: Create a Student class with a list of marks. Add a method to return average and
pass/fail.
Answer:'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        avg = sum(self.marks) / len(self.marks)
        return avg >= 40
# Object and method call
s1 = Student("Priya", [45, 56, 60])
print("Passed:", s1.is_passed())