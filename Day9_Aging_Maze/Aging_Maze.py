# aging maze - window version (uses tkinter, comes with python)
# every step makes you 1 year older, get to the gold square before you hit 90
# move with arrow keys or w a s d. space = next level / try again, r = restart

import random
import tkinter as tk

MAX_AGE = 90
ELIXIR_YEARS = 6
WIDTH = 800
HEIGHT = 540

# colors for each life stage
STAGE_COLORS = {
    "Child": "#ffd166",
    "Teen": "#4cc9f0",
    "Adult": "#80ed99",
    "Elder": "#c8b6ff",
}


def get_stage(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teen"
    elif age < 60:
        return "Adult"
    else:
        return "Elder"


def sight(age):
    # how far you can see, gets worse when you're old
    if age < 13:
        return 4
    elif age < 20:
        return 6
    elif age < 60:
        return 5
    else:
        s = 5 - (age - 60) // 10
        if s < 2:
            s = 2
        return s


def make_maze(width, height):
    # 1 = wall, 0 = open
    w = width * 2 + 1
    h = height * 2 + 1
    maze = []
    for i in range(h):
        maze.append([1] * w)

    # start at 1,1 and carve paths (depth first)
    maze[1][1] = 0
    stack = [(1, 1)]
    while len(stack) > 0:
        x, y = stack[-1]
        neighbors = []
        for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
            nx = x + dx
            ny = y + dy
            if nx > 0 and nx < w - 1 and ny > 0 and ny < h - 1:
                if maze[ny][nx] == 1:
                    neighbors.append((nx, ny))

        if len(neighbors) == 0:
            stack.pop()
        else:
            nx, ny = random.choice(neighbors)
            # knock down the wall in between
            maze[(y + ny) // 2][(x + nx) // 2] = 0
            maze[ny][nx] = 0
            stack.append((nx, ny))
    return maze


# ---------- game state (just globals, keeping it simple) ----------
maze = []
px = 1
py = 1
exit_x = 0
exit_y = 0
age = 5
level = 1
score = 0
best = 0
elixirs = []
seen = set()
state = "play"  # play, won or dead
message = ""


def new_level():
    global maze, px, py, exit_x, exit_y, age, elixirs, seen, state, message

    # maze gets bigger each level (but not forever)
    width = min(8 + (level - 1) * 2, 20)
    height = min(5 + (level - 1), 10)
    maze = make_maze(width, height)
    h = len(maze)
    w = len(maze[0])

    px = 1
    py = 1
    exit_x = w - 2
    exit_y = h - 2
    age = 5
    seen = set()
    state = "play"
    message = "Find the gold square! Grab the blue diamonds to get younger."

    # scatter some elixirs, not too close to the start
    elixirs = []
    while len(elixirs) < min(3 + level, 10):
        x = random.randint(1, w - 2)
        y = random.randint(1, h - 2)
        if maze[y][x] == 0 and (x + y) > 8 and (x, y) != (exit_x, exit_y) and (x, y) not in elixirs:
            elixirs.append((x, y))

    update_seen()
    draw()


def update_seen():
    r = sight(age)
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if (x - px) ** 2 + (y - py) ** 2 <= r * r:
                seen.add((x, y))


def move(dx, dy):
    global px, py, age, score, best, state, message

    nx = px + dx
    ny = py + dy

    if maze[ny][nx] == 1:
        message = "Bonk! That's a wall."
        draw()
        return

    px = nx
    py = ny
    age += 1
    message = ""

    if (px, py) in elixirs:
        elixirs.remove((px, py))
        age -= ELIXIR_YEARS
        if age < 0:
            age = 0
        message = "Elixir! You feel " + str(ELIXIR_YEARS) + " years younger."

    if px == exit_x and py == exit_y:
        score += 100 + (MAX_AGE - age) * 10
        if score > best:
            best = score
        state = "won"
    elif age >= MAX_AGE:
        if score > best:
            best = score
        state = "dead"

    update_seen()
    draw()


def draw():
    canvas.delete("all")
    h = len(maze)
    w = len(maze[0])
    cell = min(WIDTH // w, HEIGHT // h)
    ox = (WIDTH - cell * w) // 2
    oy = (HEIGHT - cell * h) // 2
    r = sight(age)
    stage = get_stage(age)

    # tiles we've seen (bright if we can see them right now, dim if remembered)
    for (x, y) in seen:
        visible = ((x - px) ** 2 + (y - py) ** 2) <= r * r
        if maze[y][x] == 1:
            if visible:
                color = "#6c74c9"
            else:
                color = "#2b2f55"
        else:
            if visible:
                color = "#242a4d"
            else:
                color = "#0f1226"
        x1 = ox + x * cell
        y1 = oy + y * cell
        canvas.create_rectangle(x1, y1, x1 + cell, y1 + cell, fill=color, outline="")

    # exit
    if (exit_x, exit_y) in seen:
        x1 = ox + exit_x * cell
        y1 = oy + exit_y * cell
        canvas.create_rectangle(x1 + 2, y1 + 2, x1 + cell - 2, y1 + cell - 2, fill="#ffd700", outline="white")

    # elixirs
    for (x, y) in elixirs:
        if (x, y) in seen:
            x1 = ox + x * cell
            y1 = oy + y * cell
            m = cell // 2
            s = cell // 3
            canvas.create_polygon(x1 + m, y1 + m - s, x1 + m + s, y1 + m, x1 + m, y1 + m + s, x1 + m - s, y1 + m,
                                  fill="#7df9ff", outline="white")

    # the player, gets a little smaller as a kid and a cane when old
    x1 = ox + px * cell
    y1 = oy + py * cell
    pad = cell // 5
    if stage == "Child":
        pad = cell // 3
    if stage == "Elder":
        canvas.create_line(x1 + cell - pad, y1 + cell // 2, x1 + cell - pad + 3, y1 + cell - 2, fill="#c9a66b", width=2)
    canvas.create_oval(x1 + pad, y1 + pad, x1 + cell - pad, y1 + cell - pad, fill=STAGE_COLORS[stage], outline="white")

    # top info text
    info.config(text="Age " + str(age) + " (" + stage + ")     Sight " + str(r) +
                     "     Level " + str(level) + "     Score " + str(score) + "     Best " + str(best),
                fg=STAGE_COLORS[stage])

    # age bar
    bar.delete("all")
    bar.create_rectangle(0, 0, WIDTH, 14, fill="#1a1d3a", outline="")
    bar.create_rectangle(0, 0, WIDTH * age // MAX_AGE, 14, fill=STAGE_COLORS[stage], outline="")

    # bottom message
    msg.config(text=message)

    if state == "won":
        popup("YOU ESCAPED!", "Aged " + str(age) + ", score " + str(score), "Press SPACE for the next level", "#ffd166")
    elif state == "dead":
        popup("YOU DIED OF OLD AGE", "Level " + str(level) + ", score " + str(score), "Press SPACE to try again", "#ff6b6b")


def popup(title, line1, line2, color):
    canvas.create_rectangle(180, 170, WIDTH - 180, 370, fill="#0b0d1f", outline=color, width=3)
    canvas.create_text(WIDTH // 2, 215, text=title, fill=color, font=("Arial", 24, "bold"))
    canvas.create_text(WIDTH // 2, 275, text=line1, fill="white", font=("Arial", 14))
    canvas.create_text(WIDTH // 2, 330, text=line2, fill="white", font=("Arial", 13))


def key_press(event):
    global level, score

    k = event.keysym.lower()

    if k == "r":
        level = 1
        score = 0
        new_level()
        return

    if state == "play":
        if k == "up" or k == "w":
            move(0, -1)
        elif k == "down" or k == "s":
            move(0, 1)
        elif k == "left" or k == "a":
            move(-1, 0)
        elif k == "right" or k == "d":
            move(1, 0)
    else:
        if k == "space" or k == "return":
            if state == "won":
                level += 1
            else:
                level = 1
                score = 0
            new_level()


# ---------- build the window ----------
root = tk.Tk()
root.title("Aging Maze")
root.configure(bg="#0b0d1f")
root.resizable(False, False)

info = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#0b0d1f", pady=6)
info.pack()

bar = tk.Canvas(root, width=WIDTH, height=14, bg="#0b0d1f", highlightthickness=0)
bar.pack()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#05060f", highlightthickness=0)
canvas.pack()

msg = tk.Label(root, text="", font=("Arial", 12), fg="#e8eaff", bg="#0b0d1f", pady=6)
msg.pack()

hint = tk.Label(root, text="Arrow keys / WASD to move  |  R = restart", font=("Arial", 10),
                fg="#777b9c", bg="#0b0d1f", pady=4)
hint.pack()

root.bind("<Key>", key_press)

new_level()
root.mainloop()