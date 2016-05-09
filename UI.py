import pygame
import Extras


class PlayButton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.normal_image = pygame.image.load("res/button_play_normal.png")
        self.hover_image = pygame.image.load("res/button_play_hover.png")

        self.image = self.normal_image
        self.rect = self.image.get_rect()

        self.rect.x = 200
        self.rect.y = 280

    def update(self):
        if Extras.point_col(pygame.mouse.get_pos(), self.rect):
            self.image = self.hover_image
            if pygame.mouse.get_pressed() == (1, 0, 0):
                return True
        else:
            self.image = self.normal_image
        return False

