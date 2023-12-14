import pygame
from projectile import Projectile
import asyncio
import time

#créer une premiere classe qui va repr notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 22
        self.base_attack = 22
        self.attack_check = 0
        self.velocity = 15
        self.y_velocity = 12
        self.all_projectiles = pygame.sprite.Group()
        self.all_leftprojectiles = pygame.sprite.Group()
        self.image = pygame.image.load('Assets/Vaisseau_Gold.png')
        self.image = pygame.transform.scale(self.image,(200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = self.game.screen_size[0]/2
        self.rect.y = self.game.screen_size[1]-100
        self.boostcoef = 1
        self.boost_percent = 0
        self.boost_percent_speed = 100

    def damage(self, amount):
        if self.health - amount >= amount:
           self.health -= amount
        else: 
            self.game.game_over()
        print(self.health)

    def heal(self, amount):
        self.health += amount
        if self.health >= 100:
            self.health = 100

    def update_health_bar(self, surface):
        #déssiner la barre de vie:
        pygame.draw.rect(surface, (60,63,60), [self.game.screen_size[0]/11.1, self.game.screen_size[1]/1.09, self.max_health*4.2, 25])
        pygame.draw.rect(surface, (111,210, 46), [self.game.screen_size[0]/11.1, self.game.screen_size[1]/1.09 , self.health*4.2, 25])


    def launch_projectile_right(self):
        #creer une nouvelle instance de la classe Projectile
        self.all_projectiles.add(Projectile(self))
        # self.start_animation()

    def move_right(self):
        # si le joueur n'est pas en collision avec une entité
        # if not self.game.check_collision(self, self.game.all_monsters):
        if self.rect.x < self.game.screen_size[0]+10:
            self.rect.x += self.velocity

    def move_left(self):
        # if not self.game.check_collision(self, self.game.all_monsters):
        if self.rect.x > 0:
            self.rect.x -= self.velocity

    def move_back(self):
        if self.rect.y < self.game.screen_size[1]+10:
            self.rect.y += self.y_velocity

    def move_forward(self):
        if self.rect.y > 0:
            self.rect.y -= self.y_velocity

    def boost(self):
        self.attack = self.attack*2
        self.attack_check = 3