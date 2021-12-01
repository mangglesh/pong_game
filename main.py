from random import randint
from time import sleep, time
from turtle import Screen, Turtle, penup, screensize, width
from ball import LeftPaddle,RightPaddle,Ball,Score_board
screen = Screen()
screen.setup(width = 800,height=600)
screen.bgcolor("black")
screen.tracer(0)
line = Turtle()
line,penup()
line.goto(0,-400)
line.color("white")
line.pendown()
line.goto(0,400)
line.hideturtle()


leftball = LeftPaddle()
rightBall = RightPaddle()
score_board = Score_board()


screen.listen()
screen.onkey(leftball.move_up, "w")
screen.onkey(leftball.move_down, "s")
screen.onkey(rightBall.move_up, "Up")
screen.onkey(rightBall.move_down, "Down")
ball = Ball()
ball.setheading(randint(0,90))
game_is_on = True
while game_is_on:
    screen.update()
    sleep(ball.sleep_time)
    if ball.collision(leftball,rightBall):
        score_board.game_over()
        game_is_on = False
    ball.move()



 








screen.exitonclick()
