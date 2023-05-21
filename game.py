#!/usr/bin/env python3

import random

def check_option():
    
    options = ['paper', 'scissors', 'rock']
    chosen_option_pc = random.choice(options)
    chosen_option_user = input('Choose paper, scissors, or rock => ').lower()
    
    if chosen_option_user not in options:
        print('choose a valid option!')
        return None, None
        
    return chosen_option_pc, chosen_option_user

def rules(pc_option, user_option, computer_win, user_win):
  
    if user_option == pc_option:
        print('DRAW!')
        
    elif user_option == 'rock':
        if pc_option == 'scissors':
            user_win += 1
        elif pc_option == 'paper':
            computer_win += 1
    
    elif user_option == 'scissors':
        if pc_option == 'rock':
            computer_win += 1
        elif pc_option == 'paper':
            user_win += 1
            
    elif user_option == 'paper':
        if pc_option == 'scissors':
            computer_win += 1
        elif pc_option == 'rock':
            user_win += 1

    return computer_win, user_win
    

def run():
    
    computer_win = 0
    user_win = 0
    rounds = 1
    
    while True:
        
        print('*'*50)
        print(f'Round number {rounds}')
        
        
        print('computer_wins', computer_win)
        print('user_wins', user_win)
        rounds += 1
        
        
        pc, user = check_option()
        computer_win, user_win = rules(pc, user, computer_win, user_win)
        
        if computer_win == 2:
            print('COMPUTER WON!')
            break
        elif user_win == 2:
            print('YOU WON!')
            break
    
        print('*'*50)
        
if __name__ == '__main__':
    run()