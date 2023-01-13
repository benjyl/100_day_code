import pandas

# challenge: Create a script that will list the phonetic equivalent of a word and catch key errors
phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_df.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    user_input = input("Input a word and receive the phonetic equivalent:\n").upper()
    try:
        phonetic_list = [phonetic_dict[i] for i in user_input]
    except KeyError:
        print("Sorry, only give letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()
    
