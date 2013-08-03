#!/usr/bin/python

"""
A riddle game, the player must answer 3 out of 5 riddles correctly to win.
Riddles and answers are loaded from two files:

	- riddle_questions.txt
	- riddle_answers.txt

The line numbers between the files should match, meaning that the answer on
line 10 of riddle_answers.txt should be the answer to the riddle on line 10
of riddle_questions.txt

Bunch of ASCII art from http://www.asciiworld.com/
"""

import random # Used later to randomly select questions

# Base file-loading functions

def read_riddles():
	riddle_file = open('riddle_questions.txt')
	riddles = []

	for line in riddle_file:
		riddles.append(line.strip()) # Get rid of newline character

	riddle_file.close()

	return riddles

def read_answers():
	answer_file = open('riddle_answers.txt')
	answers = []

	for line in answer_file:
		answers.append(line.strip()) # Get rid of the newline character

	answer_file.close()

	return answers

def clear_screen():
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

def clear_lines(num):
	print "\n" * num

# Game variables

riddles = read_riddles()
answers = read_answers()
num_riddles = len(riddles)

won = False
attempts = 0
num_correct = 0
riddles_chosen = None

# Game specific screens and outputs

def welcome_screen():
	clear_screen()

	text = """
. . . .-. .   .-. .-. .  . .-.   .-. .-. 
| | | |-  |   |   | | |\/| |-     |  | | 
`.'.' `-' `-' `-' `-' '  ` `-'    '  `-'  .  .  .

    
             d8b                            d8,      d8b       d8b  d8b                 
       d8P   ?88                           `8P       88P       88P  88P                 
    d888888P  88b                                   d88       d88  d88                  
      ?88'    888888b  d8888b      88bd88b  88b d888888   d888888  888   d8888b  88bd88b
      88P     88P `?8bd8b_,dP      88P'  `  88Pd8P' ?88  d8P' ?88  ?88  d8b_,dP  88P'  `
      88b    d88   88P88b         d88      d88 88b  ,88b 88b  ,88b  88b 88b     d88     
      `?8b  d88'   88b`?888P'    d88'     d88' `?88P'`88b`?88P'`88b  88b`?888P'd88' 


"""
	print text
	clear_lines(3)

def show_challenge():
	clear_screen()
	text = """
    ____________________________
  |____________________________|
 /______________________________\    Bonjour, je suis le riddler. Or, problement,
|________________________________|   en your language, I am the riddler. I have a
[)      /                \      (]   challange pour vous. In this game, I will ask
[)   |\/   ^          ^   \ /|  (]   cinq (that's 5 in your English) questions.
[)   | |   o    L     o    | |  (]
     |                       |       If you can answer 3 correctly, you win! Simple!
     | |                   | |
     |/       .......       \|
        \                 /
         \               /
          \_____))))____/
                 ))                  OK? Let's go! On y va!
                 ))
"""
	print text

def get_player_name():
	raw_name = raw_input("Welcome challenger, what is your name? ")
	raw_name.strip()
	return raw_name

def setup_riddles():
	riddle_numbers = []

	for i in range(0, 5):
		selected = False

		while not selected:
			number = random.randint(0, num_riddles)

			if number in riddle_numbers:
				continue
			else:
				riddle_numbers.append(number)
				selected = True

	return riddle_numbers

def wait_for_input():
	print "Press ENTER to continue"
	inp = raw_input() # Use this as a pause

def show_next_riddle():
	riddle_num = riddles_chosen[attempts]
	question = riddles[riddle_num]
	answer = answers[riddle_num]
	answer_size = len(answer)

	clear_screen()

	response = raw_input(question + " (" + str(answer_size) + " chars): ")
	response = response.strip().lower()

	clear_lines(3)

	correct = response == answer

	return correct

# Everything's defined, let's play! Algorithm logic here!
riddles_chosen = setup_riddles()
welcome_screen()
name = get_player_name()

show_challenge()
wait_for_input()

while attempts < 5 and not won:
	clear_screen()
	correct = show_next_riddle()

	if correct:
		print "Well done, you guessed correctly!"
		num_correct += 1
	else:
		print "Bad luck, try the next one."

	clear_lines(3)
	wait_for_input()

	if num_correct == 3:
		won = True
		break
	else:
		attempts += 1

# Out of the game loop now, time to give the good (or bad) news...

clear_screen()

if won:
	print """
   .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-. 
 .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.
(    .     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .    )
 `.   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   .'
   )    )                                                       (    (
 ,'   ,'                                                         `.   `.
(    (                                                             )    )
 `.   `.                                                         .'   .' 
   )    )                                                       (    (
 ,'   ,'                                                         `.   `.
(    (               C O N G R A T U L A T I O N S                 )    )
 `.   `.                                                         .'   .' 
   )    )                                                       (    (
 ,'   ,'                                                         `.   `.
(    (                                                             )    )
 `.   `.                                                         .'   .' 
   )    )       _       _       _       _       _       _       (    (
 ,'   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   `.
(    '  _  `-'  _  `-'  _  `-'  _  `-'  _  `-'  _  `-'  _  `-'  _  `    )
 `.   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   .'
   `-'     `-'     `-'     `-'     `-'     `-'     `-'     `-'     `-'
"""
	
	clear_lines(3)
	print "Well done " + name + ", you have beaten the riddler!"
else:
	print 'Bad Luck, Until Next Time!'
