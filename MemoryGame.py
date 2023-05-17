import random
import os
import time


def generate_sequence(chosen_difficulty):
    sequence = []
    for i in range(int(chosen_difficulty)):
        sequence.append(random.randint(1, 101))
    return sequence


def get_list_from_user():
    # list_of_numbers = []
    while True:
        try:
            list_of_numbers = list(map(int, input("Enter a list of numbers separated by a comma: ").split(',')))
            break
        except ValueError:
            print("Please enter a list of numbers separated by a comma.")
    return list_of_numbers


def is_list_equal(sequence, list_of_numbers):
    if sequence == list_of_numbers:
        return True
    else:
        return False


def play(chosen_difficulty):
    sequence = generate_sequence(chosen_difficulty)
    print(sequence, end='')
    time.sleep(0.7)
    print('', end='\r')
    time.sleep(0.7)
    # os.system('cls' if os.name == 'nt' else 'clear')
    list_of_numbers = get_list_from_user()
    if is_list_equal(sequence, list_of_numbers) is True:
        print("You won!")
        return True
    else:
        print("You lost!")
        return False


