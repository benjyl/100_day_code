import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass



student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# challenge: Create a script that will list the phonetic equivalent of a word


# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_df.iterrows()}
print(phonetic_dict)

user_input = input("Input a word and receive the phonetic equivalent:\n").upper()
word_list = [i for i in user_input]
phonetic_list = [phonetic_dict[i] for i in user_input]
print(phonetic_list)
