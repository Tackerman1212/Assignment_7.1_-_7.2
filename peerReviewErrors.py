# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Tanner Ackerman
# Creation Date: 2/15/2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

#correct
def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()


def chooseCave():	
	
	cave = ''
	
	# while cave != '1' and cave != '2':
		#print('Which cave will you go into? (1 or 2)')
		#cave = input()
		
	while(True):
		print('Which cave will you go into? (1 or 2)')
		cave = input()
		if cave == '1' or cave == '2':
			break
			
	# ERROR #1 & #2: First was a logic error, I turned it to a while(True) statement with a "break", and the second error was changing "and" to "or". I also changed "!=" to "==" to fit the new logic. 

	#return caves
	return cave
	# ERROR #3: 'caves' should not be plural, simple syntax error. Correct version is 'cave'.

	
# def checkCave(chosenCave):
def checkCave(chooseCave):
# ERROR #4: 'chosenCave' was given the past tense language, the syntax was incorrect by not matching the previously established function name of 'chooseCave'.
	
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	
	#sleep for 2 seconds
	#time.sleep(3)
	time.sleep(2)
	# ERROR #5: '3' was entered incorrectly and was replaced with '2' which is correct according to the stated comments in the code.
	
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	#if chosenCave == str(friendlyCave):
	if chooseCave == str(friendlyCave): 
	# ERROR #6: 'chosenCave' should be 'chooseCave' to match the previous function name. Also 'friendlyCave' wouldn't be a 'str' or string, it is an integer or 'int'.
		
		print('Gives you his treasure!')
	else:
		#print 'Gobbles you down in one bite!'
		print('Goobles you down in one bite!')
		# ERROR #7 Parenthesis were forgotten on the print() function.


playAgain = 'yes'

#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
# ERROR #8: changed "=" to "==" for comparison purposes.
	
	displayIntro()
	
	#caveNumber = choosecave()
	caveNumber = chooseCave()
	# ERROR #9: Case sensitive syntax error not matching the previously defined function of 'chooseCave'.
	
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		#print("Thanks for planing")
		print("Thanks for playing")
		# ERROR #10: A typo 'planing' should be 'playing'.

