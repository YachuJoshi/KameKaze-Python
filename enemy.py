import os
import pygame
from init import screen

class Enemy:
    def __init__(self, x, y):
        self.height = 100
        self.width = 100
        self.x = x
        self.dy = 2
        self.y = y
        self.health = 2
        self.health_y = y - 45
        self.image = pygame.image.load(os.path.join("images", "enemy.png"))
        self.healthImgFull = pygame.image.load(os.path.join("images", "full-hp.png"))
        self.healthImgHalf = pygame.image.load(os.path.join("images", "half-hp.png"))

    def draw(self):
        screen.blit(self.image, (round(self.x), round(self.y)))
        if self.health > 1:
            screen.blit(self.healthImgFull, (round(self.x - 4), round(self.health_y)))
        else:
            screen.blit(self.healthImgHalf, (round(self.x - 4), round(self.health_y)))

    def update(self):
        self.y += self.dy
        self.health_y += self.dy

    def decrease_health(self):
        self.health -= 1