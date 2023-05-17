from py_currency_converter import convert
import random


def generate_random_number():
    random_num = random.randint(1, 100)
    return random_num


def get_money_interval(chosen_difficulty, random_num):
    ils = convert(base='USD', amount=1, to=['ILS'])['ILS']
    t = random_num * ils
    d = int(chosen_difficulty)
    interval = (t - (5 - d), t + (5 - d))
    return interval


def get_guess_from_user(random_num, interval):
    print(f'if you have {random_num} USD')
    guess = int(input("Guess what you thinks is the value in ILS (Shekel):\n "))
    try:
        if guess in range(int(interval[0]), int(interval[1])):
            print(f'you guessed it!')
            return True
        else:
            print(f'almost... maybe next time! \nThe right answer is in the rang(base on difficulty you choose)- {interval}')
            return False
    except ValueError:
        print(f'please enter a number')
        return get_guess_from_user(random_num, interval)


def play(chosen_difficulty):
    random_num = generate_random_number()
    interval = get_money_interval(chosen_difficulty, random_num)
    result = get_guess_from_user(random_num, interval)
    return result


