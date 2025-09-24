import turtle
import pandas
from create_state import Create_State

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(width=700, height=500)
screen.addshape(image)
turtle.shape(image)

correct = 0
state_list = data.state.to_list()
store_list = []
create_state = Create_State()


while correct < 50:

    answer_state = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in state_list and answer_state not in store_list:
        store_list.append(answer_state)
        correct += 1
        state_data = data[data.state == answer_state]
        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])
        create_state.write_state(answer_state, x, y)

    print(answer_state.title())

#states_to_learn.csv
states_to_learn = []
for state in state_list:
    if state not in store_list:
        states_to_learn.append(state)
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")