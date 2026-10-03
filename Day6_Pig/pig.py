import random


def roll():
    return random.randint(1, 6)


# ask how many people are playing
while True:
    try:
        num_players = int(input("How many players? (2-4): "))
    except ValueError:
        print("That's not a number, try again.")
        continue

    if 2 <= num_players <= 4:
        break
    print("Pick a number between 2 and 4.")

target = 100
scores = [0] * num_players
winner = None

while winner is None:
    for p in range(num_players):
        print(f"\n--- Player {p + 1}'s turn (total: {scores[p]}) ---")

        turn_score = 0

        while True:
            choice = input("Roll? (y/n): ").strip().lower()

            if choice == "n":
                break
            if choice != "y":
                print("Just y or n please.")
                continue

            value = roll()
            print("You rolled a", value)

            if value == 1:
                print("Ouch, a 1. You lose everything from this turn.")
                turn_score = 0
                break

            turn_score += value
            print("Turn score so far:", turn_score)

            # no point rolling again if this already wins it
            if scores[p] + turn_score >= target:
                break

        scores[p] += turn_score
        print(f"You banked {turn_score}. Total: {scores[p]}")

        if scores[p] >= target:
            winner = p
            break

print(f"\n🎉 Player {winner + 1} wins!")

print("\nFinal scores:")
for i, s in enumerate(scores):
    print(f"Player {i + 1}: {s}")
    