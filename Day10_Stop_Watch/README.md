# Stopwatch in Python

A simple stopwatch with a graphical window, built with Python and tkinter.
I made this project to practice Python logic, so the code is kept short and easy to read.

## Features

- Start, Stop and Reset the stopwatch
- Resume from where you stopped (Stop does not reset the time)
- Lap button that saves lap times in a list
- Time shown in `MM:SS.hh` format (minutes, seconds, hundredths of a second)

## Requirements

- Python 3.x
- tkinter (it comes with Python, so nothing needs to be installed)

On some Linux systems tkinter is not included. If you get an error, install it with:

```
sudo apt install python3-tk
```

## How to Run

1. Download `stopwatch.py`
2. Open a terminal in the same folder
3. Run:

```
python stopwatch.py
```

(use `python3 stopwatch.py` on Mac or Linux if `python` does not work)

## How to Use

| Button | What it does |
|--------|--------------|
| Start  | Starts the stopwatch, or continues it after Stop |
| Stop   | Pauses the stopwatch |
| Lap    | Saves the current time in the lap list (only works while running) |
| Reset  | Sets the time back to zero and clears all laps |

## How the Logic Works

- **`running`** is a True/False variable that tells if the stopwatch is on.
- **`start_time`** stores the moment the stopwatch was started.
- **`elapsed`** stores the total seconds counted so far.

When Start is pressed, the program sets `start_time = time.time() - elapsed`.
Subtracting `elapsed` is what makes the stopwatch continue after a pause instead of starting from zero.

While running, `update_time()` calculates `elapsed = time.time() - start_time`, updates the label,
and then calls itself again after 10 milliseconds using `window.after()`.

`format_time()` changes the seconds into minutes, seconds and hundredths using `//` and `%`.

## Project Structure

```
stopwatch/
├── stopwatch.py
└── README.md
```

## Ideas to Improve It

- Add keyboard shortcuts (for example Space to start/stop)
- Save lap times to a text file
- Add a countdown timer mode
- Rewrite it using a class instead of global variables