# Text Adventure Game

**Project 4 of 33**

A simple text-based adventure game written in Python. You type your name, then make choices that decide whether you win or lose.

## How to Run

1. Make sure you have Python 3 installed.
2. Save the code as `adventure.py`.
3. Open a terminal in the same folder and run:

```
python adventure.py
```

No extra libraries are needed.

## How to Play

The game asks you questions and you type your answer. Answers are not case-sensitive, so `Left` and `left` both work.

| Choice | Options |
|--------|---------|
| Dirt road | `left` or `right` |
| River (left path) | `walk` or `swim` |
| Bridge (right path) | `cross` or `back` |
| Stranger (after the bridge) | `talk` or `ignore` |

If you type something that is not an option, the game tells you and you lose.

## Story Paths

- **Left, then swim:** you get eaten by an alligator (lose)
- **Left, then walk:** you run out of water (lose)
- **Right, then back:** you turn around (lose)
- **Right, then cross, then ignore:** the stranger is offended (lose)
- **Right, then cross, then talk:** the stranger gives you gold (**win**)

There is only one winning path, so try to find it!

## What I Practiced

- Using `input()` and `print()`
- Using `.lower()` to handle capital letters
- `if`, `elif`, and `else` statements
- Nested `if` statements for choices inside choices

## Ideas for the Future

- Add more paths and endings
- Add an inventory (for example, a map from the stranger)
- Let the player play again without restarting the program