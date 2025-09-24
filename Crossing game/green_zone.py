from turtle import Turtle

class Green(Turtle):
    def __init__(self, y_cor):
        super().__init__()
        self.penup()
        self.goto(0, y_cor)
        self.shape('square')
        self.shapesize(stretch_wid=2, stretch_len=30)
        self.color('light green')
