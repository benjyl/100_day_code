import time

# Decorator function that causes function to wait 2 seconds before being called
# Decorator modifies functionality, adds something before function or after
def delay_decorator(function):
    def wrapper_function():
        
        time.sleep(2)
        # Do something before
        function()
        # Do something after
    return wrapper_function 

@delay_decorator # adds delay_decorator to this function
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")
    
say_hello() # takes 2 seconds to be called
say_greeting() # called immediately

import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    # need wrapper function to stop function being called when decorator put on top of function
    # function with decorator should only run when function called
    def wrapper_function(): 
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}")
    return wrapper_function
    
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator  
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
