import pygame
import random
import time


#créer une classe qui va gérer la nottion de monstre sur notre jeu
class Pointbuff(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.image = pygame.image.load('Assets/X2.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.pos_x = 1300
        self.pos_y = 40
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.velocity = random.randint(8,10)

    # def damage(self, amount):
    #      #infliger les dégats
    #     self.health -= amount

    #     #vérifier si son nouveau nombre de pv est <= 0
    #     if self.health <= 0:
    #         # Reapparaitre comme un nv monstre
    #         self.rect.x = random.randint(0,1800)
    #         self.rect.y = -100
    #         self.health = self.max_health

    # def update_health_bar(self, surface):
    #      #déssiner la barre de vie:
    #     pygame.draw.rect(surface, (60,63,60), [self.rect.x + 10, self.rect.y - 15, self.max_health, 5])
    #     pygame.draw.rect(surface, (111,210, 46), [self.rect.x + 10, self.rect.y - 15, self.health, 5])

    def remove(self):
        self.game.all_pointbuffs.remove(self)

    def forward(self):
        #le déplacement ne se fait que si il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
        elif self.rect.y >= self.game.screen_size[1]+100:
            self.remove()
        else:
            # self.game.player.boost(2)
            self.remove()

    # def fall(self):
    #     self.rect.y += self.velocity
    #     if self.rect.y >= 500:
    #         print("sol")