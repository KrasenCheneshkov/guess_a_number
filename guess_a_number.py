import random
def game_head():
    print(f'{'=' * 25}')
    print('Welcome player!')
    print('In this game the computer has chosen a number and you have to guess it!')
    print(f'{'=' * 25}')

def number_guess(level: int):
    top_limit = 100 * level
    number_to_guess = random.randint(1, top_limit)

    while True:
        player_guess = int(input(f'Please enter your guess (1-{top_limit}): '))
        if number_to_guess == player_guess:
            break
        elif player_guess > number_to_guess:
            print('The correct number is LOWER than your guess.')
        elif player_guess < number_to_guess:
            print('The correct number is HIGHER than your guess.')

    print('Congratulations! Your guess was correct!')

def stay_in_game_question(answer) -> bool:
    if answer == 'Y':
        return True
    return False

def game_body():
    level = 1
    while True:
        print(f'=== LEVEL {level} ===')
        number_guess(level)
        print(f'{'=' * 15}\n')

        stay_in_game = input('Would you like to play the next level? (Y/N): ')
        if stay_in_game_question(stay_in_game):
            level += 1
            continue
        else:
            print('*** Thank you for playing! ***')
            print('*** BYE! ***')
            break
game_head()
game_body()

