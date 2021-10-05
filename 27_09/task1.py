import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255,0), (200, 200), 100)
line(screen, (0, 0, 0), (140, 250), (260, 250), 8)
circle(screen, (255, 0, 0), (160, 170), 20)
circle(screen, (255, 0, 0), (240, 170), 10)
circle(screen, (0 , 0 , 0), (160, 170), 10)
circle(screen, (0, 0, 0), (240, 170), 5)
line(screen, (0 , 0, 0), (180, 160), (120, 120),10)
line(screen, (0, 0, 0), (210, 175), (260, 145), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()