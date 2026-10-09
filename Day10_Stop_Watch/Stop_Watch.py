import tkinter as tk
import time

# these variables keep track of the stopwatch
running = False
start_time = 0
elapsed = 0  # total seconds counted so far


def format_time(seconds):
    # converts seconds into MM:SS.hh format
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    hundredths = int((seconds * 100) % 100)
    return f"{minutes:02}:{secs:02}.{hundredths:02}"


def update_time():
    global elapsed
    if running:
        elapsed = time.time() - start_time
        time_label.config(text=format_time(elapsed))
        # call this function again after 10 milliseconds
        window.after(10, update_time)


def start():
    global running, start_time
    if not running:
        running = True
        # subtract elapsed so it continues from where we stopped
        start_time = time.time() - elapsed
        update_time()


def stop():
    global running
    running = False


def reset():
    global running, elapsed
    running = False
    elapsed = 0
    time_label.config(text=format_time(0))
    lap_list.delete(0, tk.END)


def lap():
    if running:
        lap_number = lap_list.size() + 1
        lap_list.insert(tk.END, f"Lap {lap_number}:  {format_time(elapsed)}")


# ---------- UI part ----------
window = tk.Tk()
window.title("Stopwatch")
window.geometry("300x380")

time_label = tk.Label(window, text="00:00.00", font=("Arial", 36))
time_label.pack(pady=20)

button_frame = tk.Frame(window)
button_frame.pack()

start_button = tk.Button(button_frame, text="Start", width=8, command=start)
start_button.grid(row=0, column=0, padx=5, pady=5)

stop_button = tk.Button(button_frame, text="Stop", width=8, command=stop)
stop_button.grid(row=0, column=1, padx=5, pady=5)

lap_button = tk.Button(button_frame, text="Lap", width=8, command=lap)
lap_button.grid(row=1, column=0, padx=5, pady=5)

reset_button = tk.Button(button_frame, text="Reset", width=8, command=reset)
reset_button.grid(row=1, column=1, padx=5, pady=5)

lap_list = tk.Listbox(window, width=30, height=8, font=("Arial", 12))
lap_list.pack(pady=15)

window.mainloop()