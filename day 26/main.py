numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

double_range = [2*i for i in range(1,5)]
print(double_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_upper_name = [name.upper() for name in names if len(name) > 5]
print(long_upper_name)

# Task 1: create list of square numbers using list comprehension
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number**2 for number in numbers]
print(squared_numbers)

# Task 2: filter to only get even numbers in list - list comprehension
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num%2==0 ]
print(result)

# Task 3: get common values between 2 text files using list comprehension
file1_list = [int(line.rstrip()) for line in open("file1.txt")]
file2_list = [int(line.rstrip()) for line in open("file2.txt")]

# print(file1_list)
# print(file2_list)

result = [num for num in file1_list if num in file2_list]

print(result)
