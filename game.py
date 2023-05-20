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
    while True:
        pass

if __name__ == '__main__':
    run()