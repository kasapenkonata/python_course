import turtle
import math

turtle.shape('turtle')
angle = 0
for i in range(300):
    angle = angle + 0.1
    rho = 10 * angle / (2 * math.pi)
    turtle.goto(rho*math.cos(angle), rho*math.sin(angle))

x = input()