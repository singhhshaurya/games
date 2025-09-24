from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, high_score
import random
import time


a = open('high score.txt', 'r+')
sc = Screen()
sc.setup(600, 600)
sc.bgcolor('black')
sc.tracer(0)

sn1 = Snake()
cors = []
for i in range(-280, 280, 5):
    cors.append(i)

fd = Food(random.choice(cors), random.choice(cors))

is_speed = True
delay = 0.1
score = 0
scbd = Scoreboard()
scbd2 = Scoreboard()
scbd3 = Scoreboard()
scbd.write_score(score)
scbd2.hi_score()

snake_body = [sn1]
is_game = False

scbd3.start_game()
def start_game():
    global is_game
    scbd3.clear()
    is_game = True
    scbd3.game_over(sn1, snake_body)
    scbd2.clear()
    scbd2.hi_score()


while True:
    if is_game:
        sc.onkeypress(sn1.up, 'Up')
        sc.onkeypress(sn1.down, 'Down')
        sc.onkeypress(sn1.left_d, 'Left')
        sc.onkeypress(sn1.right_d, 'Right')
        sc.listen()

        if fd.distance(sn1) < 20:
            fd.goto(random.choice(cors), random.choice(cors))
            sn = Snake()
            sn.color('grey')
            snake_body.append(sn)
            score += 1
            if not is_speed:
                is_speed = True
            scbd.clear()
            scbd.write_score(score)

        for i in range(len(snake_body)-1, 0, -1):
            if i != sn1:
                new_x = snake_body[i-1].xcor()
                new_y = snake_body[i-1].ycor()
                snake_body[i].goto(new_x, new_y)

        sn1.fd(20)
        if sn1.collison_with_wall() or sn1.collison_with_itself(snake_body):
            if score > high_score:
                scbd3.change_hi_score(score)
            scbd3.game_over_message()
            scbd3.start_game()
            score = 0
            sc.update()

            is_game = False
            delay = 0.1
            continue

        if is_speed:
            if score % 5 == 0 and score != 0:
                is_speed = False
                delay *= 0.8
    else:
        sc.onkeypress(start_game, 'space')
        sc.listen()

    sc.update()
    time.sleep(delay)

sc.exitonclick()
