import pandas

nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_file.iterrows()}

word = input("Enter a word: ").upper()
phonetics = [f"{letter} for {nato_dict[letter]}" for letter in word]

print(f"The NATO Phonetics for your word are: \n{phonetics}")
