import turtle

def draw_circle():
    for i in range(60):
        turtle.forward(4)
        turtle.right(6)

for i in range(6):
    draw_circle()
    turtle.right(60)