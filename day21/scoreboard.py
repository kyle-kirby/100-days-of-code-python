from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as self.high_score:
            self.high_score = int(self.high_score.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)


    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score} ", align="center", font=("Arial", 22, "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_score:
                new_score.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial", 22, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()