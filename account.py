[25bcs165@mepcolinux ex5]$cat login.py
class InvalidLoginError(Exception):
    pass
class AccountLockedError(Exception):
    pass
class Loginsystem:
    def __init__(self):
        self.username=input("set your Username: ")
        self.password=input("set your Password: ")
        self.max_attempts=3
    def login(self):
        attempts=0
        while attempts < self.max_attempts:
            try:
                user=input("Enter Username: ")
                pwd=input("Enter Password: ")
                if user!=self.username or pwd!=self.password:
                    attempts+=1
                    raise InvalidLoginError("Invalid Username or Password")
                print("Login Successful")
                return
            except InvalidLoginError as e:
                print(e)
                print("Attempts Left:",self.max_attempts-attempts)
        raise AccountLockedError("Account Locked due to too many attempts")
obj=Loginsystem()
try:
    obj.login()
except AccountLockedError as e:
    print(e)
