import turtle
import pandas



def capitalize_individual(string):
    string = string.lower()
    answer = ""
    for x in string.split():
        if answer == "":
            answer += x.capitalize()
        else:
            answer += " " + x.capitalize()
    return answer


height = 600
width = 780
screen = turtle.Screen()
screen.setup(width, height)

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.tracer(0)
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
states_xcor = data.x.to_list()
states_ycor = data.y.to_list()

game_is_on = True
count_state = 0
answer_saved = []
while game_is_on:
    answer_state = screen.textinput(title=f"Guess the state: {count_state}/50", prompt="What's another state's name?")
    answer_state = capitalize_individual(answer_state)

    if count_state == 50 or answer_state == "Exit":
        game_is_on = False

    if (answer_state in states_list) and (answer_state not in answer_saved):
        count_state += 1
        answer_saved.append(answer_state)
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        index = states_list.index(answer_state)
        print(index)
        print(states_xcor[index])
        print(states_ycor[index])
        state_turtle.goto(x=states_xcor[index], y=states_ycor[index])
        state_turtle.write(answer_state)
        screen.update()

# states_to_learn.csv
states_to_learn = [x for x in states_list if x not in answer_saved]
frame = pandas.DataFrame(states_to_learn)
frame.to_csv("states_to_learn.csv")


# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

# screen.exitonclick()
