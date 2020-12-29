from turtle import Turtle
import random
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():
    def __init__(self):
        self.allcars = []

    def create_cars(self):
        numbers = [1,2,3,4,5,6]
        random_number = random.choice(numbers)
        if random_number == 1:
            newcar=Turtle("square")
            newcar.color(random.choice(COLORS))
            newcar.penup()
            newcar.shapesize(2.0, 1.0, 1.0)
            newcar.setx( 300)
            newcar.sety(random.randint(-250, 250))
            newcar.setheading(90)
            self.allcars.append(newcar)

    def move(self):
        for car in self.allcars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto((new_x, car.ycor()))

    def movefaster(self):
        for car in self.allcars:
            faster = 10
            new_x = car.xcor() - faster
            car.goto((new_x, car.ycor()))
            faster -= 10



