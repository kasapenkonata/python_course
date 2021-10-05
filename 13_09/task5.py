
import turtle

turtle.shape('turtle')
a = 0
for j in range(10):
    a = a + 10
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)
    turtle.penup()
    turtle.backward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.pendown()

x = input()