#!/usr/bin/python

"""
Hangman game, developed based upon the Perl version written by Claire Q, Python'd by Matt Pugh.
"""

import random # Necessary so we can get a random integer later.

# Define our basic, file-loading functions here (Need to define things *before* we call them)

def read_dictionary():
	"""
	Reads in a file, dict.txt, which contains the dictionary to be used in the
	game.
	"""
	dict_file = open('dict.txt')
	temp_dict = []
	
	for line in dict_file: # Every line in the file is a single word
		temp_dict.append(line) # Append each one to our temp_dict

	dict_file.close() # Not strictly necessary, but tell the OS to release the dict.txt file

	return temp_dict

def get_word():
	"""
	Get a random word from the dictionary we have loaded in.
	"""
	size = len(dictionary) # How many words in the dictionary?
	num = int(random.randint(0, size)) # Generate a random integer from range 0 - size
	word = dictionary[num] # Get the word located at that number in our dictionary

	return word

# Now we can set up our variables for the game

dictionary = read_dictionary() 		# The dictionary of words to choose from
word = get_word() 					# The word to guess for this game
answer = word
length = len(word) 
spaces = [] 						# The display array of characters
hanged = 0							# How far hanged is the man?
won = False							# Has the player won?
guess = None
prev_guesses = []					# Letters already guessed

# Define our game functions (or subroutines) here

def welcome():
	print "Welcome to hangman!\n"
	print "Here we go:\n"

def make_spaces():
	"""
	Initialise the word spaces for the game to be empty.
	"""
	for i in range(1, length):
		spaces.append('_')

def clear_screen():
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

def drawing():
	"""
	Draw the current status of the player, we rely on the variable hanged
	to ascertain the current game status.
	"""
	clear_screen()

	if hanged == 0:
		print "\n\n\n\n\n"
	elif hanged == 1:
		print "    "
		print "    "
		print "    "
		print "    "
		print "   |"
	elif hanged == 2:
		print "    "
		print "    "
		print "    "
		print "   |"
		print "   |"
	elif hanged == 3:
		print "    "
		print "    "
		print "   |"
		print "   |"
		print "   |"
	elif hanged == 4:
		print "    "
		print "   |"
		print "   |"
		print "   |"
		print "   |"
	elif hanged == 5:
		print "  _ "
		print "   |"
		print "   |"
		print "   |"
		print "   |"
	elif hanged == 6:
		print " __ "
		print "   |"
		print "   |"
		print "   |"
		print "   |"
	elif hanged == 7 :
		print " __ "
		print "|  |"
		print "   |"
		print "   |"
		print "   |"
	elif hanged == 8:
		print " __ "
		print "|  |"
		print "o  |"
		print "   |"
		print "   |"
	elif hanged == 9:
		print " __ "
		print "|  |"
		print "o  |"
		print "|  |"
		print "   |"
	elif hanged == 10:
		print " __ "
		print "|  |"
		print "o  |"
		print "|  |"
		print "/  |"
	elif hanged == 11:
		print " __ "
		print "|  |"
		print "o  |"
		print "|  |"
		print '/\ |'
	else: # If we end up here, hanged has to be greater than 11, game is over!
		print "you lose"

def show_spaces():
	"""
	Show the spaces for the answer, with correct and previous guesses too.
	"""
	print "".join(spaces)
	print "Guessed letters: " + " ".join(prev_guesses)

def get_guess():
	player_input = '0' # Initialise as some string that is *NOT* in the alphabet

	while not player_input.isalpha(): # For as long as the input isn't alphabet characters...
		player_input = raw_input("Please enter a letter to guess:\n")
		player_input.strip() # Clean off any whitespace or \n from the input

	return player_input[0] # Return only the first character

def check_guess(current_guess):

	found = False # Initialise this variable for later

	if current_guess in prev_guesses:
		# If the character current_guess is in prev_guesses,
		# then they have already guessed this character.
		print "Already guessed!\n";
	else:
		if current_guess in answer:
			# If it hasn't been guessed already and it is a
			# correct guess, find the position of the character
			# in the word so we can drop it in over the _ in
			# the spaces variable.
			position = answer.find(current_guess)
			spaces[position] = current_guess
			found = True

		if not '_' in spaces:
			# If there are no more underscores in spaces,
			# then we have found all the letters!
			won = True
			clear_screen()
			drawing()

			# Print the result here as the program will end
			print "".join(spaces) + "\n"

		prev_guesses.append(current_guess)

		return found

## Program logic here, we have already defined everything we need.

welcome()
make_spaces()

# Start of main program loop

while hanged < 11 and not won:
	"""
	This loop has two conditions. Whilst either the value of hanged is
	less than 11 or the variable won isn't True, it'll continue to loop.
	"""

	drawing()
	show_spaces()
	found = check_guess(get_guess())

	if not found: # If they didn't find a correct character, hang some more.
		hanged = hanged + 1

# End of main program loop

if won:
	# If we're here, the player won the game, congratulate them!
	print "Well Done!\n"
else:
	# Otherwise, not so lucky...
	print "Bad Luck! :(\n"

# That's it! The program has finished.