
# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Lec 12: Rock, Paper, Scissors

import random

op = ['rock', 'paper', 'scissors']

while True:
    userr = input('\nrock, paper, scissors? ')
    print('............................................')
    compp = random.choice(op)
    
    print('You chose:', userr)
    print('Computer chose:', compp)
    
    if userr == compp:
        print('\nTie!')
    elif userr == 'rock' and compp == 'paper':
        print('\nComputer Won')
    elif userr == 'rock' and compp == 'scissors':
        print('\nYou Won')
    elif userr == 'paper' and compp == 'rock':
        print('\nYou Won')
    elif userr == 'paper' and compp == 'scissors':
        print('\nComputer Won')
    elif userr == 'scissors' and compp == 'rock':
        print('\nComputer Won')
    elif userr == 'scissors' and compp == 'paper':
        print('\nYou Won')
    else:
        print('\nInvalid Input')
        
    print('===========================================')
        
    res = input('Play Again? (y/n): ')
    if res != 'y':
        break