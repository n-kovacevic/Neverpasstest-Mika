import pygame
import UI
import Objects


class Menu:
    sprites = []

    def __init__(self, surface):
        self.surface = surface
        self.background = pygame.image.load("res/background.png")

        button_play = UI.PlayButton()
        self.sprites.append(button_play)

    def update(self):
        self.surface.fill((255, 255, 255))
        self.surface.blit(self.background, self.surface.get_rect())
        for sprite in self.sprites:
            if sprite.update():
                return True
            self.surface.blit(sprite.image,sprite.rect)
        return False


class Game:
    def __init__(self, surface):
        self.objects = []
        self.surface = surface
        self.background = pygame.image.load("res/background.png")
        self.objects.append(Objects.Mika())

    def update(self):
        self.surface.fill((255, 255, 255))
        self.surface.blit(self.background, self.surface.get_rect())
        for obj in self.objects:
            if obj.update():
                return True
            self.surface.blit(obj.image, obj.rect)
