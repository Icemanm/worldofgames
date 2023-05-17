import MemoryGame, GuessGame, CurrencyRouletteGame, sys
from Utils import screen_cleaner
from Score import add_score


def welcome():
    name = input('What is your name? ')
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.\n")


def difficulty(chosen_difficulty=0):
    chosen_difficulty = input('Please choose a difficulty: from 1 to 5: \n')
    try:
        if 1 <= int(chosen_difficulty) <= 5:
            return chosen_difficulty
        else:
            return difficulty()
    except ValueError:
        print('\n Please Enter a number between 1 and 5')
        return difficulty()


def game_runner(game, chosen_difficulty):
    if int(game) == 1:
        result = MemoryGame.play(chosen_difficulty)
    elif int(game) == 2:
        result = GuessGame.play(chosen_difficulty)
    elif int(game) == 3:
        result = CurrencyRouletteGame.play(chosen_difficulty)
    else:
        print("Unknown game please try again")
    return result


def load_game(game=0, chosen_difficulty=0):
    print('''Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')
    game = input()
    if game.isdecimal():
        if 3 >= int(game) >= 1:
            chosen_difficulty = difficulty()
            print(f' the game you chose {game}\n the difficulty you chose {chosen_difficulty}')
            result = game_runner(game, chosen_difficulty)
            if result is True:
                add_score(chosen_difficulty)
            return result
        else:
            return starter()
    else:
        print('\n Please Enter a Only number ')
        return starter()


def end_game():
    print('Do you want to play again?')
    answer = input('Enter y \ n ')
    if answer.isalpha() == True:
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            screen_cleaner()
            return starter()
    else:
        print('that was fun! bye bye... hope to see you agine')
        sys.exit()


def starter():
    load_game()
    end_game()




