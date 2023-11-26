import pygame
from laser import Laser
from meteorite_event import MeteoriteFallEvent

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.meteorite_event = MeteoriteFallEvent()
        self.health = 100
        self.max_health = self.health
        self.attack = 1
        self.velocity = 25
        self.all_lasers = pygame.sprite.Group()
        self.img = pygame.image.load("assets/ship.png")
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.rect = self.img.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def update_health_bar(self,surface, position):
        bar_color = (71, 209, 71)
        back_bar_color = (230, 0, 0)
        bar_position = [position[0] + 63, position[1] + 27, self.health * 4, 30]
        back_bar_position = [position[0] + 63, position[1] + 27, self.health * 4, 30]

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_laser(self):
        laser = Laser(self)
        self.all_lasers.add(laser)

    def damage(self, amount):
        self.health -= amount
        print(self.health)
        if self.health <= 0:
            print('You have died!')

    def chek_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False)


    def handle_input(self):
        keys_pressed = pygame.key.get_pressed()

        if self.chek_collision(self, self.meteorite_event.all_meteorite):
            print("joueur toucher")
            self.damage(10)

        if keys_pressed[pygame.K_q] and self.rect.x > 0:
            self.rect.x -= self.velocity
        if keys_pressed[pygame.K_d] and self.rect.x + self.rect.width < 1920:
            self.rect.x += self.velocity
        if keys_pressed[pygame.K_z] and self.rect.y > 0:
            self.rect.y -= self.velocity
        if keys_pressed[pygame.K_s] and self.rect.y + self.rect.height < 1080:
            self.rect.y += self.velocity
        
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if keys_pressed[pygame.K_SPACE]:
                    self.launch_laser()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    self.launch_laser()