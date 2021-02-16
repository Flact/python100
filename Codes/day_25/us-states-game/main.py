import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"]
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another sate name?")

    if answer_state:
        striped_answer = answer_state.title().strip()
        if striped_answer == "Exit":
            break
        row_state = data[data["state"] == striped_answer]
        if not row_state.empty and not None:
            guessed_states.append(striped_answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(row_state["x"]), int(row_state["y"]))
            t.write(row_state["state"].item())
    else:
        break

# print(sorted(list(set(all_states) - set(guessed_states))))  # this is missing states of couldn't filled out
missing_states = pandas.DataFrame(sorted(list(set(all_states) - set(guessed_states))))
missing_states.to_csv("states_to_learn.csv")
