#Generate a random number from 1-100
import random
number = random.randint(1,100)
print(number)
# be careful not to make the mistake of using print, input(...) asks the user for input and returns a string.

#You’re wrapping that in print(...), which prints the string—but print() always returns None.
#so you’re assigning guess = None, and then comparing None < number, which raises a TypeError.that Compare the user's guess to the generated number
guess = int(input('Please guess a number between 1 and 1 hundred: \n'))

if guess < number:
    print('Your guess was too low!')
elif guess > number:
    print('Your guess was too high!')
elif guess == number:
    print('Your guess was just right, congrats!')
else:
    print('The math is not mathing...')

#Print the number (for easier debugging)
#Ask the user to guess the number
#Print that the guess was too high / too low / just right!

