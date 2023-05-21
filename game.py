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

def rules(pc_option, user_option):
    
    computer_win = 0
    user_win = 0
    
    if user_option == pc_option:
        print('DRAW!')
        
    elif user_option == 'rock':
        if pc_option == 'scissors':
            print('user wins!')
            user_win += 1
        elif pc_option == 'paper':
            print('computer wins!')
            computer_win += 1
    
    elif user_option == 'scissors':
        if pc_option == 'rock':
            print('computer wins!')
            computer_win += 1
        elif pc_option == 'paper':
            print('user wins!')
            user_win += 1
            
    elif user_option == 'paper':
        if pc_option == 'scissors':
            print('computer wins!')
            computer_win += 1
        elif pc_option == 'rock':
            print('user wins!')
            user_win += 1

    return computer_win, user_win
    

def run():
    
    # print('*'*100)
    # print('WELCOME TO PAPER, ROCK, SCISSORS')
    rounds = 0
    
    while True:

        
        pc = pc_option()
        user = user_option()
        
        computer, you = rules(pc, user)
        rounds += 1
        print(computer, you)
        
        if computer == 2:
            print('COMPUTER WON!')
            break
        elif you == 2:
            print('YOU WON!')
            break
        
        print('*'*100)
    
if __name__ == '__main__':
    run()