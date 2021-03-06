from turtle import Turtle

ALIGNMENT = "center"
FONT = ("PottaOne-Regular", 18, "normal")


def read_score():
    with open("data.txt") as file:
        return int(file.read())


def write_score(score):
    with open("data.txt", mode="w") as file:
        file.write(score)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()
        # self.clear()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def rest(self):
        if self.score > self.high_score:
            self.high_score = self.score
            write_score(f"{self.high_score}")

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
