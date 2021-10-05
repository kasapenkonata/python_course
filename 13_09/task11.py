import turtle

def draw_circle(radius):
    for i in range(60):
        turtle.forward(radius)
        turtle.right(6)

for i in range(1,7):
    draw_circle(i)
    turtle.right(180)
    draw_circle(i)