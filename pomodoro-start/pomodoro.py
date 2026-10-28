from tkinter import *
from pathlib import Path
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#cbdfbd"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TEXT_COLOR = "#343a40"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
COLORS = [PINK, RED, GREEN, YELLOW]
repetitions = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global repetitions, timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmark_label.config(text="")
    repetitions = 0
    start_btn.config(state=NORMAL)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repetitions, timer
    if timer is not None:
        return

    repetitions += 1
    start_btn.config(state=DISABLED)

    if repetitions % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break")
    elif repetitions % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text="Short Break")
    else:
        countdown(WORK_MIN * 60)
        title_label.config(text="Work")
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global repetitions, timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        timer = None
        start_timer()
        marks = ""
        for _ in range(repetitions // 2):
            marks += "✔"
        checkmark_label.config(text=marks)

# ---------------------------- COLOR SWAP ------------------------------- #
# Color change button
def change_color():
    current_color = window.cget("bg")
    next_color = COLORS[(COLORS.index(current_color) + 1) % len(COLORS)]
    window.config(bg=next_color)
    header_frame.config(bg=next_color)
    canvas.config(bg=next_color)
    title_label.config(bg=next_color)
    subtitle_label.config(bg=next_color)
    controls_frame.config(bg=next_color)
    color_btn.config(bg=next_color)
    start_btn.config(bg=next_color, activebackground=next_color)
    reset_btn.config(bg=next_color, activebackground=next_color)
    checkmark_label.config(bg=next_color)
        
# ---------------------------- UI SETUP ------------------------------- #

bg_color = YELLOW
asset_dir = Path(__file__).resolve().parent
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=30, bg=bg_color)
window.resizable(False, False)

# Header
header_frame = Frame(window, bg=bg_color)
header_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

# Title Label
title_label = Label(
    header_frame,
    text="Timer",
    fg=TEXT_COLOR,
    bg=bg_color,
    font=(FONT_NAME, 36, "bold"),
)
title_label.grid(row=0, column=1, pady=(0, 2))

# Color Change Button
button_icon = PhotoImage(file=asset_dir / "palette.png")
color_btn = Button(
    highlightthickness=0,
    command=change_color,
    bg=bg_color,
    activebackground=bg_color,
    image=button_icon,
    width=20,
    height=20,
    borderwidth=0,
)
color_btn.grid(row=0, column=2, sticky="e")

subtitle_label = Label(
    text="Stay focused, one session at a time",
    fg=TEXT_COLOR,
    bg=bg_color,
    font=(FONT_NAME, 10),
)
subtitle_label.grid(row=1, column=0, columnspan=3, pady=(0, 12))

# Canvas
canvas = Canvas(width=200, height=224, bg=bg_color, highlightthickness=0)
tomato_img = PhotoImage(file=asset_dir / "tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=2, column=0, columnspan=3)

# Controls
controls_frame = Frame(window, bg=bg_color)
controls_frame.grid(row=3, column=0, columnspan=3, pady=(8, 0))

start_btn = Button(
    controls_frame,
    text="Start",
    width=9,
    highlightthickness=0,
    command=start_timer,
    bg=bg_color,
    activebackground=bg_color,
)
start_btn.grid(row=0, column=0, padx=(0, 6))

reset_btn = Button(
    controls_frame,
    text="Reset",
    width=9,
    highlightthickness=0,
    command=reset_timer,
    bg=bg_color,
    activebackground=bg_color,
)
reset_btn.grid(row=0, column=1, padx=(6, 0))

#checkmark
checkmark_label = Label(fg=TEXT_COLOR, bg=bg_color, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(row=4, column=0, columnspan=3, pady=(12, 0))

window.mainloop()