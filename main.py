import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

data = pandas.read_csv('nato_phonetic_alphabet.csv')


all_alphabet_dict = []
for current_student in student_dict['student']:
    alphabet_dict = {letter:data.code[data.letter == letter.upper()].iloc[0] for letter in current_student}
    all_alphabet_dict.append(alphabet_dict)

# List of all Names with phonetic alphabet.
print(all_alphabet_dict)

user_input = input("Enter a Name to get the Phonetic Alphabet: ")
alphabet_dict = {}
while user_input != "Exit":
    alphabet_dict = {letter:data.code[data.letter == letter.upper()].iloc[0] for letter in user_input}
    print(alphabet_dict)
    user_input = input("Enter a Name to get the Phonetic Alphabet: ")
