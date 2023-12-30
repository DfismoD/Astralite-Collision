import pygame
from projectile import Projectile
from projectilebis import Projectile2
from projectilebis3 import Projectile3
from projectilebis4 import Projectile4
from projectilebis5 import Projectile5
import asyncio
import time

#créer une premiere classe qui va repr notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.level = 0
        self.xp = 0
        self.max_level_xp = 100
        self.attack = 22
        self.base_attack = 22
        self.attack_check = 0
        self.velocity = 15
        self.y_velocity = 12
        self.all_projectiles = pygame.sprite.Group()
        self.all_projectiles2 = pygame.sprite.Group()
        self.image = pygame.image.load('Assets/Vaisseau_Gold.png')
        self.image = pygame.transform.scale(self.image,(200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = self.game.screen_size[0]/2
        self.rect.y = self.game.screen_size[1]-200
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
        pygame.draw.rect(surface, (111,210,46), [self.game.screen_size[0]/11.1, self.game.screen_size[1]/1.09 , self.health*4.2, 25])

    def update_xp_bar(self, surface):
        #déssiner la barre de vie:
        pygame.draw.rect(surface, (60,63, 60), [self.game.screen_size[0]/11.1, self.game.screen_size[1]/1.2 , self.max_level_xp*4.2, 25])
        pygame.draw.rect(surface, (176,224,230), [self.game.screen_size[0]/11.1, self.game.screen_size[1]/1.2, self.xp*4.2, 25])
        

    def launch_projectile_right(self):
        #creer une nouvelle instance de la classe Projectile
        
        if self.level == 0 :
            self.all_projectiles.add(Projectile(self))
            self.game.sound_manager.play('tir')
        elif self.level == 1:
            self.attack = 40
            self.all_projectiles.add(Projectile2(self))     
            self.game.sound_manager.play('tir2')  
        elif self.level == 2:
            self.attack = 55
            self.all_projectiles.add(Projectile3(self))     
            self.game.sound_manager.play('tir3') 
        elif self.level == 3:
            self.attack = 75
            self.all_projectiles.add(Projectile4(self))     
            self.game.sound_manager.play('tir4')  
        else :
            self.attack = 100
            self.all_projectiles.add(Projectile5(self))     
            self.game.sound_manager.play('tir5')  



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

    def levelup(self):
        self.xp = 0
        self.level += 1
        self.game.sound_manager.play('levelup')