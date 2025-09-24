from turtle import Turtle
import time
import random
from turtle import Screen
from PaddleClass import Paddle, Writing

# SCREEN
sc = Screen()
sc.setup(width=1366, height=760)
sc.bgcolor('black')
sc.tracer(0)


# SLIDERS
t1 = Paddle(600, 0)
t2 = Paddle(-650, 0)

# Line drawing in the middle
tp = Turtle()
tp.pencolor('white')
tp.pensize(10)
tp.penup()
tp.hideturtle()
tp.goto(0, 360)
tp.left(90)
for i in range(17):
    tp.pendown()
    tp.bk(20)
    tp.up()
    tp.bk(20)

# Score boards
p1 = Writing(-200, 220, 100, '0')
p2 = Writing(100, 220, 100, '0')


point = Turtle(shape='square')
point.color('white')
point.penup()

# Variables
chance = 2
pn1 = 0
pn2 = 0
turns = 0
speed = 0.05
sp = True

sc.tracer(1)
while True:
    if chance == 2:
        sc.onkeypress(t1.up, 'Up')
        sc.onkeypress(t1.down, 'Down')
        sc.onkeypress(t1.nothing, 'w')
        sc.onkeypress(t1.nothing, 's')
    elif chance == 1:
        sc.onkeypress(t2.up, 'w')
        sc.onkeypress(t2.down, 's')
        sc.onkeypress(t2.nothing, 'Up')
        sc.onkeypress(t2.nothing, 'Down')

    sc.listen()
    point.forward(25)
    time.sleep(speed)
    if point.xcor() <= -615 or point.xcor() >= 565:
        # TARGET HITS THE POINTER
        turns += 1
        if chance == 1 and -50 <= point.ycor() - t2.ycor() <= 50 or chance == 2 and -50 <= point.ycor() - t1.ycor() <= 50:
            sc.tracer(0)
            if chance == 1:
                point.setheading(random.randint(-60, 60))
            else:
                point.setheading(random.randint(140, 220))
            sc.tracer(1)
            point.fd(25)
            time.sleep(speed)
            if chance == 1:
                chance = 2
            else:
                chance = 1
        else:
            # Someone gets OUT!
            if chance == 2:
                pn1 += 1
                p1.clear()
                p1.write(str(pn1), font=('bank gothic', 100, 'normal'))
                point.setheading(0)
            else:
                pn2 += 1
                p2.clear()
                p2.write(str(pn2), font=('bank gothic', 100, 'normal'))
                point.setheading(180)
            time.sleep(1)
            sc.tracer(0)
            point.goto(0, 0)
            sc.tracer(1)
            speed, sp, turns = 0.05, True, 0

        # speed
        if speed == 0.01:
            sp = False
        if sp:
            if turns % 2 == 0 and turns != 0:
                speed /= 2

    sc.tracer(0)

    # turning the pointer when it hits the wall
    if point.ycor() >= 350 or point.ycor() <= -300:
        point.setheading(360 - point.heading())

    # GAME OVER
    if pn1 == 2 or pn2 == 2:
        sc.tracer(0)
        p2.goto(-450, 0)
        p2.write("GAME OVER", font=('bank gothic', 100, 'normal'))
        break

    sc.tracer(1)
sc.exitonclick()
