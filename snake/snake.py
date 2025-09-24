from turtle import Turtle, Screen

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')

    def right_d(self):
        self.setheading(0)
        print("TADA")

    def left_d(self):
        self.setheading(180)

    def up(self):
        self.setheading(90)

    def down(self):
        self.setheading(270)

    def collison_with_wall(self):
        if self.xcor()<-280 or self.xcor()>280 or self.ycor()<-280 or self.ycor()>280:
            return True
        else:
            return False

    def collison_with_itself(self, body):
        for i in body[1:]:
            if self.distance(i) < 10:
                print(self.distance(i))
                print(body.index(i))
                return True
        else:
            return False




