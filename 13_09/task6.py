
import turtle

turtle.shape('turtle')
print('Input number:')
n = int(input())
print('Your number is:' + str(n))
for i in range(n):
        turtle.forward(100)
        turtle.stamp()
        turtle.goto(0, 0)
        turtle.right(360/n)

x = input()