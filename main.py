# IMPORT LIBRARIES

import pygame
import random
from sys import exit
from player import Player
from platform_manager import Platform
from support import *


class Game:
    def __init__(self):
        self.width = WIDTH  # Width of display surface
        self.height = HEIGHT  # Height of display surface
        self.title = TITLE  # Title of display
        self.fps = FPS  # Framerate

        # START PYGAME
        pygame.init()

        # CONTROL THE FRAMERATE
        self.clock = pygame.time.Clock()

        # Activate GAME WINDOW
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        # LOAD IMAGES
        self.bg_image = pygame.image.load("assets/bg.png").convert_alpha()

        # INITIALIZE PLAYER
        self.jumpy = Player(self.width // 2, self.height - 150)

        # CREATE SPRITE GROUPS
        self.platform_group = pygame.sprite.Group()

        # CREATE TEMPORARY PLATFORMS - The first 10
        for p in range(MAX_PLATFORMS):
            p_w = random.randint(40, 60)  # random platform width
            p_x = random.randint(0, WIDTH - p_w)  # random x of platform (0, Width - platform width)
            p_y = p * random.randint(80, 120)
            platform = Platform(p_x, p_y, p_w)
            self.platform_group.add(platform)

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

    def update(self):
        # Any game logic updates would go here
        self.jumpy.move(self.platform_group)

    def render(self):
        # Any rendering/drawing updates would go here
        # DRAW BACKGROUND
        self.screen.blit(self.bg_image, (0, 0))

        # DRAW PLAYER
        self.jumpy.render(self.screen)

        # DRAW SPRITES
        self.platform_group.draw(self.screen)

        # UPDATE DISPLAY
        pygame.display.update()

    def quit_game(self):
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = Game()
    game.run()
