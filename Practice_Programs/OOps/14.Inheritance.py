#14. Employee and Manager

class Employee:
    def __init__(self, name):
        self.name = name
    def show_role(self):
        print("General employee")


class Manager(Employee):
    def show_role(self):
        print("Manager with team responsibilities")

mgr = Manager("Ravi")
mgr.show_role()