import random as rnd
import math
import pygame

FPS = 60
g = 9.8
screen_width = 800
screen_height = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
COLORS = [BLUE, YELLOW, GREEN]

class Target():
    rad = 20

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = Target.rad
        self.color = COLORS[rnd.randint(0, 2)]
        self.is_alive = True

    def move(self, dt):
        ax, ay = 0, 0
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vx += ax * dt
        self.vy += ay * dt
        if self.x >= screen_width - self.r:
            self.x = screen_width - self.r
            self.vx = -self.vx
        if self.x <= 0 + self.r:
            self.x = 0 + self.r
            self.vx = -self.vx
        if self.y >= screen_height - self.r:
            self.y = screen_height - self.r
            self.vy = -self.vy
        if self.y <= 0 + self.r:
            self.y = 0 + self.r
            self.vy = -self.vy

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(round(self.x)), int(round(self.y))), self.r)

    def collide(self, other):
        if other.detect_collision(self):
            self.is_alive = False

class Gun():
    max_power = 5
    min_v = 25
    length = 50
    height = 10

    def __init__(self, x, y):
        self.power = 0
        self.on = False
        self.x = x
        self.y = y
        self.Bomb_num = 10
        self.direction = math.pi / 4
        self.color = WHITE

    def aim(self, pos):
        x = pos[0] - self.x
        y = self.y - pos[1]
        if x != 0:
            self.direction = math.atan(y / x)
        else:
            self.direction = math.pi / 2
        if self.on:
            self.power += Gun.max_power / FPS
        if self.power > Gun.max_power:
            self.power = Gun.max_power

    def fire(self):
        if self.Bomb_num > 0:
            self.Bomb_num -= 1
            length = Gun.length
            x, y = (self.x + length * math.cos(self.direction), self.y - length * math.sin(self.direction))
            vx = Gun.min_v * (self.power + 1) * math.cos(self.direction)
            vy = Gun.min_v * (self.power + 1) * math.sin(self.direction)
            projectile = Bomb(x, y, vx, -vy)
            return projectile

    def draw(self):
        color = (255, (Gun.max_power - self.power) * 255 / Gun.max_power, (Gun.max_power - self.power) * 255 / Gun.max_power)
        half = Gun.height / 2
        length = Gun.length
        pos1 = (self.x - half * math.sin(self.direction), self.y - half * math.cos(self.direction))
        pos2 = (self.x - half * math.sin(self.direction) + length * math.cos(self.direction),
                self.y - half * math.cos(self.direction) - length * math.sin(self.direction))
        pos3 = (self.x + half * math.sin(self.direction) + length * math.cos(self.direction),
                self.y + half * math.cos(self.direction) - length * math.sin(self.direction))
        pos4 = (self.x + half * math.sin(self.direction), self.y + 10 * math.cos(self.direction))
        pygame.draw.polygon(screen, color, [pos1, pos2, pos3, pos4])


class Bomb():
    standard_radius = 25

    def __init__(self, x, y, vx, vy):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.r = Bomb.standard_radius
        self.is_alive = True


    def check_corners(self, refl_y=0.8, refl_x=0.9):
        if self.x >= screen_width - self.r:
            self.vx = -(self.vx * refl_x)
        if self.x <= self.r:
            self.vx = - (self.vx * refl_x)
        if self.y >= screen_height - self.r:
            self.vy = -(self.vy * refl_y)
        if self.y <= self.r:
            self.vy = -(self.vy * refl_y)

    def move(self, dt):
        dt = 15 / FPS
        ax = 0
        ay = g
        self.x += self.vx * dt + ax * (dt ** 2) / 2
        self.y += self.vy * dt + ay * (dt ** 2) / 2
        self.vx += ax * dt
        self.vy += ay * dt
        self.check_corners()
        if not (self.x in (0 + self.r, screen_width - self.r) and self.y in (0 + self.r, screen_height - self.r)):
            self.deleted = True

    def draw(self):
        pygame.draw.circle(screen, RED, (int(round(self.x)), int(round(self.y))), self.r)

    def detect_collision(self, other):
            length = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
            return length <= self.r + other.r


def generate_random_targets(number: int):
    targets = []
    for i in range(number):
        x = rnd.randint(0, screen_width)
        y = rnd.randint(0, screen_height)
        v = rnd.randint(30, 60)
        angle = rnd.randint(0, 360)
        vx = v * math.cos(angle / (2 * math.pi))
        vy = v * math.sin(angle / (2 * math.pi))
        target = Target(x, y, vx, vy)
        targets.append(target)
    return targets


def game_main_loop():
    targets = generate_random_targets(10)
    gun = Gun(0, 300)
    clock = pygame.time.Clock()
    projectiles = []
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.on = True
            elif event.type == pygame.MOUSEBUTTONUP:
                gun.on = False
                if gun.Bomb_num > 0:
                    projectiles.append(gun.fire())
                gun.power = 0
        pygame.display.update()
        screen.fill(BLACK)
        gun.aim(pygame.mouse.get_pos())
        gun.draw()
        for target in targets:
            target.move(1 / FPS)

        for target in targets:
            target.draw()

        for projectile in projectiles:
            projectile.move(1 / FPS)
        for projectile in projectiles:
            projectile.draw()

        for target in targets:
            for projectile in projectiles:
                target.collide(projectile)

        for target in targets:
            if not target.is_alive:
                targets.remove(target)
        for projectile in projectiles:
            if not projectile.is_alive:
                projectiles.remove(projectile)

        for target in targets:
            target.draw()
        for projectile in projectiles:
            projectile.draw()


    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.update()


game_main_loop()