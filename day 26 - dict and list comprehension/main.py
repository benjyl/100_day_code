import random

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

double_range = [2 * i for i in range(1, 5)]
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
result = [num for num in numbers if num % 2 == 0]
print(result)

# Task 3: get common values between 2 text files using list comprehension

file1_list = [int(line.rstrip()) for line in open("file1.txt")]
file2_list = [int(line.rstrip()) for line in open("file2.txt")]

# print(file1_list)
# print(file2_list)

result = [num for num in file1_list if num in file2_list]

print(result)

# student score dictionary comprehension
student_score = {name: random.randint(0, 100) for name in names}
print(student_score)

passed_students = {
    name: score for (name, score) in student_score.items() if score >= 40
}
print(passed_students)

# Dict comprehension task 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {
    word: len(word) for word in sentence.split()
}  # don't need to create list variable first


print(result)

# Dict comprehension task 2, convert deg_c -> deg_f for week temps
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
