import os
import pygame
from constant import SCREEN_WIDTH
from init import screen


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