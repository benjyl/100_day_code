# *args get passed in to function as a tuple
# **kwargs passed in as a dict

def add(*args):
    # total = 0
    # for i in args:
    #     total += i
    print(sum(args))

def calculate(n, **kwargs):
    print(kwargs)
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)
    
sum_1 = add(1,3,5,6,3,1,3)
sum_2 = add(15,3465,1223,124)

calculate(2, add=3, multiply=5)