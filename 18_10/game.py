import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 80
screen = pygame.display.set_mode((600, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

print("Hello!")

f = open('players.txt', 'r')
counter = 0

#for line in f:
#    Line = line.split()
#    counter = counter + 1
#    if ((counter + 5)  == 0):
#        number = int(Line[counter])
#        name = Line[counter + 1]
#        score = int(Line[counter + 2])

#        print(number)
#        print(name)
#        print(score)

class Ball:
    def __init__(self):
        self.x = randint(0, 595)
        self.y = randint(0, 595)
        self.r = randint(5, 50)
        self.color = COLORS[randint(0, 5)]
        circle(screen, self.color, (self.x, self.y), self.r)


    def move(self, color, x, y, r, alpha, betta):
        self.x = x
        self.y = y
        self.color = color
        self.r = r
        self.x = self.x + alpha
        self.y = self.y + betta
        circle(screen, self.color, (self.x, self.y), self.r)

    # Проверка на столкновение шариков о стенки
    def collision(self, x, y, r):
        counter = 0
        if ( x + r  > 600):
            counter = 1
            return 1
        if ( x - r  < 0):
            counter = 1
            return 2
        if (y + r  > 600):
            counter = 1
            return 3
        if (y - r  < 0):
            counter = 1
            return 4
        if (counter == 0):
            return 0

class Rectangle:
    def __init__(self):
        self.x = randint(85, 525)
        self.y = randint(85, 525)
        self.color = COLORS[randint(0, 5)]
        self.x_coord = 0
        self.y_coord = 0
        self.r = randint(30, 50)
        self.a = randint(15, 30)
        self.b = randint(15, 30)
        self.angle = (randint(1, 40) * 0.1 * 2 * math.pi) / 360
#       print(self.angle)
        a_x = self.x - 0.5 * self.a
        a_y = self.y - 0.5 * self.b
        rect(screen, self.color, (a_x, a_y, self.a, self.b))


    def move1(self, color, x, y, x_coord, y_coord,  a, b, r, angle):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color
        self.r = r
        self.angle = self.angle
        self.x_coord = self.x + self.r * math.cos(angle)
        self.y_coord = self.y + self.r * math.sin(angle)
        rect(screen, self.color, (self.x_coord - self.a * 0.5, self.y_coord - self.b * 0.5, self.a, self.b))
#        print(self.x)


N = 10
all_balls = []
all_rects = []
alpha = []
betta = []
counter = 0
score = 0

# Создание мишеней
def create_items():
    for i in range(N):
        a = randint(-1, 1)
        b = randint(-1, 1)
        alpha.append(a)
        betta.append(b)
        ball = Ball()
        rectang = Rectangle()
        all_balls.append(ball)
        all_rects.append(rectang)
        all_rects[i].x = randint(0, 500)
        all_rects[i].y = randint(200, 500)

create_items()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            x = event.pos[0]
            y = event.pos[1]

            # Проверка на то, что попали мышью на мишень
            check = 0
            for i in range(N):
                rect_top = all_rects[i].y + all_rects[i].b
                rect_down = all_rects[i].y - all_rects[i].b
                rect_left = all_rects[i].x - all_rects[i].a
                rect_right = all_rects[i].x + all_rects[i].a
                if (x > rect_left and x < rect_right and y > rect_down and y < rect_top):
                    check = 1
                    type = 1
                if ((x - all_balls[i].x)**2 + (y - all_balls[i].y)**2 < all_balls[i].r):
                    check = 1
                    type = 0
            if (check == 1):
                if (type == 0):
                    score = score + 1
                    print("Great you've touched circle! +1")
                if (type == 1):
                    score = score + 20
                    print("Great you've touched square! +20")

    for i in range(N):

        all_balls[i].move(all_balls[i].color, all_balls[i].x, all_balls[i].y, all_balls[i].r, alpha[i], betta[i])
        ball_collision_return = all_balls[i].collision(all_balls[i].x, all_balls[i].y, all_balls[i].r)
        # Отражение от стенок
        if (ball_collision_return == 1):
            alpha[i] = randint(-1,0)
        if (ball_collision_return == 2):
            alpha[i] = randint(0, 1)
        if (ball_collision_return == 3):
            betta[i] = randint(-1, 0)
        if (ball_collision_return == 4):
            betta[i] = randint(0, 1)
        all_rects[i].move1(all_rects[i].color, all_rects[i].x,all_rects[i].y, all_rects[i].x_coord, all_rects[i].y_coord, all_rects[i].a, all_rects[i].b, all_rects[i].r, all_rects[i].angle * counter)

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

print("Your game is over. Time is out!")
print("Score: ", score)

