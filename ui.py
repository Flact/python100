from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=25, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, font=(
            'Calibri', 20, "bold"), fg="white").grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        # self.ques_text = "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory."
        self.ques_text = self.canvas.create_text(150, 125,
                                                 width=300,
                                                 fill=THEME_COLOR,
                                                 font=('Consolas', 18, "bold italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, bd=0)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, bd=0)
        self.false_button.grid(row=2, column=1, padx=(20, 20))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.ques_text, text=q_text)
