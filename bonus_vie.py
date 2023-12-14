import pygame
import random


#créer une classe qui va gérer la nottion de monstre sur notre jeu
class Bonus_vie(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.image = pygame.image.load('Assets/HP.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.pos_x = 700
        self.pos_y = 40
        self.rect = self.image.get_rect()
        self.rect.x = self.game.comet_event.position_x_avant_suppression
        self.rect.y = self.game.comet_event.position_y_avant_suppression
        self.velocity = random.randint(8,10)

    def remove(self):
        self.game.all_bonus_vie.remove(self)

    def forward(self):
        #le déplacement ne se fait que si il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
        elif self.rect.y >= self.game.screen_size[1]+100:
            self.remove()
        else:
            self.game.player.heal(self.attack)
            self.remove()