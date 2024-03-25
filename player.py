# IMPORT LIBRARIES
import pygame


class Player:
    def __init__(self, posx, posy):
        # Prepare image for blitting
        self.image = pygame.image.load("assets/jump.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)

    def update(self):
        pass

    def render(self, _screen):
        _screen.blit(self.image, self.rect)
