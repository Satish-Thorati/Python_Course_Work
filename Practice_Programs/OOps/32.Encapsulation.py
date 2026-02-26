#32. Password Protection

class User:
    def __init__(self, password):
        self.__password = password

    def change_password(self, old, new):
         if old == self.__password:
            self.__password = new
            print("Password changed")
         else:
             print("Incorrect old password")

u = User("1234")
u.change_password("1234", "abcd")