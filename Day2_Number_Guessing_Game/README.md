# 🎯 Number Guessing Game

**Day 2 of my 21-day Python project series.**

A simple command-line game. You choose the biggest number you want to play with, the computer picks a secret number between 0 and that number, and you try to guess it. Every correct guess gives you one point.

It's a small project, but it's a good one if you just finished a Python tutorial and want to build something real.

---

## How it works

1. Enter the maximum number (for example `10`)
2. The computer secretly picks a random number between 0 and 10
3. You guess the number
4. Right guess = +1 point. Wrong guess = the game shows you the real number
5. The game keeps going until you type `q`

If you type something that isn't a number (or a number that's 0 or below), the game asks again instead of crashing.

---

## Example

```
Enter max number (q to quit): 10
Guess the number between 0 and 10: 7
❌ Wrong! The number was 3
Score: 0

Enter max number (q to quit): 5
Guess the number between 0 and 5: 2
🎉 Correct! You got it
Score: 1

Enter max number (q to quit): q
Your final score is 1
```

---

## How to run it

You need Python 3 installed.

```bash
python guessing_game.py
```

On Mac or Linux you might need `python3` instead:

```bash
python3 guessing_game.py
```

---

## What you'll practice

- `while` loops
- `if / elif / else`
- Taking user input with `input()`
- Checking input with `.isdigit()`
- Using `continue` and `break`
- The `random` module
- Keeping a score with a variable

---

## Ideas to make it your own

- Give hints like "too high" or "too low"
- Limit the number of attempts
- Let the user guess more than once per secret number
- Save a high score to a file

---

## About this series

I'm building one Python project every day for 33 days. Each one is beginner-friendly, so if you're just starting out, follow along and build them with me.

⭐ If this helped you, star the repo.
