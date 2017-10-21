#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.
play = 'Y'
while play == 'Y':
	guess_list = []
	guess = ''
	ans = 5 #random between 1-9 including 1 & 9
	while guess != ans:
		guess = int(input ('Make a guess: '))
		guess_list.append(guess)
		if guess - ans > 0:
			print ('too high')
		elif guess - ans < 0:
			print ('too low')
		else:
			print ('Correct!')
			print ('You guessed', len(guess_list), 'time(s)')
			play = input('To keep playing type "Y". To quit type "exit": ')
	