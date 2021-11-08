import pygame
import math
from pygame.draw import *
from random import *

pygame.init()

# Настройки прорисовки и экрана
FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)


# Настройки
target_num = 2 # количество мишеней, одновременно присутствующих на экране
min_gun_len = 40 # длина пушки до выстрела
max_gun_len = 100 # максимальная длина отрезка, изображающего пушку
sc_line = 55 # величина поля в левой части экрана, в котором расположена пушка
target_max_rad = 50 # максимальный радиус мишени
rad_bullet = 15 # радиус пули
target_max_angle = 2*math.pi # максимальное значение угла (применяется при расчетах движения мишени)
target_speed = 10 # скорость перемещения мишеней
gun_bottom = [0, HEIGHT/2] # координата основания пушки
gun_len = min_gun_len
flag = 0
min_power = 5 # начальная мощность пушки
power = min_power
points = 0
shots = 0
g = 1 # ускорение свободного падения


def target_delete(target_list, target):
    '''
    Функция заменяет пораженные мишени новыми
    '''
    target_list[target_list.index(target)] = list(new_target())
    return target_list


def new_target():
    '''
    Функция создает кружок-мишень
    '''
    color = choice(GAME_COLORS)
    x = randint(target_max_rad + sc_line, WIDTH - target_max_rad)
    y = randint(target_max_rad, HEIGHT - target_max_rad)
    rad = randint(30, target_max_rad)
    circle(screen, color, (x, y), rad)
    circle(screen, BLACK, (x, y), rad, 1)
    angle = randint(0, int(target_max_angle))
    return [x, y, rad, angle, color]


def moving_target(target):
    '''
    Функция обеспечивает передвижение мишени
    '''
    x = target[0]
    y = target[1]
    rad = target[2]
    color = target[4]
    if x >= WIDTH - rad:
        target[3] = math.pi / 2 + random() * math.pi
    if y >= HEIGHT- rad - sc_line:
        target[3] = random() * math.pi
    if rad >= x:
        target[3] = random() * math.pi - math.pi / 2
    if rad >= y:
        target[3] = random() * math.pi + math.pi
    angle = target[3]
    x += int(target_speed * math.cos(angle))
    y -= int(target_speed * math.sin(angle))
    target[0] = x
    target[1] = y
    circle(screen, color, (x, y), rad)
    circle(screen, BLACK, (x, y), rad, 1)
    return target


# Предварительное создание мишеней
target_list = []
for i in range(target_num):
    list.append(target_list, list(new_target()))

# Предварительное создание списка пуль
bullet_list = []


def gun_drawing(gun_bottom, gun_top, color):
    '''
    Gun-drawing function
    '''
    line(screen, color, gun_bottom, gun_top, 7)


def gun_turning(cursor, gun_bottom, gun_len):
    '''
    Функция поворачивает пушку вслед за курсором мыши
    '''
    dx = cursor[0] - gun_bottom[0]
    dy = (-1)*(cursor[1] - gun_bottom[1])
    if dx == 0:
        dx = 1
    angle = math.atan(dy/dx)
    x = gun_len * math.cos(angle)
    y = HEIGHT/2 - gun_len * math.sin(angle)
    return [x, y], angle


def new_bullet(gun_top):
    '''
    Функция обеспечивает возникновение шарика-снаряда
    '''
    x = int(gun_top[0])
    y = int(gun_top[1])
    circle(screen, CYAN, (x, y), rad_bullet)
    circle(screen, BLACK, (x, y), rad_bullet, 1)
    return [x, y]


def hit(bullet, target_list, rad_bullet, points):
    '''
    Функция проверяет, произошло ли попадание пули в мишень
    '''
    for target in target_list:
        if (bullet[0] - target[0])**2 + (bullet[1] - target[1])**2 <= (target[2] + rad_bullet)**2:
            target_list = target_delete(target_list, target)
            points += 1
    return target_list, points



def moving_bullet(bullet, g):
    '''
    Функция обеспечивает полет шарика-снаряда
    '''
    x = bullet[0]
    y = bullet[1]
    vx = int(bullet[2])
    vy = int(bullet[3])
    rad = bullet[4]
    color = bullet[5]
    wall_hits = bullet[6]

    if x >= WIDTH - rad:
        vx = vx * (-1) * 0.75
        vy = vy * 0.9
        x = WIDTH - rad - 1
        wall_hits += 1
    elif y >= HEIGHT - rad:
        vy = vy * (-1) * 0.75
        vx = vx * 0.9
        y = HEIGHT - rad - 1
        wall_hits += 1
    elif rad >= x:
        vx = vx * (-1) * 0.75
        vy = vy * 0.9
        x = rad + 1
        wall_hits += 1
    elif rad >= y:
        vy = vy * (-1) * 0.75
        vx = vx * 0.9
        y = rad + 1
        wall_hits += 1

    x += vx
    y -= vy
    vy -= g

    if wall_hits >= 15:
        bullet_list.pop(bullet_list.index(bullet))
    else:
        bullet[0] = x
        bullet[1] = y
        bullet[2] = vx
        bullet[3] = vy
        bullet[6] = wall_hits
        circle(screen, color, (int(x), int(y)), rad)
        circle(screen, BLACK, (int(x), int(y)), rad, 1)
        return bullet


def points_table(points):
    '''
    Функция обеспечивает работу счетчика очков
    '''
    my_font = pygame.font.Font(None, 50)
    string = "Счёт: " + str(points)
    text = my_font.render(string, 1, BLACK)
    screen.blit(text, (5, 3))


def shots_table(shots):
    '''
    Функция обеспечивает работу счетчика очков
    '''
    my_font = pygame.font.Font(None, 50)
    string = "Выстрелов: " + str(shots)
    text = my_font.render(string, 1, BLACK)
    screen.blit(text, (WIDTH - 250, 3))


clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEMOTION:
            gun_top, angle = gun_turning(list(pygame.mouse.get_pos()), gun_bottom, gun_len)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            shots = shots + 1
            flag = 0
            color = RED
            gun_len = min_gun_len
            bullet = [new_bullet(gun_top)[0], new_bullet(gun_top)[1], power*math.cos(angle), power*math.sin(angle), rad_bullet, CYAN, 0]
            list.append(bullet_list, bullet)

    if flag == 1:
        gun_top, angle = gun_turning(list(pygame.mouse.get_pos()), gun_bottom, gun_len)
        gun_drawing(gun_bottom, gun_top, RED)
        if gun_len < max_gun_len:
            gun_len = gun_len + 1
            power = power + 1
    else:
        gun_drawing(gun_bottom, gun_top, BLACK)
        gun_len = min_gun_len
        power = min_power

    for bullet in bullet_list:
        target_list, points = hit(bullet, target_list, rad_bullet, points)
        moving_bullet(bullet, g)

    for target in target_list:
        moving_target(target)

    points_table(points)
    shots_table(shots)

    pygame.display.update()
    screen.fill(WHITE)


    rect(screen, GREY, (0, HEIGHT -sc_line, WIDTH, sc_line))

pygame.quit()