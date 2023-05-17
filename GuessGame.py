import random


def generate_number(chosen_difficulty, secret_number=0):
    secret_number = random.randint(1, int(chosen_difficulty))
    return secret_number


def get_guess_from_user(chosen_difficulty, guess=0):
    guess = input(f'Guess a number between 1 and {chosen_difficulty}: ')
    if 1 <= int(guess) <= int(chosen_difficulty):
        return guess
    else:
        print('Please enter a number between 1 and', chosen_difficulty)
        return get_guess_from_user(chosen_difficulty)


def compare_results(secret_number, guess):
    if int(guess) == int(secret_number):
        print(f'You guessed {guess} and its the right number! ')
        return True
    else:
        print(f'You guessed the number in {guess}, but it was {secret_number}.')
        return False


def play(chosen_difficulty):
    secret_number = int(generate_number(chosen_difficulty))
    guess = get_guess_from_user(chosen_difficulty)
    result = compare_results(secret_number, guess)
    return result



