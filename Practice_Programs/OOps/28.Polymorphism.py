#28. Employee Roles

class Employee:
    def role(self):
        pass

class Developer(Employee):
     def role(self):
         print("Writes code")

class Designer(Employee):
     def role(self):
         print("Creates UI")

team = [Developer(), Designer()]
for member in team:
     member.role()