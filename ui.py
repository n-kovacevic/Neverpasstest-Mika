import pygame
import extras


class PlayButton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.normal_image = pygame.image.load("res/button_play_normal.png")
        self.hover_image = pygame.image.load("res/button_play_hover.png")

        self.image = self.normal_image
        self.rect = self.image.get_rect()

        self.rect.x = 207
        self.rect.y = 280

    def update(self):
        if extras.point_col(pygame.mouse.get_pos(), self.rect):
            self.image = self.hover_image
            if pygame.mouse.get_pressed() == (1, 0, 0):
                return 1
        else:
            self.image = self.normal_image
        return 0


class ScoreButton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.normal_image = pygame.image.load("res/button_hs_normal.png")
        self.hover_image = pygame.image.load("res/button_hs_hover.png")

        self.image = self.normal_image
        self.rect = self.image.get_rect()

        self.rect.x = 207
        self.rect.y = 340

    def update(self):
        if extras.point_col(pygame.mouse.get_pos(), self.rect):
            self.image = self.hover_image
            if pygame.mouse.get_pressed() == (1, 0, 0):
                return 2
        else:
            self.image = self.normal_image
        return 0

class ReturnButton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.normal_image = pygame.image.load("res/button_ret_normal.png")
        self.hover_image = pygame.image.load("res/button_ret_hover.png")

        self.image = self.normal_image
        self.rect = self.image.get_rect()

        self.rect.x = 207
        self.rect.y = 400

    def update(self):
        if extras.point_col(pygame.mouse.get_pos(), self.rect):
            self.image = self.hover_image
            if pygame.mouse.get_pressed() == (1, 0, 0):
                return True
        else:
            self.image = self.normal_image
        return False

class SubmitButton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.normal_image = pygame.image.load("res/button_submit_normal.png")
        self.hover_image = pygame.image.load("res/button_submit_hover.png")

        self.image = self.normal_image
        self.rect = self.image.get_rect()

        self.rect.x = 207
        self.rect.y = 280

    def update(self):
        if extras.point_col(pygame.mouse.get_pos(), self.rect):
            self.image = self.hover_image
            if pygame.mouse.get_pressed() == (1, 0, 0):
                return 1
        else:
            self.image = self.normal_image
        return 0
