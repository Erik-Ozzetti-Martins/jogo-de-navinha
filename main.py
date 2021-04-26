import random

import pygame

from inimigo import Inimigo
from inimigos2 import Inimigos2
from player import Player
from shot import Shot

pygame.init()




display = pygame.display.set_mode((640, 480))
pygame.display.set_caption("asterx")

objectGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()
inimigoGroup = pygame.sprite.Group()
inimigos2Group = pygame.sprite.Group()


bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("date/background.png")
bg.image = pygame.transform.scale(bg.image, [640, 480]).convert()
bg.rect = bg.image.get_rect()

player = Player(objectGroup)

pygame.mixer.music.load("date/bottom.ogg")
pygame.mixer.music.play(-2)





shot = pygame.mixer.Sound("date/boom1.wav")

gameLoop = True
clock = pygame.time.Clock()
timer = 0

pontos = 0
pygame.font.init()
fonte = pygame.font.SysFont('bahnschrift', 28)
mensagem = f'pontos {pontos}'
tento_form = fonte.render(mensagem, False, (255, 255, 255))
if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)
        mensagem = f'pontos {pontos}'
        tento_form = fonte.render(mensagem, False,(255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shot.play()
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = player.rect.center




        objectGroup.update()
        clock.tick(60)

        timer += 1
        if timer > 30:
                
            if random.random() < 0.2:
                newinimigo = Inimigo(objectGroup, inimigoGroup)
                newinimigo2= Inimigos2(objectGroup,inimigos2Group)
                

        collisions = pygame.sprite.spritecollide(player, inimigoGroup, False)
        collisions2 = pygame.sprite.spritecollide(player, inimigos2Group, False)
        if collisions or collisions2:
            gameLoop = False


        hits = pygame.sprite.groupcollide(shotGroup, inimigoGroup, True, True, pygame.sprite.collide_mask)
        hit = pygame.sprite.groupcollide(shotGroup, inimigos2Group, True, True, pygame.sprite.collide_mask)
        if hits or hit :
            hits
            hit
            pontos += 5





        display.fill([46, 46, 46])
        objectGroup.draw(display)
        display.blit(tento_form, (0,0))

        pygame.display.update()