import turtle

def draw_star(n):
    alpha = 360/(n*2)
    for i in range(n):
        turtle.forward(100)
        turtle.left(180-alpha)

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
draw_star(5)
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
draw_star(11)