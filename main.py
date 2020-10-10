import os
import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = (400, 600)
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
        self.image = pygame.image.load(os.path.join("images", "batmobile.png"))

    def draw(self):
        screen.blit(self.image, (round(self.x), self.y))


hero = Hero()
running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hero.draw()
    pygame.display.update()