#19. Teacher and SubjectTeacher

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} teaches in general")

class MathTeacher(Teacher):
    def teach(self):
        print(f"{self.name} teaches mathematics")

t = MathTeacher("Mrs. Kapoor")
t.teach()