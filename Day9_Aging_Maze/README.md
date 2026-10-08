# 🧓 Aging Maze

**Project 9 of 10** in my personal coding project challenge.

A fun Python maze game where **every step makes you one year older**. Your goal is to navigate through the maze, collect magical elixirs to become younger, and reach the golden exit **before reaching age 90**.

## 🎮 How to Play

- Use **Arrow Keys** or **W A S D** to move.
- Every step increases your age by **1 year**.
- Find the **gold square** to escape the maze.
- Collect **blue diamonds 💎** to become **6 years younger**.
- Your vision/sight changes as you age.
- If you reach **90 years old before escaping, you lose**.
- Press **SPACE** after winning to move to the next level.
- Press **SPACE** after losing to try again.
- Press **R** anytime to restart from Level 1.

## 🧠 Game Features

- Randomly generated mazes
- Increasing maze difficulty
- Age-based life stages:
  - 👶 Child
  - 🧑 Teen
  - 🧑‍💼 Adult
  - 👴 Elder
- Limited vision that becomes worse with age
- Age-reducing elixirs
- Score and best score system
- Multiple levels
- Fog-of-war exploration system
- Keyboard controls
- Tkinter graphical interface

## 🛠️ Technologies Used

- **Python**
- **Tkinter** — for the graphical user interface
- **Random** — for procedural maze generation

Tkinter comes included with standard Python installations, so no external GUI library is required.

## ▶️ How to Run

Make sure Python is installed on your computer.

Then run:

```bash
python aging_maze.py
```

The game window should open automatically.

## 🎯 Scoring

You receive points when you escape the maze.

The score is based on:

- Successfully reaching the exit
- How young you are when you escape

The younger you are when you reach the gold square, the higher your score.

## 🧩 How the Maze Works

The maze is generated randomly using a **Depth-First Search (DFS)** maze-generation algorithm.

Each level becomes larger, making it harder to find the exit before your age reaches 90.

## 🤖 AI Assistance

I built this project as part of my **10-project coding challenge**.

I also took help from **Claude** while developing the **Tkinter UI and game interface**. I used AI as a development assistant to help with ideas, implementation, and improving the interface, while understanding and working with the code myself.

## 📚 What I Learned

Through this project, I practiced:

- Python functions and variables
- Tkinter GUI programming
- Keyboard event handling
- Random maze generation
- Game state management
- Collision detection
- Score systems
- Procedural generation
- Working with multiple levels
- Using AI tools as a programming assistant

## 🚀 Project Progress

**Project 9 / 10** ✅

One more project to complete my 10-project challenge!

---

Made with **Python 🐍 + Tkinter + a little AI assistance 🤖**