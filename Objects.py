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
        self.current_image = random.choice(images)
        self.image = self.current_image.subsurface(pygame.Rect(0, 0, 48, 48))
        self.rect = pygame.Rect(6, 6, 36, 36)
        self.rect.y += 400
        self.rect.x += rect.x
        self.cur_x = 0

    def update(self):
        self.rect.y -= 10
        if self.cur_x+48 < self.current_image.get_rect().w:
            self.cur_x += 48
        else:
            self.cur_x = 0
        self.image = self.current_image.subsurface(pygame.Rect(self.cur_x, 0, 48, 48))


class BadEssay(pygame.sprite.Sprite):
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/bad_essay.png")
        self.rect = rect

    def update(self):
        self.rect.y += 4
        if self.rect.y >= 430:
            return True
