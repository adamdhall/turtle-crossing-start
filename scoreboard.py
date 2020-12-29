from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 0
        
    def update(self):
        self.clear()
        self.goto(-250, 250)
        self.write(self.level, align="center", font=FONT)
        
    def levelup(self):
        self.level += 1
        self.update()
