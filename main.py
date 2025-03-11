import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")

data = pandas.read_csv("50_states.csv")
correct_answer = data[data["state"] == answer_state]
print(correct_answer)