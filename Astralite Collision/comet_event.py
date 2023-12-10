import pygame
from comet import Comet

#créer la classe de l'event
class CometFallEvent:

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 100
        self.game = game

        #définir le grp de sprite pour stocker nos comètes
        self.comet = Comet(self)
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        self.all_comets.add(Comet(self))
    
    def attempt_fall(self):
        if self.is_full_loaded():
            self.meteor_fall()
            self.reset_percent()


    def update_bar(self, surface):

        self.add_percent()

        self.attempt_fall()

        # pygame.draw.rect(surface, (0,0,0),[
        #     0, #x
        #     surface.get_height()-20, #y
        #     surface.get_width(),
        #     10
        # ])

        # pygame.draw.rect(surface, (187,11,11),[
        #     0, #x
        #     surface.get_height()-20, #y
        #     (surface.get_width() / 100)*self.percent,
        #     10
        # ])
