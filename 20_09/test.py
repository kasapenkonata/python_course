import turtle
import math
dist = 0
koeff = 0

list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []

List = [list0, list1, list2, list3, list4, list5, list6, list7, list8, list9]

f = open('input.txt', 'r')
counter = 0
i = 0
for line in f:
    Line = line.split()
    counter = counter + 1
    if (counter == 2):
        print('here')
        dist = float(Line[0])
        print(dist)
    if (counter == 4):
        koeff = float(Line[0])
        print(koeff)
    if (counter > 5 and counter < 26 and counter%2 == 0):
        i = Line[0]
#        print(i)
    if (counter > 5 and counter < 26 and counter%2 == 1):
        k = 0
        r = 0
        for r in range(len(Line)):
            Line[r] = int(Line[r])

        while (int(Line[k]) != 11):
            t = int(Line[k])
            List[int(i)].append(t)
            k = k + 1

k = 0
t = 0
i = 0
r = 0
x = 0
y = 0
counter = 0
line = 0

for i in range(10):
    print(List[i])


def goto(x, y, sign1, sign2):
    turtle.penup()
    turtle.goto(x + sign1 * dist, y + sign2 * dist)
    turtle.pendown()

def draw(x_start, y_start, A):
    i = 0
    goto(x_start, y_start, 0, 0)
    while (A[i] != 10):
        s = A[i]
        if (s < 0):
            turtle.right(abs(A[i]))
        if (s == 0):
            turtle.forward(dist)
        if (s == 1):
            turtle.forward(dist * math.sqrt(2))
        if (s == 2):
            goto(x_start, y_start, 0, 1)
        if (s == 3):
            goto(x_start, y_start, 1, 1)
        if (s == 4):
            goto(x_start, y_start, 1, 0)
        if (s == 6):
            goto(x_start, y_start, 0, -1)
        i = i + 1

print("Enter each new digit in new line")
for i in range(6):
    n = int(input())
    A = List[n]
    draw(koeff*(i+1)*dist, 0, A)
    turtle.seth(0)
    i = i + 1

x = input()

