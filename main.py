import pandas

# Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in df.iterrows()}
print(alphabet)

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Put a word here:  ").upper()

alpha_words = [alphabet[letter] for letter in user_input if letter in alphabet.keys()]
print(alpha_words)