class ExceptionDemo:
    def divide(self):
        try:
            a = int(input("Enter a number: "))
            b = int(input("Enter another number: "))
            a=int(a)
            b=int(b)
            result=a/b
            print("Result:",result)
        except ZeroDivisionError:
            print("Error:can't divide by zero")
        except ValueError:
            print("Error:input must be number")
    def access_list(self):
        try:
            lst=[]
            n=int(input("Enter a number of elements in list: "))
            for i in range(n):
                val=int(input("Enter element:"))
                lst.append(val)
            index=int(input("Enter index:"))
            print("Element:",lst[index])
        except IndexError:
            print("Error:index out of range")
        except ValueError:
            print("Error:input must be number")
    def access_dict(self):
        try:
            dic={}
            n=int(input("Enter a number of elements in dict: "))
            for i in range(n):
                key=input("Enter key:")
                value=input("Enter value:")
                dic[key]=value
            k=input("Enter key to search:")
            print("value:",dic[k])
        except KeyError:
            print("Error:key not found in dict")
obj=ExceptionDemo()
print("---Division---")
obj.divide()
print("---Access List---")
obj.access_list()
print("---Access Dict---")
obj.access_dict()
