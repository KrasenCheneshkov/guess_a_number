import random

def guess_a_number(level: int) -> str:
    top_limit = 100 * level
    number_to_guess = random.randint(1, top_limit)
    while True:
        player_guess = int(input(f'Please enter your guess (1-{top_limit}): '))
        if number_to_guess == player_guess:
            break
        elif player_guess > number_to_guess:
            print('The correct number is lower than your guess.')
        elif player_guess < number_to_guess:
            print('The correct number is higher than your guess.')
    return 'Congratulations! Your guess was correct!'

def stay_in_game_question() -> bool:
    stay_in_game = input('Would you like to play the next level? (Y/N): ')
    if stay_in_game == 'Y':
        return True
    return False

def game_body():
    level = 1
    while True:
        print(f'=== LEVEL {level} ===')
        guess_a_number(level)
        print(f'{'=' * 15}\n')
        stay_in_game_question()
        if stay_in_game_question():
            level += 1
        else:
            print('*** Thank you for playing! ***')
            print('*** BYE! ***')
            break
print(f'{'=' * 25}')
print('Welcome player!')
print('In this game the computer has chosen a number and you have to guess it!')
print(f'{'=' * 25}')

game_body()