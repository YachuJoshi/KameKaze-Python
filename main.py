import os
import pygame
import random
import math

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = (400, 600)
LANES = 3
BLOCK_WIDTH = math.ceil(SCREEN_WIDTH / LANES)
POSSIBLE_X = [(BLOCK_WIDTH * i) + 16 for i in range(LANES)]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("KameKaze")
icon = pygame.image.load(os.path.join("images", "spaceship.png"))
pygame.display.set_icon(icon)

backgroundImg = pygame.image.load(os.path.join("images", "clouds.jpg"))


class Hero:
    def __init__(self):
        self.height = 100
        self.width = 100
        self.x = SCREEN_WIDTH / 2 - self.width / 2
        self.y = 480
        self.health = 2
        self.image = pygame.image.load(os.path.join("images", "batmobile.png"))

    def draw(self):
        screen.blit(self.image, (round(self.x), self.y))

    def move(self, direction):
        if direction == "left":
            if self.x <= 16:
                return
            self.x -= 134
        elif direction == "right":
            if self.x >= 284:
                return
            self.x += 134

    def decrease_health(self):
        self.health -= 1


class Enemy:
    def __init__(self, x, y):
        self.height = 100
        self.width = 100
        self.x = x
        self.dy = 0.5
        self.y = y
        self.health = 2
        self.health_y = y - 45
        self.image = pygame.image.load(os.path.join("images", "enemy.png"))
        self.healthImgFull = pygame.image.load(os.path.join("images", "full-hp.png"))
        self.healthImgHalf = pygame.image.load(os.path.join("images", "half-hp.png"))

    def draw(self):
        screen.blit(self.image, (round(self.x), self.y))
        if self.health > 1:
            screen.blit(self.healthImgFull, (round(self.x - 4), self.health_y))
        else:
            screen.blit(self.healthImgHalf, (round(self.x - 4), self.health_y))

    def update(self):
        self.y += self.dy
        self.health_y += self.dy

    def decrease_health(self):
        self.health -= 1


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 24
        self.width = 24
        self.dy = 1.5
        self.image = pygame.image.load(os.path.join("images", "bullet.png"))

    def draw(self):
        screen.blit(self.image, (round(self.x), self.y))

    def update(self):
        self.y -= self.dy


def create_enemies():
    for position_x in POSSIBLE_X:
        if random.randint(1, 2) < 1.5:
            continue
        enemies.append(Enemy(position_x, 30))


def check_collision(first_item, second_item):
    return (
        first_item.x < second_item.x + second_item.width
        and first_item.x + first_item.width > second_item.x
        and first_item.y < second_item.y + second_item.height
        and first_item.y + first_item.height > second_item.y
    )


hero = Hero()
enemies = []
bullets = []
distance = 0
create_enemies()
running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.move("left")
            elif event.key == pygame.K_RIGHT:
                hero.move("right")

            if event.key == pygame.K_SPACE:
                bullet = Bullet(hero.x + hero.width / 2 - 12, hero.y)
                bullets.append(bullet)

    distance += 1

    if distance % 400 == 0:
        create_enemies()

    hero.draw()

    for bullet in bullets:
        bullet.draw()
        bullet.update()

    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)

    for enemy in enemies:
        enemy.draw()
        enemy.update()
        if check_collision(hero, enemy):
            hero.decrease_health()
            enemies.remove(enemy)

    for enemy in enemies:
        if enemy.y >= SCREEN_HEIGHT or enemy.health <= 0:
            enemies.remove(enemy)

    for enemy in enemies:
        for bullet in bullets:
            if check_collision(enemy, bullet):
                enemy.decrease_health()
                bullets.remove(bullet)

    if hero.health <= 0:
        running = False
    pygame.display.update()