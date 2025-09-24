from turtle import Screen
from Cars import Cars
from Toto import Toto
from green_zone import Green
from Level import Level

import time
import random

sc = Screen()
sc.setup(600, 700)
sc.tracer(0)

cars = []
count = 0
speed = 0.05
player_level = 1
car_count = 4
change = True

y_cors = []

for i in range(-220, 300, 20):
    if i in [20, 40, 60]:
        continue
    y_cors.append(i)


x_cor = []
ctr = 360
for i in range(12):
    x_cor.append(ctr)
    ctr += 15


g1 = Green(-290)
g2 = Green(40)
l1 = Level(player_level)
t1 = Toto()

is_game = True
while is_game:
    sc.onkeypress(t1.up, 'Up')
    sc.onkeypress(t1.behind, 'Down')
    sc.onkeypress(t1.left_side, 'Left')
    sc.onkeypress(t1.right_side, 'Right')
    sc.listen()

    sc.update()

    y_coordinates = [i for i in y_cors]
    x_coordinates = [i for i in x_cor]
    if count % 20 == 0:
        for i in range(car_count):
            car1 = Cars(random.choice(x_coordinates), random.choice(y_coordinates))
            y_coordinates.remove(int(car1.ycor()))
            x_coordinates.remove(int(car1.xcor()))
            cars.append(car1)

    for i in cars.copy():
        if -20 < i.ycor() - t1.ycor() < 25 and -25 < i.xcor() - t1.xcor() < 25:

            print(i.ycor() - t1.ycor(), 'Y')
            print(i.xcor() - t1.xcor(), 'X')
            t1.color('dark red')
            sc.update()
            time.sleep(2)
            t1.color('black')
            t1.goto(0, -290)
            break

        i.move()
        if i.xcor() < -320:
            cars.remove(i)

    if t1.ycor() >= 330:
        time.sleep(1.5)
        player_level += 1
        l1.clear()
        l1 = Level(player_level)
        t1.goto(0, -290)

        speed *= 0.5
        car_count += 1
        change = True

    sc.update()
    time.sleep(speed)
    count += 1

sc.exitonclick()