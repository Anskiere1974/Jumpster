import pygame
from support import HEIGHT


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        platform_image = pygame.image.load("assets/wood.png").convert_alpha()
        self.image = pygame.transform.scale(platform_image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        # update platforms vertical position
        self.rect.y += scroll

        # check if platform has gone off the screen
        if self.rect.top > HEIGHT:
            self.kill()
