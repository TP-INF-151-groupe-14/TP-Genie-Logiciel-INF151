import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("green")

beam = turtle.Turtle()
beam.hideturtle()
beam.speed(0)
beam.width(3)
beam.color("lime")

targets = [
    (random.randint(-150, 150), random.randint(-150, 150))
    for _ in range(5)
]

angle = 0


def draw_radar():
    t.clear()

    for r in [50, 100, 150, 200]:
        t.penup()
        t.goto(0, -r)
        t.pendown()
        t.circle(r)

    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.goto(200, 0)

    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.goto(0, 200)


def animate():
    global angle

    beam.clear()

    x = 200 * math.cos(math.radians(angle))
    y = 200 * math.sin(math.radians(angle))

    beam.penup()
    beam.goto(0, 0)
    beam.setheading(angle)
    beam.pendown()
    beam.goto(x, y)

    for tx, ty in targets:
        target_angle = math.degrees(math.atan2(ty, tx))

        diff = abs(target_angle - angle)

        if diff > 180:
            diff = 360 - diff

        if diff < 4:
            t.penup()
            t.goto(tx, ty)
            t.dot(12, "red")

    angle += 3

    if angle >= 360:
        angle = 0

    screen.update()

    screen.ontimer(animate, 20)


draw_radar()
animate()

screen.mainloop()