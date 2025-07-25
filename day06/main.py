#  This solves the maze challenge at https://reeborg.ca/reeborg.html
#  TODO: solve edge cases

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_on_right() and not front_is_clear():
        turn_left()
    else:
        turn_right()
        move()