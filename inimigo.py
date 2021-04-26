import pygame
import random


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("date/enemy.png")
        self.image = pygame.transform.scale(self.image, [40, 40])
        self.rect = pygame.Rect(0, 40, 40, 40)

        self.rect.x = 740 +random.randint(50, 300)
        self.rect.y =random.randint(50, 300)

        self.speed = 3 + random.random () * 2


    def update (self, *args):
        self.rect. x -= self.speed


        if self.rect.right < 0:
            self.kill()