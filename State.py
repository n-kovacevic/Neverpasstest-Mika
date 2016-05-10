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
        self.surface = surface
        self.background = pygame.image.load("res/background.png")
        self.player = pygame.sprite.GroupSingle(Objects.Mika())
        self.projectiles = pygame.sprite.Group()
        self.timer = 30
        self.pimages = []
        self.pimages.append(pygame.image.load("res/projectile_1.png"))

    def update(self):
        self.timer += 1
        self.surface.fill((255, 255, 255))
        self.surface.blit(self.background, self.surface.get_rect())

        self.player.update()
        self.player.draw(self.surface)

        self.projectiles.update()
        self.projectiles.draw(self.surface)

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            if self.timer >= 12:
                self.projectiles.add(Objects.Projectile(self.pimages, self.player.sprite.rect))
                self.timer = 0

        if key[pygame.K_ESCAPE]:
            return True
        return False
