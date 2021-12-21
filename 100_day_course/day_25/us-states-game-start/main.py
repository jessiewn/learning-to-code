from os import stat
import turtle
import pandas


screen=turtle.Screen()
tim=turtle.Turtle()

screen.title("U.S. States Game")
image="100_day_course/day_25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)



data=pandas.read_csv("100_day_course/day_25/us-states-game-start/50_states.csv")
state_list=data.state.to_list()
print(state_list)


game_continue=True
answer_list=[]
score=0
while score<50:
    answer_state = screen.textinput(title=f"{score}/50states correct",prompt="What'sn another state's name?").title()
    if answer_state=="Exit":
        missing_state=[state for state in state_list if state not in answer_list]
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("100_day_course/day_25/us-states-game-start/states_to_learn.csv")
        break
    for state in state_list:
        if answer_state == state:
            row=data[data["state"]==answer_state]
            x=int(row.x)
            y=int(row.y)
            tim.hideturtle()
            tim.penup()
            tim.color("black")
            tim.goto(x,y)
            tim.write(f"{state}")
            answer_list.append(state)
            score=len(answer_list)


turtle.mainloop()




