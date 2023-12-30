import pygame, random
from comet import Comet
from cometbis import Cometbis
from cometbis3 import Cometbis3

#créer la classe de l'event
class CometFallEvent:

    def __init__(self, game):
        self.position_x_avant_suppression = 0
        self.position_y_avant_suppression = 0
        self.percent = 0
        self.percent_speed = 100
        self.game = game

        #définir le grp de sprite pour stocker nos comètes
        self.comet = Comet(self)
        self.comet_2 =  Cometbis(self)
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        if self.game.score >= 500:
            if self.game.score >= 1500:
                self.number = random.randint(0, 6)
                if self.number <= 2:
                    self.all_comets.add(Cometbis(self))
                elif self.number <= 4:
                    self.all_comets.add(Cometbis3(self))
                else :
                    self.all_comets.add(Comet(self))
            else:
                self.number = random.randint(0, 5)
                if self.number <= 2:
                    self.all_comets.add(Cometbis(self))
                else:
                    self.all_comets.add(Comet(self))
        else:
            self.all_comets.add(Comet(self))
    
    def attempt_fall(self):
        if self.is_full_loaded():
            self.meteor_fall()
            self.reset_percent()


    def update_bar(self, surface):

        self.attempt_fall()

        self.add_percent()      