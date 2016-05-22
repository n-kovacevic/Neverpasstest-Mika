import pygame
import UI
import Objects
import Extras
import ScoreManager


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
        self.spawner = Extras.ObjectSpawner()

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

        self.spawner.draw(self.surface)

        if key[pygame.K_ESCAPE]:
            return True

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
        self.pressed = False

    def update(self):
        self.surface.fill((255, 255, 255))
        self.surface.blit(self.background, self.surface.get_rect())
        self.surface.blit(self.text_box, self.text_box_rect)
        self.draw()

        key = pygame.key.get_pressed()
        if key == self.released:
            self.pressed = False
            return False
        if key[pygame.K_q] and not self.pressed:
            self.name += "Q"
            self.pressed = True
        elif key[pygame.K_w] and not self.pressed:
            self.name += "W"
            self.pressed = True
        elif key[pygame.K_e] and not self.pressed:
            self.name += "E"
            self.pressed = True
        elif key[pygame.K_r] and not self.pressed:
            self.name += "R"
            self.pressed = True
        elif key[pygame.K_t] and not self.pressed:
            self.name += "T"
            self.pressed = True
        elif key[pygame.K_z] and not self.pressed:
            self.name += "Z"
            self.pressed = True
        elif key[pygame.K_u] and not self.pressed:
            self.name += "U"
            self.pressed = True
        elif key[pygame.K_i] and not self.pressed:
            self.name += "I"
            self.pressed = True
        elif key[pygame.K_o] and not self.pressed:
            self.name += "O"
            self.pressed = True
        elif key[pygame.K_p] and not self.pressed:
            self.name += "P"
            self.pressed = True
        elif key[pygame.K_a] and not self.pressed:
            self.name += "A"
            self.pressed = True
        elif key[pygame.K_s] and not self.pressed:
            self.name += "S"
            self.pressed = True
        elif key[pygame.K_d] and not self.pressed:
            self.name += "D"
            self.pressed = True
        elif key[pygame.K_f] and not self.pressed:
            self.name += "F"
            self.pressed = True
        elif key[pygame.K_g] and not self.pressed:
            self.name += "G"
            self.pressed = True
        elif key[pygame.K_h] and not self.pressed:
            self.name += "H"
            self.pressed = True
        elif key[pygame.K_j] and not self.pressed:
            self.name += "J"
            self.pressed = True
        elif key[pygame.K_k] and not self.pressed:
            self.name += "K"
            self.pressed = True
        elif key[pygame.K_l] and not self.pressed:
            self.name += "L"
            self.pressed = True
        elif key[pygame.K_y] and not self.pressed:
            self.name += "Y"
            self.pressed = True
        elif key[pygame.K_x] and not self.pressed:
            self.name += "X"
            self.pressed = True
        elif key[pygame.K_c] and not self.pressed:
            self.name += "C"
            self.pressed = True
        elif key[pygame.K_v] and not self.pressed:
            self.name += "V"
            self.pressed = True
        elif key[pygame.K_b] and not self.pressed:
            self.pressed = True
            self.name += "B"
        elif key[pygame.K_n] and not self.pressed:
            self.name += "N"
            self.pressed = True
        elif key[pygame.K_m] and not self.pressed:
            self.name += "M"
            self.pressed = True
        elif key[pygame.K_BACKSPACE] and not self.pressed:
            self.name = self.name[0:len(self.name)-1]
            pygame.time.wait(40)

        if key[pygame.K_RETURN]:
            return ScoreManager.Score(self.name, self.score)

        return False

    def draw(self):
        self.score_display = self.font.render(self.name, 1, self.font_color)
        if self.score_display.get_rect().width > 315:
            self.name = self.name[:len(self.name) - 1]
            self.score_display = self.font.render(self.name, 1, self.font_color)
        self.surface.blit(self.score_display, self.score_rect)
