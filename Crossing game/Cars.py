import turtle
from turtle import Turtle
import random

y_cors = []
for i in range(-300, 300, 20):
    y_cors.append(i)
turtle.colormode(255)


class Cars(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x_cor, y_cor)
        self.color((random.randint(0, 155), random.randint(100, 155), random.randint(100, 155)))
        self.y_cor = y_cor

    def move(self):
        self.bk(7)


