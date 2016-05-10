import pygame
import random


class Mika(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/mika.png")
        self.rect = self.image.get_rect()
        self.rect.y = 436
        self.rect.x = 290
        self.speed = 0

    def update(self):
        key = pygame.key.get_pressed()
        if not (key[pygame.K_LEFT] or key[pygame.K_RIGHT]):
            if self.speed > 0:
                self.speed -= 6
            elif self.speed < 0:
                self.speed += 6
        if key[pygame.K_LEFT]:
            if self.rect.x > 19:
                if self.speed > -18:
                    self.speed -= 6
            else:
                self.speed = 0
        if key[pygame.K_RIGHT]:
            if self.rect.x < 640-60-19:
                if self.speed < 18:
                    self.speed += 6
            else:
                self.speed = 0
        self.rect.x += self.speed


class Projectile(pygame.sprite.Sprite):

    def __init__(self, images, rect):
        pygame.sprite.Sprite.__init__(self)
        self.current_image = images[0]
        self.image = self.current_image.subsurface(pygame.Rect(0, 0, 48, 48))
        self.rect = self.image.get_rect()
        self.rect.y = 400
        self.rect.x = rect.x

    def update(self):
        self.rect.y -= 10
