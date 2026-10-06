# simple banking program
# you can check your balance, deposit money, or withdraw money

def show_balance():
    print(f"Your balance is: ${balance}")

def deposit():
    amount = float(input("How much do you want to deposit? "))
    # no negative deposits, just give back 0 so the balance doesn't change
    if amount < 0:
        print("You can't deposit a negative amount.")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("How much do you want to withdraw? "))
    # check for a negative amount first, then check if there's enough money
    if amount < 0:
        print("You can't withdraw a negative amount.")
        return 0
    elif amount > balance:
        print("Not enough money in your account.")
        return 0
    else:
        return amount

def main():
    # balance is global so show_balance() and withdraw() can use it too
    global balance
    balance = 0
    is_running = True

    # keeps showing the menu until the user picks 4
    while is_running:
        print("Welcome to the Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Pick an option (1-4): ")
        if choice == '1':
            show_balance()
        elif choice == '2':
            amount = deposit()
            balance += amount
            print(f"You deposited ${amount}. Your balance is now ${balance}")
        elif choice == '3':
            amount = withdraw()
            balance -= amount
            print(f"You withdrew ${amount}. Your balance is now ${balance}")
        elif choice == '4':
            is_running = False
            print("Thanks for using the Banking Program, have a nice day!")
        else:
            print("That's not a valid option, try again.")

if __name__ == "__main__":
    main()