import pygame
import random
from init import *
from constant import POSSIBLE_X
from hero import Hero
from enemy import Enemy
from bullet import Bullet


class Game:
    def __init__(self):
        self.hero = Hero()
        self.enemies = []
        self.bullets = []
        self.distance = 0
        self.score_font = pygame.font.Font("freesansbold.ttf", 16)
        self.game_over_font = pygame.font.Font("freesansbold.ttf", 32)
        self.health_font = pygame.font.Font("freesansbold.ttf", 16)

    def init(self):
        self.create_enemies()

    def show_health_bar(self):
        health_bar = self.health_font.render(
            f"Health: {self.hero.health}", True, (255, 255, 255)
        )
        screen.blit(health_bar, (300, 16))

    def show_score(self):
        score = self.score_font.render(f"Score: {self.distance}", True, (255, 255, 255))
        screen.blit(score, (16, 16))

    def game_over_screen(self):
        score = self.game_over_font.render(
            f"Final Score: {self.distance}", True, (255, 255, 255)
        )
        screen.blit(
            score,
            (round(SCREEN_WIDTH / 2 - 132), round(SCREEN_HEIGHT / 2 - 15)),
        )

    def create_enemies(self):
        for position_x in POSSIBLE_X:
            if random.randint(1, 2) < 1.5:
                continue
            self.enemies.append(Enemy(position_x, 30))

    def check_collision(self, first_item, second_item):
        return (
            first_item.x < second_item.x + second_item.width
            and first_item.x + first_item.width > second_item.x
            and first_item.y < second_item.y + second_item.height
            and first_item.y + first_item.height > second_item.y
        )

    def start(self):
        self.init()
        running = True
        game_over = False

        while running:
            screen.fill((0, 0, 0))
            screen.blit(backgroundImg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.hero.move("left")
                    elif event.key == pygame.K_RIGHT:
                        self.hero.move("right")

                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(
                            self.hero.x + self.hero.width / 2 - 12, self.hero.y
                        )
                        bullet_sound.play()
                        self.bullets.append(bullet)

            self.distance += 1

            if self.distance % 100 == 0:
                self.create_enemies()

            self.hero.draw()

            for bullet in self.bullets:
                bullet.draw()
                bullet.update()

            for bullet in self.bullets:
                if bullet.y <= 0:
                    self.bullets.remove(bullet)

            for enemy in self.enemies:
                enemy.draw()
                enemy.update()
                if self.check_collision(self.hero, enemy):
                    self.hero.decrease_health()
                    self.enemies.remove(enemy)

            for enemy in self.enemies:
                if enemy.y >= SCREEN_HEIGHT or enemy.health <= 0:
                    self.enemies.remove(enemy)
                    if enemy.health <= 0:
                        explosion_sound.play()

            for enemy in self.enemies:
                for bullet in self.bullets:
                    if self.check_collision(enemy, bullet):
                        enemy.decrease_health()
                        self.bullets.remove(bullet)

            if self.hero.health <= 0:
                running = False
                game_over = True

            self.show_score()
            self.show_health_bar()
            pygame.display.update()
            clock.tick(60)

        while game_over:
            screen.fill((0, 0, 0))
            self.game_over_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False

            pygame.display.update()
