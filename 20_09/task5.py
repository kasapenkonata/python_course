import turtle
from random import *

# Функции fisrt_check и second_check выявляют столкновения
def first_check(n, x, r):
    segment = []
    for i in range(n):
        seg = (x[i] - r[i], x[i] + r[i], i)
        segment.append(seg)
    segment.sort()

    intersect = set()
    for i in range(n - 1):
        k = i + 1
        while (k < n and segment[i][1] > segment[k][0]):
            intersect.add((min(segment[i][2], segment[k][2]), max(segment[i][2], segment[k][2])))
            k += 1
    return intersect


def second_check(intersect, n, r, x, y):
    collisions = set()
    for pair in intersect:
        i = pair[0]
        k = pair[1]
        if ((x[i] - x[k]) ** 2 + (y[i] - y[k]) ** 2 < (r[i] + r[k]) ** 2):
            collisions.add((min(i, k), max(i, k)))
    return collisions

# Рассчитываем соударение частиц друг с другом
def calc_coll_gas(collision, n, m, x, y, vx, vy, ):
    for pair in collision:
        x1 = x[pair[0]]
        y1 = y[pair[0]]
        vx1 = vx[pair[0]]
        vy1 = vy[pair[0]]
        x2 = x[pair[1]]
        y2 = y[pair[1]]
        vx2 = vx[pair[1]]
        vy2 = vy[pair[1]]
        factor1 = (vx2 - vx1) * (x2 - x1) + (vy2 - vy1) * (y2 - y1)
        if (factor1 < 0):
            factor2 = 2 * factor1 / ((m[pair[0]] + m[pair[1]]) * ((x2 - x1) ** 2 + (y2 - y1) ** 2))
            vx[pair[0]] += m[pair[1]] * factor2 * (x2 - x1)
            vy[pair[0]] += m[pair[1]] * factor2 * (y2 - y1)
            vx[pair[1]] += m[pair[0]] * factor2 * (x1 - x2)
            vy[pair[1]] += m[pair[0]] * factor2 * (y1 - y2)

# Рассчитывавем соударение частиц со стенами
def calc_coll_walls(width, height, n, r, x, y, vx, vy):
    for i in range(n):
        if (vx[i] > 0 and x[i] + r[i] > width / 2):
            vx[i] *= -1.0
        if vy[i] > 0 and y[i] + r[i] > height / 2:
            vy[i] *= -1.0
        if vx[i] < 0 and x[i] - r[i] < -width / 2:
            vx[i] *= -1.0
        if vy[i] < 0 and y[i] - r[i] < -height / 2:
            vy[i] *= -1.0

# Рассчитываем движение частиц за время dt
def calc_iter(n, x, y, vx, vy, dt, g):
    for i in range(n):
        x[i] += vx[i] * dt
        y[i] += vy[i] * dt - g * dt ** 2 / 2
        vy[i] -= g * dt

# Перемезщаем частицы
def drawgas(n, gas, x, y):
    for i in range(n):
        gas[i].goto(x[i], y[i])


# константы
n = 10
width = 400.0
height = 400.0
dt = 1
total_iter = 5000
g = 0.1
a = 1
b = 1

# рисование коробки
god = turtle.Turtle(shape='turtle')
god.penup()
god.left(90)
god.speed(10)
god.goto(-width / 2, -height / 2)
god.pendown()
god.goto(width / 2, -height / 2)
god.goto(width / 2, height / 2)
god.goto(-width / 2, height / 2)
god.goto(-width / 2, -height / 2)
god.hideturtle()
god.penup()
god.goto(0, height / 1.8)

# инициализация частиц газа
r = [12.0] * n
m = [1.0] * n
x = [0.0] * n
y = [0.0] * n
vx = [0.0] * n
vy = [0.0] * n
gas = []
for i in range(n):
    gas.append(turtle.Turtle(shape='circle'))
    gas[i].penup()
    gas[i].speed(10)
    vx[i] = (2.0 * random() - 1.0) * 8.0
    vy[i] = (2.0 * random() - 1.0) * 8.0

vx_max = 8 * 2
vx_plot = [0] * (2 * vx_max + 1)

for i in range(total_iter):
    god.showturtle()
    intersect_x = first_check(n, x, r)
    intersect_y = first_check(n, y, r)
    intersect = intersect_x & intersect_y
    collision = second_check(intersect, n, r, x, y)
    calc_coll_gas(collision, n, m, x, y, vx, vy, )
    calc_coll_walls(width, height, n, r, x, y, vx, vy)
    calc_iter(n, x, y, vx, vy, dt, g)
    for k in range(n):
        vx_plot[min(max(vx_max + round(vx[k]), 0), vx_max * 2)] += 1
    if i % 50 == 0:
        sigma = 0
        for k in range(2 * vx_max + 1):
            sigma += vx_plot[k] * (k - vx_max) ** 2
        sigma /= n * (i + 1)
    god.hideturtle()
    drawgas(n, gas, x, y)