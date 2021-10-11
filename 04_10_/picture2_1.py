import pygame
from math import pi, cos, sin

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
    def draw_background(sky_color, grass_color):
        pygame.draw.rect(screen, sky_color, [0, 0, 500, 255])
        pygame.draw.rect(screen, grass_color, [0, 255, 500, 255])

    # Дом
    def draw_house(contour_color, house_color):
        pygame.draw.rect(screen, contour_color, [69, 169, 152, 152], 1)
        pygame.draw.rect(screen, house_color, [70, 170, 150, 150])

    # Окно
    def draw_window(window_color):
        pygame.draw.rect(screen, window_color, [113, 205, 65, 65])

    # Крыша
    def draw_roof(contour_color, roof_color):
        pygame.draw.polygon(screen, contour_color, [[145, 90], [70, 169], [220, 169]])
        pygame.draw.polygon(screen, roof_color, [[145, 92], [72, 168], [218, 168]])

    # Тучки
    def draw_clouds(contour_color, clouds_color):
        for i in range(200, 291, 30):
            pygame.draw.circle(screen, contour_color, [i, 60], 25)
            pygame.draw.circle(screen, clouds_color, [i, 60], 24)

        for i in range(230, 261, 30):
            pygame.draw.circle(screen, contour_color, [i, 40], 25)
            pygame.draw.circle(screen, clouds_color, [i, 40], 24)

    # Ствол дерева
    def draw_trunk(trunk_color):
        pygame.draw.rect(screen, trunk_color, [350, 230, 20, 100])

    # Листья
    def draw_leaves(contour_color, leaves_color):
        pygame.draw.circle(screen, contour_color, [360, 170], 22)
        pygame.draw.circle(screen, leaves_color, [360, 170], 21)
        pygame.draw.circle(screen, contour_color, [340, 190], 22)
        pygame.draw.circle(screen, leaves_color, [340, 190], 21)
        pygame.draw.circle(screen, contour_color, [380, 190], 22)
        pygame.draw.circle(screen, leaves_color, [380, 190], 21)
        pygame.draw.circle(screen, contour_color, [360, 210], 22)
        pygame.draw.circle(screen, leaves_color, [360, 210], 21)

        pygame.draw.circle(screen, contour_color, [340, 230], 22)
        pygame.draw.circle(screen, leaves_color, [340, 230], 21)
        pygame.draw.circle(screen, contour_color, [380, 230], 22)
        pygame.draw.circle(screen, leaves_color, [380, 230], 21)

    # Вспомогательная фуекцимя для рисования солнца
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

    # Солнце
    def draw_sun(contour_color, sun_color):
        pygame.draw.polygon(screen, contour_color, sun_(420, 80, 24, 41))
        pygame.draw.polygon(screen, sun_color, sun_(420, 80, 24, 40))


    draw_background(Blue, Green)
    draw_house(Black, Brown)
    draw_window(BlueWindow)
    draw_roof(Black, Red)
    draw_clouds(Black, White)
    draw_trunk(Black)
    draw_leaves(Black, GreenTrees)
    draw_sun(Black, Pink)

    pygame.display.flip()

pygame.quit()
