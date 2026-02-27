#33. Encapsulated Student Info

class Student:
    def __init__(self, name):
        self.__name = name

def get_name(self):
    return self.__name

s = Student("Riya")
print(s.get_name())