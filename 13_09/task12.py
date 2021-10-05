import turtle

def draw_half_circle(step):
    for i in range(30):
        turtle.forward(step)
        turtle.right(6)

def spiral():
    draw_half_circle(4)
    draw_half_circle(1)

turtle.left(90)
spiral()

for i in range(5):
    spiral()

x = input()