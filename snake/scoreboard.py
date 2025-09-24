from turtle import Turtle

a = open('high score.txt', 'r+')
high_score = int(a.read().split()[-1])
a.close()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(100, 200)
        self.hideturtle()
        self.color('white')

    def write_score(self, score):
        self.goto(-100, 260)
        self.write(f'SCORE : {score}', align = 'center', font=('times new roman', 20, 'normal'))

    def game_over(self, snake, body):
        snake.goto(0, 0)
        for i in body[1:]:
            i.hideturtle()
        body.clear()
        body.append(snake)
        pass

    def game_over_message(self):
        self.goto(0, 0)
        self.write(f'GAME OVER!', align='center', font=('times new roman', 20, 'normal'))

    def hi_score(self):
        self.goto(125, 260)
        self.write(f'HIGH SCORE : {high_score}', align='center', font=('times new roman', 20, 'normal'))

    def change_hi_score(self, new):
        with open('high score.txt', 'a') as a:
            a.write(" "+str(new))
        self.goto(0, -50)
        self.write(f'NEW HIGH SCORE!!', align='center', font=('times new roman', 30, 'normal'))
        global high_score
        high_score = new

    def start_game(self):
        self.goto(0, -200)
        self.write(f'PRESS "SPACE" TO START THE GAME', align='center', font=('times new roman', 10, 'normal'))


