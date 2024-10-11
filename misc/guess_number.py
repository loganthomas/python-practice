"""
Generate a random number between 1 and 9 (including 1 and 9).

Ask the user to guess the number, then tell them whether they guessed
too low, too high, or exactly right.

Extras:
    - Keep the game going until the user types “exit”
    - Keep track of how many guesses the user has taken, and when the
      game ends, print this out.
"""

import random

play = 'Y'
while play == 'Y':
    ans = random.randint(1, 9)
    guess = ''
    cnt = 0
    while guess != ans:
        guess = int(input('Make a guess: '))
        cnt += 1

        if guess - ans > 0:
            print('too high')
        elif guess - ans < 0:
            print('too low')
        else:
            print('Correct!')
            print(f'You guessed {cnt} time(s)')
            play = input('To keep playing type "Y". To quit type "exit": ')
