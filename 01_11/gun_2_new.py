import random as rnd
import math
import pygame

FPS = 60
g = 9.8
screen_width, screen_height = 800, 600
scale = screen_width / 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
COLORS = [BLUE, CYAN, GREEN, MAGENTA]


class Gun:
    max_power = 3
    min_v = 5 * scale
    length = 50
    thickness = 20
    height = 50
    gun_v = 5 * scale

    def __init__(self, x, y):
        self.power = 0
        self.on = False
        self.x = x
        self.y = y
        self.shell_num = 10
        self.direction = math.pi / 4
        self.color = BLACK
        self.moving_dest = "NONE"
        self.is_alive = True

    def aim(self, pos):
        if self.is_alive:
            x = pos[0] - self.x
            y = self.y - pos[1] - Gun.height
            if x != 0:
                direction = math.atan(y / x)
            else:
                direction = math.pi / 2
            if x >= 0:
                self.direction = max(0, direction)
            else:
                self.direction = min(math.pi, direction + math.pi)
            if self.on:
                self.power += Gun.max_power / FPS
            if self.power > Gun.max_power:
                self.power = Gun.max_power

    def fire(self):
        if self.is_alive:
            if self.shell_num > 0:
                self.shell_num -= 1
                length = Gun.length
                x, y = (
                    self.x + length * math.cos(self.direction),
                    self.y - length * math.sin(self.direction) - Gun.height / 2)
                vx = Gun.min_v * (self.power + 1) * math.cos(self.direction)
                vy = Gun.min_v * (self.power + 1) * math.sin(self.direction)
                projectile = Shell(x, y, vx, -vy, self.color)
                return projectile

    def draw(self):
        if self.is_alive:
            self.color = (self.power * 255 / Gun.max_power, 0, 0)
            half = Gun.thickness / 2
            length = Gun.length
            cos = math.cos(self.direction)
            sin = math.sin(self.direction)
            pos1 = (self.x - half * sin, self.y - half * cos - Gun.height / 2)
            pos2 = (self.x - half * sin + length * cos, self.y - half * cos - length * sin - Gun.height / 2)
            pos3 = (self.x + half * sin + length * cos, self.y + half * cos - length * sin - Gun.height / 2)
            pos4 = (self.x + half * sin, self.y + half * cos - Gun.height / 2)
            pos5 = (self.x - Gun.height / 2, self.y)
            pos6 = (self.x - Gun.height / 2, self.y - Gun.height)
            pos7 = (self.x + Gun.height / 2, self.y - Gun.height)
            pos8 = (self.x + Gun.height / 2, self.y)
            pygame.draw.polygon(screen, self.color, [pos1, pos2, pos3, pos4])
            pygame.draw.polygon(screen, BLACK, [pos5, pos6, pos7, pos8])

    def move(self, dt=1 / FPS):
        if self.moving_dest == "LEFT" and self.x > Gun.height / 2:
            self.x -= Gun.gun_v * dt
        elif self.moving_dest == "RIGHT" and self.x < screen_width - Gun.height / 2:
            self.x += Gun.gun_v * dt


class Shell:
    s_radius = 10

    def __init__(self, x, y, vx, vy, color):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.r = Shell.s_radius
        self.color = color
        self.is_alive = True

    def move(self, dt=1 / FPS):
        ax, ay = 0, g * scale
        self.x += self.vx * dt + ax * (dt ** 2) / 2
        self.y += self.vy * dt + ay * (dt ** 2) / 2
        self.vx += ax * dt
        self.vy += ay * dt
        if self.y >= screen_height * 4 / 5 - self.r:
            if abs(self.vx) <= 5 * scale and abs(self.vy) <= 5 * scale:
                self.is_alive = False
            self.y = screen_height * 4 / 5 - self.r
            if self.vx >= 0:
                self.vx = max(0, self.vx - 0.2 * self.vy)
            else:
                self.vx = min(0, self.vx + 0.2 * self.vy)
            self.vy = -self.vy / 2
        if not (0 - self.r < self.x < screen_width + self.r):
            self.is_alive = False

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.r))

    def detect_collision(self, other):
        length = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return length <= self.r + other.r


class Target:
    t_radius = 15

    def __init__(self, x, y, vx, vy, color=None):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.r = Target.t_radius
        if color is None:
            self.color = COLORS[rnd.randint(0, len(COLORS) - 1)]
        else:
            self.color = color
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
        if self.y >= screen_height * 4 / 5 - self.r:
            self.y = screen_height * 4 / 5 - self.r
            self.vy = -self.vy
        if self.y <= 0 + self.r:
            self.y = 0 + self.r
            self.vy = -self.vy

    def collide(self, other):
        if other.detect_collision(self):
            self.is_alive = False


