from turtle import Turtle, Screen

class Food(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

        self.color('red')
        self.goto(x_cor, y_cor)

