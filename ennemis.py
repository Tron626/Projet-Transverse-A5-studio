import pygame

class ennemi(pygame.sprite.Sprite):
    def __init__(self):
        self.pv = 100
        self.pv_max = 100
        self.image = pygame.image.load('Asset/Joueur/peso provi.png') # metre skin
        self.rect = self.image.get_rect()
        self.x = 900
        self.y = 400
        self.pos = 900
        self.vit = 1/2

    def mouv(self):
        if self.pos>10:
            self.pos-=self.vit

    def perdu(self):
        if self.pos<=50:
            return True
        return False
