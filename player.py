import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("date/player.png")
        self.image = pygame.transform.scale(self.image, [60, 60])
        self.rect = pygame.Rect(500, 420, 60, 60)


    def update (self, *args):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.rect.x -= 5
            elif keys[pygame.K_d]:
                self.rect.x += 5