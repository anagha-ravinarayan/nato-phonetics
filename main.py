import pandas


def phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetics = [f"{letter} for {nato_dict[letter]}" for letter in word]
    except KeyError as e:
        print("Sorry, please only enter letters in the Alphabet.\n")
        phonetic()
    else:
        print(f"The NATO Phonetics for your word are: \n{phonetics}")


nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_file.iterrows()}

phonetic()
