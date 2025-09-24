from turtle import Screen, Turtle
class Level(Turtle):
    def __init__(self, player_level):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 300)
        self.pencolor('black')
        self.write(f"LEVEL: {player_level}", font=('times new roman', 20, 'underline'))