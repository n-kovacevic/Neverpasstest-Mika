import random
import pygame
import Objects


def point_col(position, rect):
    x, y = position
    if x < rect.x:
        return False
    if x > rect.x + rect.w:
        return False
    if y < rect.y:
        return False
    if y > rect.y + rect.h:
        return False
    return True


class ObjectSpawner():
    def __init__(self):
        self.spawn_timer = 0
        self.spawn_distance = random.randrange(580)
        self.spawn_location = 0
        self.max_timer = 180
        self.min_timer = 90
        self.bad_group = pygame.sprite.Group()

    def update(self, projectiles):
        for essay in self.bad_group.sprites():
            if essay.update():
                return True
        pygame.sprite.groupcollide(projectiles, self.bad_group, True, True)
        self.spawn_timer -= 1
        if self.spawn_timer <= 0:
            self.spawn_essay()
        return False

    def draw(self, surface):
        self.bad_group.draw(surface)

    def spawn_essay(self):
        rect = pygame.Rect(self.spawn_distance, -60, 60, 60)
        sprite = Objects.BadEssay(rect)
        self.bad_group.add(sprite)
        if self.max_timer > 20:
            self.max_timer -= 5
        if self.min_timer > 15:
            self.min_timer -= 5
        self.spawn_timer = random.randrange(self.min_timer, self.max_timer)
        self.spawn_location = self.spawn_distance
        self.spawn_distance = random.randrange(580)
