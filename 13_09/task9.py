import turtle
import math

#осталось центрировать

turtle.shape('turtle')
def draw(n):
    R = 10*n
    a = 2 * R * math.sin(2 * math.pi / n)
    turtle.penup()
    turtle.goto(-a/2, R)
    turtle.pendown()
    for i in range(n):
        turtle.forward(a)
        turtle.right(360/n)
    return(0)

for i in range(5):
    draw(i+3)

x = input()