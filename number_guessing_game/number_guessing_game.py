import random

score = 0

while True:
    # Ask the user to enter the maximum number
    guess_number = input('guess the number')

    # Check if the input contains only a valid number
    if guess_number.lstrip('-').isdigit():
        guess_number = int(guess_number)

        # Make sure the number is greater than 0
        if guess_number <= 0:
            print('select number greather than 0')
            continue

    # If the input is not a number
    else:
        print('seleect number only')
        continue

    # Generate a random number between 0 and the user's number
    random_number = random.randrange(0, guess_number + 1)

    # Increase the score after a valid number is entered
    score += 1

    # Display the generated random number
    print(random_number)

    # Display the current score
    print('\n', score)