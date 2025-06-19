import time

def log_decorator(func):
    def wrapper():
        print("Function is being called...")
        func()
        time.sleep(5)
        print("Function has finished executing.")
    return wrapper

@log_decorator
def test():
    print("Testing decorator")

test()