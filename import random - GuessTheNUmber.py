import random

sNumber = random.randint(1,20)
print('My number is between 1 and 20')

#Ask the player to guess 6 times
for guessTaken in range(1,7):
    print('take a guess')
    guess = int(input())

    if guess < sNumber:
        print('too low')
    elif guess > sNumber:
        print('too high')
    else:
        break #zgadnięcie liczby
if guess == sNumber:
    print('GJ, you guessed in ' + str(int(guessTaken)) + ' guesses')
else:
    print(' i was thinking of ' + str(int(sNumber)))

