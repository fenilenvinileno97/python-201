#!/usr/bin/env python3

import random

def pc_option():
    options = ['paper', 'scissors', 'rock']
    chosen_option_pc = options[random.randint(0, 2)]
    return chosen_option_pc

def user_option():
    options = ['paper', 'scissors', 'rock']
    chosen_option_user = input('Choose an option: ').lower()
    try:
        assert chosen_option_user in options, 'Choose an option between paper, scissors, and rock'
    except AssertionError as e:
        print(e)
    return chosen_option_user

def run():
    pc = pc_option()
    user = user_option()
    
    if user == pc:
        print('There is a tie')
    elif ((user == 'paper' and pc == 'rock') or (user == 'rock' and pc == 'scissors') or (user == 'scissors' and pc == 'paper')):
        print(f'you win, you got {user}')
    else:
        print(f'pc wins, pc got {pc}')

if __name__ == '__main__':
    run()