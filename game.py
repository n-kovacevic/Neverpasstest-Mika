import pygame
import sys
import score_manager
from pygame.locals import *
import state


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Neverpasstest Mika")
    current_state = 0
    menu = state.Menu(screen)
    game = None
    hs = None
    clock = pygame.time.Clock()

    score_manager.load_scores()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if current_state == 0:
            if menu.update():
                game = state.Game(screen)
                current_state = 1
        elif current_state == 1:
            score = game.update()
            if score >= 0:
                if score_manager.is_highscore(score):
                    hs = state.HighScore(score, screen)
                    current_state = 2
                else:
                    menu = state.Menu(screen)
                    current_state = 0
        elif current_state == 2:
            score = hs.update()
            if score:
                score_manager.add_score(score)
                menu = state.Menu(screen)
                current_state = 0
        pygame.display.update()
        clock.tick(30)

main()
