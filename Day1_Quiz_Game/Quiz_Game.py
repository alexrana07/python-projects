print('Welcome to my computer quiz game!')

playing = input('Do you want to play? y/n: ').lower()
score = 0

if playing != 'y':
    quit()

print("Let's start the game!\n")

# Question 1
question_1 = input('What does CPU stand for? ').lower()
answer = 'central processing unit'

if question_1 == answer:
    print('Correct! +1 score')
    score += 1
else:
    print('Incorrect!')

# Question 2
question_2 = input('What does RAM stand for? ').lower()
answer = 'random access memory'

if question_2 == answer:
    print('Correct! +1 score')
    score += 1
else:
    print('Incorrect!')

# Question 3
question_3 = input('What does ROM stand for? ').lower()
answer = 'read only memory'

if question_3 == answer:
    print('Correct! +1 score')
    score += 1
else:
    print('Incorrect!')

# Question 4
question_4 = input('What does HTML stand for? ').lower()
answer = 'hypertext markup language'

if question_4 == answer:
    print('Correct! +1 score')
    score += 1
else:
    print('Incorrect!')

# Question 5
question_5 = input('What does URL stand for? ').lower()
answer = 'uniform resource locator'

if question_5 == answer:
    print('Correct! +1 score')
    score += 1
else:
    print('Incorrect!')

# Show the final result
print(f'\nYour final score is: {score}/5')

if score >= 3:
    print('Congratulations! You passed the quiz.')
else:
    print('You need some improvement. Keep practicing!')

