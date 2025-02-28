"""
burger - function
extra chees - extra feature

main function > function add
without chanding the main function code
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper
@my_decorator
def say_hello():
    print('Hello')
    
say_hello()