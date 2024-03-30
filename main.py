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
        self.scroll = scroll
        self.bg_scroll = bg_scroll
        self.game_over = game_over
        self.score = score

        # START PYGAME
        pygame.init()

        # CONTROL THE FRAMERATE
        self.clock = pygame.time.Clock()

        # Activate GAME WINDOW
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        # LOAD IMAGES
        self.bg_image = pygame.image.load("assets/bg.png").convert_alpha()

        # DEFINE FONTS
        self.font_small = pygame.font.SysFont("Lucida Sans", 20)
        self.font_big = pygame.font.SysFont("Lucida Sans", 24)

        # INITIALIZE PLAYER
        self.jumpy = Player(self.width // 2, self.height - 150)

        # CREATE SPRITE GROUPS
        self.platform_group = pygame.sprite.Group()

        # CREATE STARTING PLATFORM
        platform = Platform(self.width // 2 - 50, self.height - 50, 100)
        self.platform_group.add(platform)

    def run(self):
        while True:
            self.handle_events()
            self.clock.tick(self.fps)

            if not self.game_over:
                self.update()
                self.render()
            else:
                print("Hello")
                self.draw_text("GAME OVER!", self.font_big, WHITE, 130, 200)
                self.draw_text("SCORE: " + str(self.score), self.font_big, WHITE, 130, 250)
                self.draw_text("PRESS SPACE TO PLAY AGAIN", self.font_big, WHITE, 40, 300)
                self.restart_game()

                # UPDATE DISPLAY
                pygame.display.update()

    def restart_game(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            # reset variables
            self.game_over = False
            self.score = 0
            self.scroll = 0

            # reposition jumpy
            self.jumpy.rect.center = (self.width // 2, self.height - 150)

            # reset platforms
            self.platform_group.empty()

            # CREATE STARTING PLATFORM
            platform = Platform(self.width // 2 - 50, self.height - 50, 100)
            self.platform_group.add(platform)

    # OUTPUTTING TEXT ON THE SCREEN
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    # FUNCTION FOR DRAWING SCROLLING BACKGROUND
    def draw_bg(self, _bg_scroll):
        self.screen.blit(self.bg_image, (0, 0 + _bg_scroll))
        self.screen.blit(self.bg_image, (0, 0 - self.height + _bg_scroll))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

    def update(self):
        # Any game logic updates would go here
        self.scroll = self.jumpy.move(self.platform_group)

        # generate platforms
        if len(self.platform_group) < MAX_PLATFORMS:
            p_w = random.randint(40, 60)
            p_x = random.randint(0, self.width - p_w)
            p_y = self.platform_group.sprites()[-1].rect.y - random.randint(80, 120)
            platform = Platform(p_x, p_y, p_w)
            self.platform_group.add(platform)

        # update platforms for scrolling
        self.platform_group.update(self.scroll)

        # check for game over
        if self.jumpy.rect.top > self.height:
            self.game_over = True

    def render(self):
        # Any rendering/drawing updates would go here
        # DRAW BACKGROUND
        self.bg_scroll += self.scroll
        if self.bg_scroll >= 600:
            self.bg_scroll = 0
        self.draw_bg(self.bg_scroll)

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
