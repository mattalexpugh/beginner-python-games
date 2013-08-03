import random
import sys

def read_dictionary():
    """
    Reads in a file, dict.txt, which contains the dictionary to be used in the
    game.
    """
    dict_file = open('dict.txt')
    temp_dict = []

    for line in dict_file: # Every line in the file is a single word
        temp_dict.append(line.strip()) # Append each one to our temp_dict

    dict_file.close() # Not strictly necessary, but tell the OS to release the dict.txt file

    return temp_dict


dictionary = read_dictionary()
dictionary = [x for x in dictionary if len(x) <= 8]
random_word = dictionary[random.randint(0, len(dictionary))].lower()
chars = [x for x in random_word]
random.shuffle(chars)
anagram = " ".join(chars).upper()


print("Anagram round! Guess the word:")
print("\n\n" + " " * 5 + anagram + "\n\n")

answer = raw_input("What's the unscrambled word? ")
answer = answer.strip().lower()

if answer == random_word:
    print("Correct!")
else:
    print("Nope, it was " + random_word)
