import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.listen()

scoreboard= Scoreboard()

car_manager= CarManager()

player=Player((0, -100))
screen.onkey(player.move, "w")



game_is_on = True

while game_is_on == True:

    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move()
    scoreboard.update()
    screen.update()



    if player.ycor() > 280:
        player.reset()
        scoreboard.levelup()
        car_manager.create_cars()

        car_manager.movefaster()

    for car in car_manager.allcars:
        if player.distance(car) < 20:
            game_is_on = False
            player.goto(0, 0)
            player.hideturtle()
            player.write("Game Over!", align="center", font= ("Courier", 24, "normal"))

screen.exitonclick()


