from turtle import Turtle
class Score_board(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = [0,0]
        self.color("white")
        self.penup()
        self.goto(0,277)
        self.hideturtle()
        self.refresh_score()
    def refresh_score(self):
        self.clear()
        self.write(f"{self.score[0]},{self.score[1]}",align="center",font=("Arial", 15 ,"normal"))


    def add_score(self,left = True):
        if left:
            self.score[0]+=1
        else:
            self.score[1]+=1
        self.refresh_score()
    def game_over(self):
        self.goto(0,0)
        self.write(f"game over",align="center",font=("Arial", 15 ,"normal"))



class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        #self.shapesize(40,20)
        self.turtlesize(stretch_wid=0.5,stretch_len=4)
    def move_up(self):
        if self.ycor() <= 280:
            self.forward(40)
    def move_down(self):
        if self.ycor() >= -280:
            self.backward(40)
        

class RightPaddle(Paddle):
    def __init__(self) -> None:
        super().__init__()
        self.goto(430,0)

class LeftPaddle(Paddle):
    def __init__(self) -> None:
        super().__init__()
        self.goto(-430,0)


class Ball(Turtle):
    def __init__(self) -> None:
        self.sleep_time = 0.2
        self.score_board = Score_board()
        super().__init__("circle")
        self.x_move = 20
        self.y_move = 20
        # self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.color("white")
    def fast_ball(self):
        self.sleep_time *= 0.9

    def bounce(self):
        if self.xcor() > 400 or self.xcor() < -400:
            self.x_move *= -1 
        elif self.ycor() > 300 or self.ycor() < -300:
            self.y_move *= -1 
    def collision(self,padle_left,padle_right):
        if self.ycor() >= 299 or self.ycor() <= -299:
            self.bounce()
            return False
        if self.xcor() >= 415:
            if self.distance(padle_right) < 80:
                self.bounce()
                self.fast_ball()
                self.score_board.add_score(left = False)
                return False
            else:
                return True
        if self.xcor() <= -415:
            if self.distance(padle_left) < 80:
                self.score_board.add_score(left = False)
                self.bounce()
                self.fast_ball()
                return False
            else:
                return True
        return False

    def move(self):
        x_cordinate = self.xcor() + self.x_move
        y_cordinate = self.ycor() + self.y_move
        self.goto(x_cordinate,y_cordinate)

        

