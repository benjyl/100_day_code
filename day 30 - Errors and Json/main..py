# # Filenot found

# try:
#     file = open("a_file.txt") # don't actually have this file
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"]) 
# except FileNotFoundError: # just using except will mean that the second error, i.e. the incorrect key usage will not be caught
#     file = open("a_file.txt", 'w')
#     file.write("something")

# except KeyError as error_message: # allows you to get original error message + whatever want to do
#     print(f"The key {error_message} does not exist")
# else: # if all succeeds, no errors
#     content = file.read()
#     print(content)
# finally: # happens whatever occurs
#     raise TypeError("This is self-made error") # raises error 

'''
height = float(input("Height: "))
weight = float(input("weight: "))

if height > 2.7:
    raise ValueError("Human height not greater than 2.7m")

bmi = weight / (height**2)
print(bmi)

'''

# Index error challenge
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

