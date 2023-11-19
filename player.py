import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.max_health = 3
        self.attack = 1
        self.velocity = 25
        self.all_lasers = pygame.sprite.Group()
        self.img = pygame.image.load("assets/ship.png")
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.rect = self.img.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_laser(self):
        laser = Laser(self)
        self.all_lasers.add(Laser(self))

    def damage(self, amount):
        self.health -= amount
        print(self.health)
        if self.health <= 0:
            print('You have died!')


    def handle_input(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_q] and self.rect.x > 0:
            self.rect.x -= self.velocity
        if keys_pressed[pygame.K_d] and self.rect.x + self.rect.width < 1920:
            self.rect.x += self.velocity
        if keys_pressed[pygame.K_z] and self.rect.y > 0:
            self.rect.y -= self.velocity
        if keys_pressed[pygame.K_s] and self.rect.y + self.rect.height < 1080:
            self.rect.y += self.velocity
        if keys_pressed[pygame.K_SPACE]:
            self.launch_laser()