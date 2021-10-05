import turtle
import math

turtle.shape('turtle')
angle = 0
turtle.right(45)
for i in range(20):
    rho = 0.3 * angle / (2 * math.pi)
    turtle.right(180)
    turtle.goto(rho*math.cos(angle*2*math.pi/360), rho*math.sin(angle*2*math.pi/360))
    angle = angle + 90

x = input()