# Usage: print 6 numbers, each number in new line

# ширина клетки (a)
# расстояние между клетками dist = a * k (k is parameter)
# c минусом задаем угол от 0 до 360(направо) (alpha)
# задаем 0, если надо двигаться вперед,
# задаем 1, если надо двигаться по диагонали, то есть на расстояние a*sqrt(2)

import turtle
import math
# length of the step
a = 30

# distance between numbers = a * k
k = 3/2

list0 = (-270, 0, -90, 0, -90, 0, 0, -90, 0, -90, 0, 10)
list1 = (-315, 1, -135, 0, 0, 10)
list2 = (2, 0, -90, 0, -45, 1, -225, 0, 10)
list3 = (-315, 1, -225, 0, 6, -135, 1, -225, 0, 10)
list4 = (2, -90, 0, -270, 0, -90, 0, 4, -180, 0, 10)
list5 = (3, -180, 0, -270, 0, -270, 0, -90, 0, -90, 0, 10)
list6 = (3, -135, 1, -225, 0, -90, 0, -90, 0, -90, 0, 10)
list7 = (2, 0, -135, 1, -315, 0, 10)
list8 = (-270, 0, -90, 0, -90, 0, 0, -90, 0, -90, 0, -90, 0, 10)
list9 = (4, -180, 0, -90, 0, -90, 0, -90, 0, -45, 1, 10)

List = (list0, list1, list2, list3, list4, list5, list6, list7, list8, list9)

def goto(x, y, sign1, sign2):
    turtle.penup()
    turtle.goto(x + sign1 * a, y + sign2 * a)
    turtle.pendown()

def draw(x_start, y_start, A):
    i = 0
    goto(x_start, y_start, 0, 0)
    while (A[i] != 10):
        s = A[i]
        if (s < 0):
            turtle.right(abs(A[i]))
        if (s == 0):
            turtle.forward(a)
        if (s == 1):
            turtle.forward(a * math.sqrt(2))
        if (s == 2):
            goto(x_start, y_start, 0, 1)
        if (s == 3):
            goto(x_start, y_start, 1, 1)
        if (s == 4):
            goto(x_start, y_start, 1, 0)
        if (s == 6):
            goto(x_start, y_start, 0, -1)
        i = i + 1

for i in range(6):
    n = int(input())
    A = List[n]
    draw(k*(i+1)*a, 0, A)
    turtle.seth(0)
    i = i + 1

x = input()
