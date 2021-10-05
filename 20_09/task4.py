import turtle

turtle.width(5)
turtle.forward(250)
turtle.left(180)
turtle.forward(250)
turtle.right(180)

i = 0
Vx = 10
Vy = 40
dt = 0.1
g = 10
y = 0
x = 0
turtle.width(0.5)

while i < 10:
    x += Vx * dt
    y += Vy * dt - g * dt ** 2 / 2
    Vy -= g * dt
    if y < 0:
        y = 0
        Vy = -0.7 * Vy
        Vx = 0.8 * Vx
        i += 1
    turtle.goto(x, y)
