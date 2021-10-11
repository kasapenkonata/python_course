import pygame
from math import pi, cos, sin


def sun_(dx, dy, num_points, radius):
    point_list = []

    for i in range(num_points * 2):
        radius_ = radius
        if i % 2 == 0:
            radius_ = radius - 5

        ang = i * pi / num_points
        x = dx + int(cos(ang) * radius_)
        y = dy + int(sin(ang) * radius_)

        point_list.append((x, y))

    return point_list


pygame.init()

# Цвета, которые мы будем использовать в формате RGB
Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (161, 235, 245)
BlueWindow = (14, 147, 145)
Green = (14, 147, 37)
GreenTrees = (15, 83, 14)
Red = (255, 0, 0)
Pink = (249, 194, 194)
Yellow = (255, 255, 0)
Brown = (147, 107, 14)

# Желаемое количество кадров в секунду
FPS = 30

# Установить высоту и ширину экрана
size = [500, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Картинка 2_1.png")

# Цикл, пока пользователь не нажмет кнопку закрытия.
done = False
clock = pygame.time.Clock()

while not done:

    # Это ограничивает цикл while до 30 раз в секунду.
    clock.tick(FPS)

    for event in pygame.event.get():  # Пользователь что-то сделал
        if event.type == pygame.QUIT:  # Если пользователь нажал кнопку "Закрыть"
            done = True  # Отметить, что мы закончили, поэтому мы выходим из цикла

    # Весь код отрисовки происходит после цикла for, но
    # внутри основного цикла while done == False.

    # Очистить экран и установить фон экрана
    screen.fill(White)

    # Фон картинки
    pygame.draw.rect(screen, Blue, [0, 0, 500, 255])
    pygame.draw.rect(screen, Green, [0, 255, 500, 255])

    # Дом
    pygame.draw.rect(screen, Black, [69, 169, 152, 152], 1)
    pygame.draw.rect(screen, Brown, [70, 170, 150, 150])

    # Окно
    pygame.draw.rect(screen, BlueWindow, [113, 205, 65, 65])

    # Крыша
    pygame.draw.polygon(screen, Black, [[145, 90], [70, 169], [220, 169]])
    pygame.draw.polygon(screen, Red, [[145, 92], [72, 168], [218, 168]])

    # Тучки
    for i in range(200, 291, 30):
        pygame.draw.circle(screen, Black, [i, 60], 25)
        pygame.draw.circle(screen, White, [i, 60], 24)

    for i in range(230, 261, 30):
        pygame.draw.circle(screen, Black, [i, 40], 25)
        pygame.draw.circle(screen, White, [i, 40], 24)

    # Ствол дерева
    pygame.draw.rect(screen, Black, [350, 230, 20, 100])

    # Листья
    pygame.draw.circle(screen, Black, [360, 170], 22)
    pygame.draw.circle(screen, GreenTrees, [360, 170], 21)
    pygame.draw.circle(screen, Black, [340, 190], 22)
    pygame.draw.circle(screen, GreenTrees, [340, 190], 21)
    pygame.draw.circle(screen, Black, [380, 190], 22)
    pygame.draw.circle(screen, GreenTrees, [380, 190], 21)
    pygame.draw.circle(screen, Black, [360, 210], 22)
    pygame.draw.circle(screen, GreenTrees, [360, 210], 21)

    pygame.draw.circle(screen, Black, [340, 230], 22)
    pygame.draw.circle(screen, GreenTrees, [340, 230], 21)
    pygame.draw.circle(screen, Black, [380, 230], 22)
    pygame.draw.circle(screen, GreenTrees, [380, 230], 21)

    # Солнце
    pygame.draw.polygon(screen, Black, sun_(420, 80, 24, 41))
    pygame.draw.polygon(screen, Pink, sun_(420, 80, 24, 40))

    pygame.display.flip()

pygame.quit()