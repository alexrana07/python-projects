# 🎲 Pig Dice Game

A simple multiplayer dice game for the terminal, written in Python.

> **Project 6 of 33** — part of my challenge to build 33 projects.

## How the game works

This is a version of the classic dice game *Pig*. Two to four players take turns, and the first one to reach **100 points** wins.

On your turn you can keep rolling a single die as many times as you like:

- Roll a **2-6** and that number gets added to your turn score.
- Roll a **1** and you lose everything you've scored *this turn*, and it's the next player's go.
- Stop whenever you want by typing `n`, and your turn score gets added to your total.

So the question is always: do you roll again and risk it, or bank your points while you can? If a roll takes you to 100 or more, the turn ends automatically and you win.

## How to run it

You only need Python 3.6 or newer. There's nothing to install.

```bash
python pig_game.py
```

On some systems you might need `python3` instead of `python`.

## Example

```
How many players? (2-4): 2

--- Player 1's turn (total: 0) ---
Roll? (y/n): y
You rolled a 4
Turn score so far: 4
Roll? (y/n): y
You rolled a 6
Turn score so far: 10
Roll? (y/n): n
You banked 10. Total: 10

--- Player 2's turn (total: 0) ---
Roll? (y/n): y
You rolled a 1
Ouch, a 1. You lose everything from this turn.
You banked 0. Total: 0
```

## What I practiced

- `while` and `for` loops (and nesting them)
- Taking user input and validating it with `try/except`
- Working with lists to keep track of each player's score
- Using the `random` module
- f-strings for cleaner output
- Breaking out of loops at the right moment

## Ideas for later

- Let players enter their names instead of using "Player 1", "Player 2"
- Add a computer opponent
- Make the target score adjustable
- Add a "play again?" option at the end

## Files

| File | What it is |
| --- | --- |
| `pig_game.py` | The whole game |
| `README.md` | This file |