# IMPORT LIBRARIES
import pygame
from sys import exit
from player import Player
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
        self.jumpy.move()

    def render(self):
        # Any rendering/drawing updates would go here
        # DRAW BACKGROUND
        self.screen.blit(self.bg_image, (0, 0))

        # DRAW PLAYER
        self.jumpy.render(self.screen)

        # UPDATE DISPLAY
        pygame.display.update()

    def quit_game(self):
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = Game()
    game.run()
