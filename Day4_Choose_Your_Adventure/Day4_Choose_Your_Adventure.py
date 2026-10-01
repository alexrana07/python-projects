# my text adventure game (project 4 of 33)

# get the name
name = input("type your name: ")
print("welcome", name, "to this adventure!")

# first choice. lower() so it doesn't matter if they type capitals
answer = input("you are on a dirt road, it has come to an end and you can go left or right. which way would you like to go? ").lower()

if answer == "left":
    # left path - river
    answer = input("you come to a river, you can walk around it or swim across. type walk to walk around or swim to swim across: ").lower()
    if answer == "swim":
        print("you swam across and were eaten by an alligator. you lose.")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game.")
    else:
        # they typed something else
        print("that's not an option. you lose.")

elif answer == "right":
    # right path - bridge
    answer = input("you come to a bridge, it looks wobbly. do you want to cross it or head back? type cross to cross it or back to go back: ").lower()
    if answer == "back":
        print("you go back and lose.")
    elif answer == "cross":
        # only get here if they crossed the bridge
        answer = input("you cross the bridge and meet a stranger. do you talk to them or ignore them? type talk to talk or ignore to ignore: ").lower()
        if answer == "talk":
            # the only way to win
            print("you talk to the stranger and they give you gold. you win!")
        elif answer == "ignore":
            print("you ignore the stranger and they are offended. you lose.")
        else:
            print("that's not an option. you lose.")
    else:
        print("that's not an option. you lose.")

else:
    # didn't type left or right
    print("that's not an option. you lose.")