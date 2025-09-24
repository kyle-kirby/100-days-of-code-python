from turtle import Turtle

class Create_State(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()


    def write_state(self, name, x, y):
        self.goto(x, y)
        self.write(name)
