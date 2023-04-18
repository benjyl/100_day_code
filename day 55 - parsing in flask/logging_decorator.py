# Create the logging_decorator() function 👇
def logging_decorator(function):
    # prints the function name, input and output 
    def wrapper(*args, **kwargs):
        print(f"You called: {function.__name__}{args}")
        output = function(*args, **kwargs)
        print(f"It returned: {output}")
    return wrapper

# Use the decorator 👇
@logging_decorator
def my_func(a,b,c):
    return sum([a,b,c])

my_func(1,2,3)