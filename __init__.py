"""
__init__.py starts the game
"""
from os import system
from time import sleep
from utils.Stack import Stack

USER_DECISIONS = {}


def clear_screen():
    system('clear')

def welcome_screen():
    print("Welcome to Days in Our Lives")
    print("The objective of the game is simple, to stay healthy and to not die.")
    print("Press ^c to quit, and enter to continue")

def intro_game_prompt():
    prompt = ['I will ask you a few questions first. What is your name?', '']


def story_loop():
    user_input_stack = Stack()
    while True:
        clear_screen()
        welcome_screen()
        if len(input()) >= 0:
            break

        clear_screen()



story_loop()
