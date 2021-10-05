import turtle

def draw_circle(step):
    for i in range(60):
        turtle.forward(step)
        turtle.right(6)

def draw_half_circle(step):
    for i in range(30):
        turtle.forward(step)
        turtle.left(6)

turtle.color('yellow')
turtle.begin_fill()
draw_circle(4)
turtle.end_fill()

turtle.penup()
turtle.goto(-15,-20)

turtle.color('blue')
turtle.begin_fill()
draw_circle(0.5)
turtle.end_fill()

turtle.penup()
turtle.goto(15,-20)

turtle.color('blue')
turtle.begin_fill()
draw_circle(0.5)
turtle.end_fill()

turtle.color('black')
turtle.goto(0,-30)
turtle.pendown()
turtle.width(3)
turtle.right(90)
turtle.forward(20)

turtle.penup()
turtle.goto(-17, -51)
turtle.color('red')
turtle.pendown()
draw_half_circle(2)


x = input()