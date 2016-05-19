import pygame, sys
import ScoreManager
from pygame.locals import *

import State


def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Neverpasstest Mika")
    state = 0
    menu = State.Menu(screen)
    game = None
    clock = pygame.time.Clock()

    ScoreManager.load_scores()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if state == 0:
            if menu.update():
                game = State.Game(screen)
                state = 1
        elif state == 1:
            if game.update():
                menu = State.Menu(screen)
                state = 0
        pygame.display.update()
        clock.tick(30)

main()
