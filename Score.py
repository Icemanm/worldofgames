# The function’s input is a variable called difficulty. The function will try to read
# the current score in the scores file, if it fails it will create a new one and will use it to save
# the current score.

def add_score(difficulty):
    points_of_winning = (int(difficulty) * 3) + 5
    try:
        with open('score.txt', 'r') as file:
            content = file.read()
            accumulation = int(content) + points_of_winning
        with open('score.txt', 'w') as file:
            file.write(str(accumulation))
            # print('success update score to ' + str(accumulation))
    except:
        with open('score.txt', 'w') as file:
            file.write(str(points_of_winning))
            # print('create score file with score ' + str(points_of_winning))

