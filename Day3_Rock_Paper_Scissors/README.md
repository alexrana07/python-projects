# Rock Paper Scissors

**Day 3 of my 10 Days of Python Projects**

A simple command-line Rock Paper Scissors game written in Python. You play against the computer, and the game keeps track of both scores.

## What I Practiced

- `while` loops and `break` / `continue`
- `if` / `elif` / `else` conditions
- Taking user input and cleaning it with `.lower()` and `.strip()`
- Using the `random` module
- Keeping score with variables

## Features

- Play as many rounds as you like
- Computer picks its move randomly
- Handles draws, wins, and losses
- Keeps a running score for you and the computer
- Ignores extra spaces and capital letters in your input (`Rock`, ` paper `, etc. all work)
- Asks again if you type something invalid

## Requirements

- Python 3.x

No extra libraries needed. The game only uses Python's built-in `random` module.

## How to Run

1. Save the code in a file, for example `rock_paper_scissors.py`
2. Open a terminal in the folder where the file is saved
3. Run:

```bash
python rock_paper_scissors.py
```

On some systems you may need to use `python3` instead of `python`.

## How to Play

1. Type `rock`, `paper`, or `scissors` and press Enter
2. The computer picks its move and the result is shown
3. Type `q` at any time to quit and see the final score

## Rules

- Rock beats scissors
- Scissors beats paper
- Paper beats rock
- Same choice from both players is a draw (nobody gets a point)

## Example

```
Select rock/paper/scissors or q to quit: rock
computer picked scissors .
you won!
Select rock/paper/scissors or q to quit: paper
computer picked paper .
draw!
Select rock/paper/scissors or q to quit: q
Thank you for playing, your score is 1 .
computer wins 0 .
```

## Ideas for Improvement

- Add a draw counter
- Add a "best of 5" mode
- Show the score after every round
- Simplify the win checks with a dictionary
