# 🐍 Computer Quiz Game

A simple **command-line quiz game built with Python**.

This is **Project 1 of my 21 Python Projects series**, where each project focuses on applying Python concepts through small, practical programs.

For this project, the main focus is **conditional statements (`if` and `else`)**.

---

## 📌 About

The Computer Quiz Game asks the player five basic computer-related questions.

For every correct answer, the player gets **1 point**. At the end of the quiz, the program displays the final score and tells the player whether they passed.

The project was intentionally kept simple to focus on understanding how **conditions can be used to make decisions in a program**.

---

## 🎯 Concepts Used

* `if` / `else` statements
* `input()`
* Variables
* String comparison
* `.lower()`
* Score tracking
* Basic program flow

---

## 🎮 How It Works

The program first asks whether the player wants to play.

If the player enters `y`, the quiz starts.

Each question follows the same basic logic:

```text
Ask a question
      ↓
Get the user's answer
      ↓
Compare with the correct answer
      ↓
   Correct?
   ↙     ↘
 Yes      No
  ↓        ↓
+1 score  No score
```

After all five questions, the final score is displayed.

A score of **3 or more** is considered a passing score.

---

## 💻 Example

```text
Welcome to my computer quiz game!

Do you want to play? y/n: y

Let's start the game!

What does CPU stand for? central processing unit
Correct! +1 score

What does RAM stand for? random access memory
Correct! +1 score

What does ROM stand for? random access memory
Incorrect!

...

Your final score is: 4/5
Congratulations! You passed the quiz.
```

---

## ▶️ How to Run

Make sure **Python 3** is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/your-username/python-projects.git
```

Go to the project directory:

```bash
cd python-projects/01-computer-quiz
```

Run the program:

```bash
python computer_quiz.py
```

---

## 🚀 Project Series

This is **Project 1 of 33** in my Python Projects series.

The projects will gradually introduce more Python concepts and build towards more practical programs.

**Progress:** `1 / 33` ✅

---

## 📝 Note

This project was created as a practical exercise for **conditional statements** and basic Python programming.

More projects coming soon.