class CommonTarget(Target):

    def __init__(self, x, y, vx, vy):
        super().__init__(x, y, vx, vy)

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(round(self.x)), int(round(self.y))), self.r)


class Cloud(Target):
    max_cd = 1

    def __init__(self, x, y, vx):
        super().__init__(x, y, vx, 0, color=RED)
        self.r = Target.t_radius * 2
        self.cd = rnd.uniform(0, 3*Cloud.max_cd)

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(round(self.x)), int(round(self.y))), self.r)

    def fire(self):
        self.cd = Cloud.max_cd
        bomb = Bomb(self.x, self.y)
        return bomb


class Bomb:
    b_radius = 15

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v = 0
        self.r = Bomb.b_radius
        self.is_alive = True

    def move(self, dt=1 / FPS):
        self.v += g * scale * dt
        self.y += self.v * dt
        if self.y >= screen_height:
            self.is_alive = False

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), int(self.r))


def generate_random_common_targets(number: int):
    common_targets = []
    for i in range(number):
        x = rnd.randint(0, screen_width)
        y = rnd.randint(0, screen_height*4/5)
        v = rnd.randint(30, 60)
        angle = rnd.randint(0, 360)
        vx = v * math.cos(angle / (2 * math.pi))
        vy = v * math.sin(angle / (2 * math.pi))
        target = CommonTarget(x, y, vx, vy)
        common_targets.append(target)
    return common_targets


def generate_random_clouds(number: int):
    clouds = []
    for i in range(number):
        x = screen_width / (i + 1)
        y = rnd.randint(0, screen_height*2/5)
        v = rnd.randint(20, 80)
        cloud = Cloud(x, y, v)
        clouds.append(cloud)
    return clouds


def movement(gun, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            if gun.moving_dest == "NONE":
                gun.moving_dest = "RIGHT"
            else:
                gun.moving_dest = "NONE"
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            if gun.moving_dest == "NONE":
                gun.moving_dest = "LEFT"
            else:
                gun.moving_dest = "NONE"

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            if gun.moving_dest == "RIGHT":
                gun.moving_dest = "NONE"
            else:
                gun.moving_dest = "LEFT"
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            if gun.moving_dest == "LEFT":
                gun.moving_dest = "NONE"
            else:
                gun.moving_dest = "RIGHT"


def game_main_loop():
    common_targets = generate_random_common_targets(10)
    clouds = generate_random_clouds(2)
    gun = Gun(screen_width / 2, screen_height*4/5)
    clock = pygame.time.Clock()
    projectiles = []
    bombs = []
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
                if gun.shell_num > 0 and gun.is_alive:
                    projectiles.append(gun.fire())
                gun.power = 0
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                movement(gun, event)

        pygame.display.update()
        screen.fill(WHITE)
        # draw ground
        pygame.draw.polygon(screen, GRAY, (
            (0, screen_height * 4 / 5), (screen_width, screen_height * 4 / 5), (screen_width, screen_height),
            (0, screen_height)), 0)
        gun.move()
        gun.aim(pygame.mouse.get_pos())
        gun.draw()
        for common_target in common_targets:
            common_target.move(1 / FPS)
        for cloud in clouds:
            cloud.move(1 / FPS)
            cloud.cd = max(0, cloud.cd - 1 / FPS)
            if cloud.cd == 0:
                bombs.append(cloud.fire())
        for bomb in bombs:
            bomb.move(1 / FPS)
            if (gun.x - Gun.height / 2 - bomb.r < bomb.x < gun.x + Gun.height / 2 + bomb.r) and (
                    gun.y - bomb.r < bomb.y < gun.y + Gun.height + bomb.r):
                gun.is_alive = False
        for projectile in projectiles:
            projectile.move(1 / FPS)
            for common_target in common_targets:
                common_target.collide(projectile)

        for common_target in common_targets:
            if not common_target.is_alive:
                common_targets.remove(common_target)
        for cloud in clouds:
            if not cloud.is_alive:
                clouds.remove(cloud)
        for bomb in bombs:
            if not bomb.is_alive:
                bombs.remove(bomb)
        for projectile in projectiles:
            if not projectile.is_alive:
                projectiles.remove(projectile)

        for common_target in common_targets:
            common_target.draw()
        for cloud in clouds:
            cloud.draw()
        for bomb in bombs:
            bomb.draw()
        for projectile in projectiles:
            projectile.draw()

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.update()

    game_main_loop()