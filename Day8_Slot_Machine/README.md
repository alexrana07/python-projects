# Slot Machine

A simple slot machine game that runs in the terminal, written in Python.

## How to run

1. Make sure you have Python 3 installed
2. Open a terminal in the folder with the file
3. Run this:

```
python slot_machine.py
```

(On some computers you might need to type `python3` instead of `python`)

## How to play

- You start with $100
- Type in how much you want to bet and press enter
- The machine spins 3 reels
- Type `q` to quit anytime
- The game ends when you run out of money

## Rules

| Result | What happens |
|---|---|
| 3 symbols match | JACKPOT! You win 10x your bet |
| 2 symbols match | You get your bet back |
| No match | You lose your bet |

## Symbols

cherry, lemon, bell, star, seven

## Notes

- Only uses the `random` module that comes with Python, so there is nothing to install
- Bets have to be whole numbers (no decimals)

## Ideas to add later

- More symbols
- A "play again" option
- Different payouts for different symbols
- Save the high score