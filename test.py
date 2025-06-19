# def make_multiplier(n):
#     def innerfunc(x):
#         return x*n
#     return innerfunc

# funccall=make_multiplier(3)
# print(funccall(10))



class Student:
    count = 0  # Class variable to count number of students

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def show(self):
        print(f"Name: {self.name}")

    @classmethod
    def total_students(cls):
        print(f"Total Students: {cls.count}")

s1 = Student("Rahul")
s2 = Student("Sneha")
s3 = Student("Aarav")

Student.total_students()  # Output: Total Students: 3

# Decorator function
def log_decorator(func):
    def wrapper():
        print("Function is being called...")
        func()
        print("Function has finished executing.")
    return wrapper

# Using the decorator
@log_decorator
def say_hello():
    print("Hello, World!")

# Call the decorated function
say_hello()




