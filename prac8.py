import random

def welcome():
    print("====================================")
    print("     Welcome to the Guess Game!")
    print(" Try to guess the number (1 to 100)")
    print("====================================")
def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    score = 100

