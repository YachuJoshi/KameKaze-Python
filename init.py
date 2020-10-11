import os
import pygame
from constant import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame import mixer

# Init pygame
pygame.init()

# Initialize window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title & Icon
pygame.display.set_caption("KameKaze")
icon = pygame.image.load(os.path.join("images", "spaceship.png"))
pygame.display.set_icon(icon)

# Background image & sound
backgroundImg = pygame.image.load(os.path.join("images", "clouds.jpg"))
mixer.music.load(os.path.join("sounds", "background.wav"))
mixer.music.play(-1)

# Sound effects
bullet_sound = mixer.Sound(os.path.join("sounds", "laser.wav"))
explosion_sound = mixer.Sound(os.path.join("sounds", "explosion.wav"))

# For fps
clock = pygame.time.Clock()