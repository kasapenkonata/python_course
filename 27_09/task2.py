import pygame
import random
from pygame.draw import *
from math import sin, cos

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

rect(screen, (55, 200, 113), (0, 0, 500, 350))
rect(screen, (128, 128, 128), (0, 350, 500, 350))

def tree(width, height, x):
    rect(screen, (214, 229, 17), (x, 0, width, height))


def mushroom(x, y, n):
    ellipse(screen, (255, 255, 255), (x, y, 10 * n, 40 * n), 0)
    ellipse(screen, (234, 24, 55), (x - 10 * n, y - 5 * n, 40 * n, 20 * n), 0)

    for i in range(0, 10):
        x0 = random.randint(x - 9 * n, x + 22 * n)
        y0 = random.randint(y - 1 * n, y + 4 * n)
        r1 = random.randint(4 * n, 7 * n)
        r2 = random.randint(9 * n, 13 * n)
        ellipse(screen, (255, 255, 255), (x0, y0,  0.5 * r2, 0.5 * r1), 0)

def fruit(color, radius, x, y):
    circle(screen, color, (x, y), radius, 0)
    circle(screen, (255, 255, 255), (x, y), radius, 2)


def spikes(x, y):
    for i in range(0, 75):
        x0 = random.randint(x + 18, x + 220)
        y0 = random.randint(y + 40, y + 137)
        r1 = random.randint(5, 8)
        r2 = random.randint(5, 8)
        r3 = random.randint(80, 100)
        a = ((random.randint(-20, 20)) * 3.1416) / 180
        polygon(screen, (50, 50, 50),
                [(x0 - (r1 * cos(a)), y0 - (r1 * sin(a))), (x0 + (r3 * sin(a)), y0 - (r3 * cos(a))),
                 (x0 + (r2 * cos(a)), y0 + (r2 * sin(a)))])
        line(screen, (0, 0, 0), (x0 - (r1 * cos(a)), y0 - (r1 * sin(a))), (x0 + (r3 * sin(a)), y0 - (r3 * cos(a))), 1)
        line(screen, (0, 0, 0), (x0 - (r1 * cos(a)), y0 - (r1 * sin(a))), (x0 + (r2 * cos(a)), y0 + (r2 * sin(a))), 1)
        line(screen, (0, 0, 0), (x0 + (r2 * cos(a)), y0 + (r2 * sin(a))), (x0 + (r3 * sin(a)), y0 - (r3 * cos(a))), 1)


def body(x, y):
    ellipse(screen, (75, 75, 75), (x - 15, y + 60, 30, 20), 0)
    ellipse(screen, (220, 220, 220), (x - 15, y + 60, 30, 20), 1)
    ellipse(screen, (75, 75, 75), (x - 15, y + 90, 30, 20), 0)
    ellipse(screen, (220, 220, 220), (x - 15, y + 90, 30, 20), 1)
    ellipse(screen, (75, 75, 75), (x + 240, y + 70, 30, 20), 0)
    ellipse(screen, (220, 220, 220), (x + 240, y + 70, 30, 20), 1)
    ellipse(screen, (75, 75, 75), (x + 215, y + 120, 30, 20), 0)
    ellipse(screen, (220, 220, 220), (x + 215, y + 120, 30, 20), 1)
    ellipse(screen, (100, 100, 100), (x, y, 250, 150), 0)
    ellipse(screen, (220, 220, 220), (x, y, 250, 150), 1)
    ellipse(screen, (50, 60, 50), (x + 225, y + 85, 55, 40), 0)
    ellipse(screen, (220, 220, 220), (x + 225, y + 85, 55, 40), 1)
    ellipse(screen, (0, 0, 0), (x + 235, y + 97, 10, 10), 0)
    ellipse(screen, (220, 220, 220), (x + 235, y + 97, 10, 10), 1)
    ellipse(screen, (0, 0, 0), (x + 250, y + 92, 10, 10), 0)
    ellipse(screen, (220, 220, 220), (x + 250, y + 92, 10, 10), 1)

    spikes(x, y)
    mushroom(x + 100, y - 60, 2)
    fruit((211, 25, 35), 30, x + 200, y)
    fruit((255, 199, 93), 30, x + 50, y + 20)
    fruit((255, 199, 93), 30, x + 70, y)
    spikes(x, y)

tree(30, 380, 0)
tree(95, 700, 55)
tree(30, 380, 380)
tree(20, 500, 450)
body(120, 520)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()