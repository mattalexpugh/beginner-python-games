#!/usr/bin/python
"""
You take the first letter of a word and put it in the end, then add 'ay' on the end.
It's hard at first but the more you do it the easier it becomes to understand.
"""

sentence = raw_input("Enter sentence to be translated: \n")
pig_part = 'ay' # This is the part we are putting in
words = sentence.split() # Make a list of words
new_sentence = [] # Make an empty list for our new words

for word in words:
	first_char = word[0] # Get the first character only
	rest_of_word = word[1:] # Get the rest of the word after the first character
	new_word = rest_of_word + first_char + pig_part # Construct our backslang word
	new_sentence.append(new_word) # Place the new word in our new sentence list

# Join the list of words with spaces between them, then print it out, done!
print " ".join(new_sentence).capitalize() # Capitalise works on the first char of the sentence.
