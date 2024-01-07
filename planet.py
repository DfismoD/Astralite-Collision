import pygame
import asyncio
import time

#créer une premiere classe qui va repr notre joueur
class Planet(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.max_level_xp = 100
        self.attack = 10
        self.image = pygame.image.load('Assets/Scores.png')
        self.image = pygame.transform.scale(self.image,(1920, 200))
        self.rect = self.image.get_rect()
        self.rect.x = self.game.screen_size[0]/2
        self.rect.y = self.game.screen_size[1]-100

    def damage(self):
        if self.health - self.attack >= self.attack:
           self.health -= self.attack
        else: 
            self.game.game_over()
        print(self.health)

    def heal(self, amount):
        self.health += amount
        if self.health >= 100:
            self.health = 100

    def update_planet_health_bar(self, surface):
        #déssiner la barre de vie:
        pygame.draw.rect(surface, (60,63,60), [self.game.screen_size[0]/11.1, self.game.screen_size[1]/1.3, self.max_health*4.2, 25])
        pygame.draw.rect(surface, (111,210,46), [self.game.screen_size[0]/11.1, self.game.screen_size[1]/1.3 , self.health*4.2, 25])
