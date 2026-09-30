import random

score = 0

while True:
    # ask for the max number
    max_number = input('Enter max number (q to quit): ')

    # quit the game
    if max_number == 'q':
        print('Your final score is', score)
        break

    # check if its a number
    if max_number.isdigit():
        max_number = int(max_number)

        # number must be more than 0
        if max_number <= 0:
            print('Number must be greater than 0')
            continue

    else:
        print('Numbers only please')
        continue

    # computer picks a secret number
    random_number = random.randint(0, max_number)

    # user guesses
    user_guess = input('Guess the number between 0 and ' + str(max_number) + ': ')

    if not user_guess.isdigit():
        print('Numbers only please')
        continue

    user_guess = int(user_guess)

    # check the guess
    if user_guess == random_number:
        print('🎉 Correct! You got it')
        score += 1
    else:
        print('❌ Wrong! The number was', random_number)

    print('Score:', score)
    print()