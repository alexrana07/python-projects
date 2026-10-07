import random

# my slot machine game
# you start with $100

money = 100
fruits = ["cherry", "lemon", "bell", "star", "seven"]

print("=== SLOT MACHINE ===")
print("you have $100 to start")

while True:
    print()
    print("money:", money)

    # check if the player is broke
    if money <= 0:
        print("you ran out of money :(")
        print("game over")
        break

    bet = input("bet how much? (q = quit) ")

    if bet == "q" or bet == "Q":
        print("ok bye, you leave with $" + str(money))
        break

    # make sure its a number
    if bet.isdigit() == False:
        print("thats not a number")
        continue

    bet = int(bet)

    if bet < 1:
        print("bet has to be at least 1")
        continue
    if bet > money:
        print("you dont have that much")
        continue

    money = money - bet

    # spin the reels
    one = random.choice(fruits)
    two = random.choice(fruits)
    three = random.choice(fruits)

    print()
    print(one, "|", two, "|", three)
    print()

    # check if they won
    if one == two and two == three:
        print("JACKPOT!!!")
        winnings = bet * 10
        money = money + winnings
        print("you won $" + str(winnings))
    elif one == two or two == three or one == three:
        print("2 match, you get your bet back")
        money = money + bet
    else:
        print("no match")
        print("you lost $" + str(bet))