#13. User and Admin Access

class User:
    def __init__(self, username):
       self.username = username
    def access(self):
       print(f"{self.username} has user access.")

class Admin(User):
    def access(self):
        print(f"{self.username} has admin access.")

admin1 = Admin("admin_john")
admin1.access()