import random

# Keep track of the scores
user_wins = 0
computer_wins = 0

# All the choices in the game
options = ['rock','paper','scissors']

while True:
    # Ask the user for their choice (lower() and strip() clean up the input)
    user_input = input('Select rock/paper/scissors or q to quit: ').lower().strip()

    # If the user types q, show the final score and stop the game
    if user_input == 'q':
        print('Thank you for playing, your score is',user_wins ,'.')
        print('computer wins',computer_wins,'.')
        break

    # If the input is not a valid option, ask again
    if user_input not in options:
        print('select from options only')
        continue

    # Computer picks a random option (0, 1 or 2)
    random_index = random.randint(0,2)

    computer_pick = options[random_index]
    print('computer picked',computer_pick,'.')

    # Same choice means a draw
    if user_input == computer_pick:
        print('draw!')

    # All the ways the user can win
    elif user_input == 'rock' and computer_pick == 'scissors':
        print('you won!')
        user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock':
        print('you won!')
        user_wins += 1

    elif user_input == 'scissors' and computer_pick == 'paper':
        print('you won!')
        user_wins += 1

    # Anything else means the computer wins
    else:
        print('you lost!')
        computer_wins += 1