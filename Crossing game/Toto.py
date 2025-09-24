from turtle import Turtle


class Toto(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.goto(0, -280)
        self.left(90)

    def up(self):
        self.sety(self.ycor()+20)

    def behind(self):
        self.sety(self.ycor()-20)

    def left_side(self):
        self.setx(self.xcor()-20)

    def right_side(self):
        self.setx(self.xcor()+20)


