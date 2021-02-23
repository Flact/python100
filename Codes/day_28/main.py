from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

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
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Button
btn_start = Button(text="Start", highlightthickness=0)
btn_start.grid(row=2, column=0)

btn_start = Button(text="Reset", highlightthickness=0)
btn_start.grid(row=2, column=2)

# Checkbox

lbl_check = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
lbl_check.grid(row=3, column=1)

window.mainloop()
