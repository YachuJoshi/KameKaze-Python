import os
import pygame
from init import screen


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 24
        self.width = 24
        self.dy = 8
        self.image = pygame.image.load(os.path.join("images", "bullet.png"))

    def draw(self):
        screen.blit(self.image, (round(self.x), round(self.y)))

    def update(self):
        self.y -= self.dy