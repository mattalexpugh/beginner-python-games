#!/usr/bin/python
"""
A more comprehensive implementation of backslang... allows encryption & decryption!

You take the first letter of a word and put it in the end, then add 'ay' on the end.
It's hard at first but the more you do it the easier it becomes to understand.
"""

PIG_PART = 'ay'

def convert_to_pig_latin(sentence):
	words = sentence.split()
	new_sentence = []

	for word in words:
		first_char = word[0]
		new_word = word[1:] + first_char + PIG_PART
		new_sentence.append(new_word)

	return " ".join(new_sentence).capitalize()

def convert_from_pig_latin(sentence):
	"""
	Expects the input parameter sentence to be already
	in backslang format. Returns the unencrypted format.
	"""
	words = sentence.split()
	new_sentence = []
	num_chars_to_delete = len(PIG_PART)

	for word in words:
		chopped = word[:-(num_chars_to_delete + 1)]
		first_char = word[num_chars_to_delete]
		new_word = first_char + chopped
		new_sentence.append(new_word)

	return " ".join(new_sentence).capitalize()

## Program logic starts here

# First thing we need to do, is get the source sentence in either case.
sentence = raw_input("Enter sentence to be translated: \n")
# Now, let's prompt the user for the mode of operation,
# i.e. are we encrypting or decrypting?
run_type = raw_input("Decrypt (D) or Encrypt (E)? ")

# Control statement. If they entered a 'D' for the run_type, we need
# to decrypt the string.
if run_type == "D":
	translated = convert_from_pig_latin(sentence)
else: # Otherwise, it's pretty safe to say we are encrypting the string
	translated = convert_to_pig_latin(sentence)

print translated # Print out the result et voila! Done.
