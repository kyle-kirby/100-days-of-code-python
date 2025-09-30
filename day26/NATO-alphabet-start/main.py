import pandas as pd

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

df = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type in a word: ").upper()
user_phonetic_list = [phonetic_dict[letter] for letter in user_input]
print(user_phonetic_list)


