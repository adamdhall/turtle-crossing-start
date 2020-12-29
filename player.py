from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(position)
        self.setheading(90)


    def move(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
        
    def win_level(self):
        if self.ycor() == 280:
            win_level = True
            
    def reset(self):
        self.goto(0, -280)

