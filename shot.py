import pygame
import math
import random

class Shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/lazer.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = self.image.get_rect()

        #Velocidade do Tiro
        self.speed = 4

    def update(self, *args, **kwargs):
        #LOGICA dos Tiros
        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()



