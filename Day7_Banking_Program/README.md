# Banking Program

A simple banking program that runs in the terminal, written in Python. You can check your balance, deposit money, and withdraw money.

This is **project 7 of my 10 Python projects**.

## What it does

- Shows your current balance
- Lets you deposit money
- Lets you withdraw money
- Stops you from depositing or withdrawing a negative amount
- Stops you from withdrawing more than you have
- Keeps running until you choose to exit

## How to run it

You need Python 3 installed (any version that supports f-strings, so 3.6 or newer).

1. Download or clone this project
2. Open a terminal in the project folder
3. Run:

```
python banking.py
```

(On some computers you may need to type `python3 banking.py` instead.)

## Example

```
Welcome to the Banking Program
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
Pick an option (1-4): 2
How much do you want to deposit? 100
You deposited $100.0. Your balance is now $100.0
Welcome to the Banking Program
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
Pick an option (1-4): 3
How much do you want to withdraw? 30
You withdrew $30.0. Your balance is now $70.0
```

## How the code works

| Function | What it does |
|----------|--------------|
| `show_balance()` | Prints the current balance |
| `deposit()` | Asks how much to deposit and returns the amount (or 0 if it's negative) |
| `withdraw()` | Asks how much to withdraw and returns the amount (or 0 if it's negative or more than the balance) |
| `main()` | Runs the menu loop and updates the balance |

The balance is stored in a global variable so all the functions can use it. The menu keeps looping until the user picks option 4.

## What I learned

- How to write and call my own functions
- Using `return` to send a value back from a function
- Using a `while` loop to keep a program running
- Using `if / elif / else` to handle different choices
- Using a global variable
- Putting the main code inside `main()` and using `if __name__ == "__main__":`

## Known issues

- If you type letters instead of a number when entering an amount, the program crashes (I haven't added error handling yet)
- After a failed withdrawal, it still prints "You withdrew $0" right after the error message
- The balance is not saved, so it goes back to 0 every time you run the program

## Ideas for later

- Add `try / except` so typing something wrong doesn't crash the program
- Save the balance in a file so it's still there next time
- Add a PIN or login
- Keep a list of past transactions
- Format money to 2 decimal places (like $70.00)