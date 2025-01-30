from turtle import Screen
from snakeclass import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game") 
screen.tracer(0)

snakeclass=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snakeclass.up,"Up")
screen.onkey(snakeclass.down,"Down")
screen.onkey(snakeclass.left,"Left")
screen.onkey(snakeclass.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snakeclass.move()


    if snakeclass.head.distance(food)<15:
        food.refresh()
        snakeclass.extend()
        score.increase_score()

    
    if snakeclass.head.xcor()>280 or snakeclass.head.xcor()<-280 or snakeclass.head.ycor()>280 or snakeclass.head.ycor()<-280:
        game_is_on=False
        score.game_over()

    for segment in snakeclass.segments[1:]:
        if snakeclass.head.distance(segment)<10:
            game_is_on=False
            score.game_over()




screen.exitonclick()