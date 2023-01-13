import pandas

# challenge: Create a script that will list the phonetic equivalent of a word
phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_df.iterrows()}
print(phonetic_dict)

user_input = input("Input a word and receive the phonetic equivalent:\n").upper()
word_list = [i for i in user_input]
phonetic_list = [phonetic_dict[i] for i in user_input]
print(phonetic_list)
