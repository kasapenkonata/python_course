import pygame
import math
from pygame.draw import *
from random import randint
import pygame.freetype
import json

pygame.init()

FPS = 80
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_height, screen_height))
game_time = 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#поверхность для вывода очков
screensch = pygame.display.set_mode((screen_height, screen_width))
text1 = pygame.font.Font(None, 50)
text2 = pygame.font.Font(None, 20)
text3 = pygame.font.Font(None, 20)
nick_text = pygame.freetype.SysFont(None, 35)
text_box = pygame.freetype.SysFont(None, 35)

# класс шарика
class Ball:
    def __init__(self):
        self.x = randint(0, 545)
        self.y = randint(0, 545)
        self.r = randint(5, 50)
        self.color = COLORS[randint(0, 5)]
        circle(screen, self.color, (self.x, self.y), self.r)

    # функция движения (по прямой)
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

    # шарик распадается на меньшие шарики принажатии на него
    def destroy(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        N = randint(2, 5)
        for i in range(N):
            ball = Ball()
            ball.r = self.r/1.5
            ball.x = self.x
            ball.y = self.y
            a = randint(-100, 100) * 1 / 100
            b = randint(-100, 100) * 1 / 100

            alpha.append(a)
            betta.append(b)
            all_balls.append(ball)
        return(N)

# класс прямоугольников
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
        self.angle = (randint(1, 40) * 0.01 * 2 * math.pi) / 360
        #self.angle = (randint(1, 40) * 0.1 * 2)
        #print(self.angle)
        a_x = self.x - 0.5 * self.a
        a_y = self.y - 0.5 * self.b
        rect(screen, self.color, (a_x, a_y, self.a, self.b))

    # движение прямоугольников (по окружности)
    def move1(self, color, x, y, x_coord, y_coord,  a, b, r, angle):
        self.x = x
        self.y = y
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.a = a
        self.b = b
        self.color = color
        self.r = r
        self.angle = self.angle
        #print(angle)
        self.x_coord = self.x + self.r * math.cos(angle)
        self.y_coord = self.y + self.r * math.sin(angle)
        rect(screen, self.color, (self.x_coord - self.a * 0.5, self.y_coord - self.b * 0.5, self.a, self.b))

N_balls = 10
N_rects = 10
all_balls = []
all_rects = []
alpha = []
betta = []
counter = 0
score = 0

# Создание мишеней
def create_items():
    for i in range(N_balls):
        a = randint(-100, 100) * 1/100
        b = randint(-100, 100) * 1/100

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

circle_counter = 0
rect_counter = 1
# тип 0 это шарик, тип 1 - прямоугольник
type = 0

while not finished:
    game_time = game_time + 1
    if (game_time > 5000):
        break
    else:
        clock.tick(FPS)
        text = text1.render(
            "Игра: Шарики",
            True,
            BLUE)
        screensch.blit(text, (0, 0))
        text = text2.render(
            "Кликни на кружок - получишь 10 очков, на квадрат - 20 очков ",
            True,
            RED)
        screensch.blit(text, (0, 40))
        text = text3.render(
            "Внимание! Время ограниено: у вас есть ровно одна минута! ",
            True,
            YELLOW)
        screensch.blit(text, (0, 80))
        text_circle = text3.render(
            "Круги: " + str(circle_counter),
            True,
            YELLOW)
        screensch.blit(text_circle, (20, 500))
        text_circle = text3.render(
            "Прямоугольники: " + str(rect_counter),
            True,
            YELLOW)
        screensch.blit(text_circle, (400, 500))
        score_print = text2.render("Score:" + " " + str(score), True, (200, 0, 0))
        screensch.blit(score_print, (0, 60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #print('Click!')
                x = event.pos[0]
                y = event.pos[1]

                # Проверка на то, что попали мышью на мишень
                check = 0
                rect_top = 0
                rect_down = 0
                rect_right = 0
                rect_left = 0
                for i in range(N_rects):
                    rect_top = all_rects[i].y_coord - all_rects[i].b/2
                    rect_down = all_rects[i].y_coord + all_rects[i].b/2
                    rect_left = all_rects[i].x_coord - all_rects[i].a/2
                    rect_right = all_rects[i].x_coord + all_rects[i].a/2
                    if (x > rect_left and x < rect_right):
                        if (y < rect_down and y > rect_top):
                            # если мы попали сюда, значит, пользователь кликнул на прямоугольник
                            check = 1
                            type = 1
                            rect_counter = rect_counter + 1
                            #print("rect: ", rect_counter)

                for i in range(N_balls):
                    if ((x - all_balls[i].x) ** 2 + (y - all_balls[i].y) ** 2 < (all_balls[i].r) ** 2):
                        check = 1
                        type = 0
                        # print(N_balls)
                        New_balls = all_balls[i].destroy(all_balls[i].r, all_balls[i].x, all_balls[i].y)
                        all_balls.remove(all_balls[i])
                        alpha.remove(alpha[i])
                        betta.remove(betta[i])
                        N_balls = N_balls + New_balls - 1
                        # print(len(all_balls))
                        circle_counter = circle_counter + 1
                        # print("circle: ", circle_counter)
                        if (check == 1):
                            if (type == 0):
                                score = score + 10
                                # print("Great you've touched circle! +1")
                        if (type == 1):
                            score = score + 20
                            # print("Great you've touched square! +20")
        for i in range(N_balls):
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

        for i in range(N_rects):
            all_rects[i].move1(all_rects[i].color, all_rects[i].x,all_rects[i].y, all_rects[i].x_coord, all_rects[i].y_coord, all_rects[i].a, all_rects[i].b, all_rects[i].r, all_rects[i].angle * counter)
            counter = counter + 1

        pygame.display.update()
        screen.fill(BLACK)

finished_score = False
name = ""
while not finished_score:
    screen.fill(GREEN)
    nick_text.render_to(screen, (0, 0), "Введите ваше имя!", BLUE)
    nick_text.render_to(screen, (0, 40), "Чтобы стереть нажмите Backspace!", MAGENTA)
    nick_text.render_to(screen, (0, 80), "Чтобы пропустить нажмите Esc!", YELLOW)
    for event in pygame.event.get():
        # если клавиша нажата
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                finished_score = True
            # если клавиша это Esc
            elif event.key == pygame.K_ESCAPE:
                finished_score = True
            # если клавиша это Backspace
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif int(event.key) <= 126 and int(event.key) >= 33 or int(event.key) <= 1103 and int(event.key) >= 1040:
                name += pygame.key.name(event.key)
                #print(name) - тут проверили, что имя считалось
        nick_text.render_to(screen, (350, 0), name, BLUE)
        pygame.display.update()
        #print(2)

with open(r"records.json") as f:
    data = json.load(f)
data[name] = score
#print(data)
step = 60
# Выводим таблицу рекордов
screen.fill(GREEN)
nick_text.render_to(screen, (0, 0), "Лучшие игроки: ", BLUE)
Records = []
for i, j in data.items():
    Records.append([j, i])
Records.sort(reverse=True)

for i in Records:
    text_box.render_to(screen
                       , (20, step), i[1] + ":" + " " + str(i[0]), BLUE)
    step = step + 30
pygame.display.update()

finished = False
nick_text.render_to(screen, (0, 300), "Чтобы выйти нажмите Esc!", BLUE)
pygame.display.update()
while not finished:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                finished = True

with open(r"records.json", 'w') as f:
    json.dump(data, f)
pygame.quit()