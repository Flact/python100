from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def rest_timer():
    if timer:
        window.after_cancel(timer)
        # timer_text 00:00
        canvas.itemconfig(timer_text, text="00:00")
        # lbl_timer "Timer"
        lbl_timer.config(text="Timer")
        # reset lbl_check
        lbl_check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's 8th rep:
    if reps % 8 == 0:
        lbl_timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # if it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        lbl_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    # if it's the 1st/3rd/5th/7th rep:
    else:
        lbl_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        lbl_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
lbl_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
lbl_timer.grid(row=0, column=1)

# Tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# *args = positional arguments, **kw = keyword arguments
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Button
btn_start = Button(text="Start", highlightthickness=0, command=start_timer)
btn_start.grid(row=2, column=0)

btn_reset = Button(text="Reset", highlightthickness=0, command=rest_timer)
btn_reset.grid(row=2, column=2)

# Checkbox
lbl_check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
lbl_check.grid(row=3, column=1)

window.mainloop()
