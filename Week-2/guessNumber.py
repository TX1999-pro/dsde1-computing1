# Week 2 Practice
'''
Number Guessing Game 
 - ask the users to guess the number between 1 and 10
'''
import random
print('Welcome to the game!')
print('A number between 1 and 10 is randomly generated. What is it?')
gen_number = random.randint(1,10) #generate a random number

#Without if statements
guess = input()
guess = int(guess)
print ( guess == gen_number)

#With if statement within a loop
'''
for i in range(10):
    
    guess = input()
    guess = int(guess)

    if guess == gen_number:
        print('Bingo! You are right!')
        print('No. of attempts: ' + str(i+1) )
        break 
    else:
        print('Sorry, try again')

'''