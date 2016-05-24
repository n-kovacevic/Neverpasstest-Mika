import pygame
import ui
import objects
import extras
import score_manager


class Menu:
    sprites = []

    def __init__(self, surface):
        self.surface = surface
        self.background = pygame.image.load("res/background.png")

        button_play = ui.PlayButton()
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
        self.player = pygame.sprite.GroupSingle(objects.Mika())
        self.projectiles = pygame.sprite.Group()
        self.timer = 30
        self.pimages = []
        self.pimages.append(pygame.image.load("res/projectile_1.png"))
        self.spawner = extras.ObjectSpawner()

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
                self.projectiles.add(objects.Projectile(self.pimages, self.player.sprite.rect))
                self.timer = 0

        self.spawner.draw(self.surface)

        if key[pygame.K_ESCAPE]:
            return self.spawner.score

        return self.spawner.update(self.projectiles)


class HighScore:
    def __init__(self, score, surface):
        self.score = score
        self.surface = surface
        self.background = pygame.image.load("res/background.png")
        self.text_box = pygame.image.load("res/text_box.png")
        self.text_box_rect = self.text_box.get_rect()
        self.text_box_rect.left = 160
        self.text_box_rect.top = 180
        self.name = str("")
        self.font = pygame.font.SysFont("Impact", 32)
        self.font_color = (200, 200, 200)
        self.score_display = self.font.render(str(self.score), 1, self.font_color)
        self.score_rect = self.score_display.get_rect()
        self.score_rect.left = 168
        self.score_rect.top = 183
        self.released = tuple([0 for i in range(323)])
        self.pressed = [False for i in range(323)]

    def update(self):
        self.surface.fill((255, 255, 255))
        self.surface.blit(self.background, self.surface.get_rect())
        self.surface.blit(self.text_box, self.text_box_rect)
        self.draw()

        key = pygame.key.get_pressed()
        if key == self.released:
            self.pressed  = [False for i in range(323)]
            return False
        if key[pygame.K_q] and not self.pressed[pygame.K_q]:
            self.name += "Q"
            self.pressed[pygame.K_q] = True
        elif key[pygame.K_w] and not self.pressed[pygame.K_w]:
            self.name += "W"
            self.pressed[pygame.K_w] = True
        elif key[pygame.K_e] and not self.pressed[pygame.K_e]:
            self.name += "E"
            self.pressed[pygame.K_e] = True
        elif key[pygame.K_r] and not self.pressed[pygame.K_r]:
            self.name += "R"
            self.pressed[pygame.K_r] = True
        elif key[pygame.K_t] and not self.pressed[pygame.K_t]:
            self.name += "T"
            self.pressed[pygame.K_t] = True
        elif key[pygame.K_z] and not self.pressed[pygame.K_z]:
            self.name += "Z"
            self.pressed[pygame.K_z] = True
        elif key[pygame.K_u] and not self.pressed[pygame.K_u]:
            self.name += "U"
            self.pressed[pygame.K_u] = True
        elif key[pygame.K_i] and not self.pressed[pygame.K_i]:
            self.name += "I"
            self.pressed[pygame.K_i] = True
        elif key[pygame.K_o] and not self.pressed[pygame.K_o]:
            self.name += "O"
            self.pressed[pygame.K_o] = True
        elif key[pygame.K_p] and not self.pressed[pygame.K_p]:
            self.name += "P"
            self.pressed[pygame.K_p] = True
        elif key[pygame.K_a] and not self.pressed[pygame.K_a]:
            self.name += "A"
            self.pressed[pygame.K_a] = True
        elif key[pygame.K_s] and not self.pressed[pygame.K_s]:
            self.name += "S"
            self.pressed[pygame.K_s] = True
        elif key[pygame.K_d] and not self.pressed[pygame.K_d]:
            self.name += "D"
            self.pressed[pygame.K_d] = True
        elif key[pygame.K_f] and not self.pressed[pygame.K_f]:
            self.name += "F"
            self.pressed[pygame.K_f] = True
        elif key[pygame.K_g] and not self.pressed[pygame.K_g]:
            self.name += "G"
            self.pressed[pygame.K_g] = True
        elif key[pygame.K_h] and not self.pressed[pygame.K_h]:
            self.name += "H"
            self.pressed[pygame.K_h] = True
        elif key[pygame.K_j] and not self.pressed[pygame.K_j]:
            self.name += "J"
            self.pressed[pygame.K_j] = True
        elif key[pygame.K_k] and not self.pressed[pygame.K_k]:
            self.name += "K"
            self.pressed[pygame.K_k] = True
        elif key[pygame.K_l] and not self.pressed[pygame.K_l]:
            self.name += "L"
            self.pressed[pygame.K_l] = True
        elif key[pygame.K_y] and not self.pressed[pygame.K_y]:
            self.name += "Y"
            self.pressed[pygame.K_y] = True
        elif key[pygame.K_x] and not self.pressed[pygame.K_x]:
            self.name += "X"
            self.pressed[pygame.K_x] = True
        elif key[pygame.K_c] and not self.pressed[pygame.K_c]:
            self.name += "C"
            self.pressed[pygame.K_c] = True
        elif key[pygame.K_v] and not self.pressed[pygame.K_v]:
            self.name += "V"
            self.pressed[pygame.K_v] = True
        elif key[pygame.K_b] and not self.pressed[pygame.K_b]:
            self.name += "B"
            self.pressed[pygame.K_b] = True
        elif key[pygame.K_n] and not self.pressed[pygame.K_n]:
            self.name += "N"
            self.pressed[pygame.K_n] = True
        elif key[pygame.K_m] and not self.pressed[pygame.K_m]:
            self.name += "M"
            self.pressed[pygame.K_m] = True
        elif key[pygame.K_SPACE] and not self.pressed[pygame.K_SPACE]:
            self.name += " "
            self.pressed[pygame.K_SPACE] = True
        elif key[pygame.K_BACKSPACE]:
            self.name = self.name[0:len(self.name)-1]
            pygame.time.wait(80)
        if key[pygame.K_RETURN]:
            return score_manager.Score(self.name, self.score)

        return False

    def draw(self):
        self.score_display = self.font.render(self.name, 1, self.font_color)
        if self.score_display.get_rect().width > 315:
            self.name = self.name[:len(self.name) - 1]
            self.score_display = self.font.render(self.name, 1, self.font_color)
        self.surface.blit(self.score_display, self.score_rect)