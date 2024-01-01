import random
import time

words = ["apple", "banana", "orange", "grape", "watermelon", "strawberry", "blueberry", "kiwi", "pineapple"]

def display_word():
    return random.choice(words)

def play_ztype():
    print("Welcome to ZType - Typing Game!")
    print("Type the words that appear as fast as you can to destroy them.")

    score = 0

    while True:
        word = display_word()
        print(f"Type the word: {word}")
        
        start_time = time.time()
        user_input = input().lower().strip()
        end_time = time.time()

        if user_input == word:
            elapsed_time = end_time - start_time
            score += max(1, int(10 - elapsed_time))
            print(f"Correct! Your score: {score}")
        else:
            print("Incorrect! Game Over.")
            break

play_ztype()
