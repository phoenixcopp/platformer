import pygame
from settings import *
from level import Level

pygame.init()

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("platformer game")
clock = pygame.time.Clock()
level = Level(level_map, win)
run = True

while run:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    level.run()
    pygame.display.update()

pygame.quit()