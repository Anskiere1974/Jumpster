# IMPORT LIBRARIES
import pygame
from support import *


class Player:
    def __init__(self, posx, posy):
        # Prepare image for blitting
        jumpy_image = pygame.image.load("assets/jump.png").convert_alpha()  # zur Skalierung vorbereiten
        self.image = pygame.transform.scale(jumpy_image, (45, 45))  # Hier wird das Bild auf die gewünschte Größe skaliert
        self.width = 25
        self.height = 40
        # self.rect = self.image.get_rect()  # usual way, but we want to tweak the collision box
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (posx, posy)

        self.vel_y = 0
        self.flip = False

    def move(self):
        # reset variables at beginning of every frame
        dx = 0
        dy = 0

        # process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -10
            self.flip = True  # flip the image when going to the left
        if key[pygame.K_d]:
            dx = 10
            self.flip = False

        # Gravity - with every frame the char falls faster
        self.vel_y += GRAVITY
        dy += self.vel_y

        # preemptive border collision check
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left
        if self.rect.right + dx > WIDTH:
            dx = WIDTH - self.rect.right

        # check collision with ground
        if self.rect.bottom + dy > HEIGHT:
            dy = 0
            self.vel_y = -20

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def render(self, _screen):
        # _screen.blit(self.image, self.rect) usual way, but we are tweaking the collision box
        # _screen.blit(self.image, (self.rect.x-12, self.rect.y-5))  #more tweaking on collision box
        # this third version will flip the image with the boolean of self.flip
        _screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))  # more tweaking on collision box
        pygame.draw.rect(_screen, WHITE, self.rect, 2)
