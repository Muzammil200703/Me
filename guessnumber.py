# Guess number between 1 to 100
# generate a number dont print it
# if user selects anything other than number say invalid number
# if user guesses number too high say too high
# if user guesses number too low say too low
# if user guesses correct number say congratulations! You guessed it right
import random


number_to_guess = random.randint(1,100)
while True:
     choice1 = input('Guess a number between 1 to 100')
     if int(choice1) > number_to_guess:
               print('Too high!')
     elif int(choice1) < number_to_guess:
               print('Too low!')
     if int(choice1) == number_to_guess:
               print('Congratulations,You guessed it right!')
               break