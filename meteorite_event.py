import pygame
from meteorite import Meteorite

class MeteoriteFallEvent:
    def __init__(self, game=None):
        self.percent = 0
        self.percent_speed = 50
        self.game = game

        self.all_meteorite = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100
    
    def meteor_fall(self):
        self.all_meteorite.add(Meteorite(self))
    
    def attempt_fall(self):
        if self.is_full_loaded():
            self.meteor_fall()
            self.percent = 0

    def update_bar(self, surface):

        self.add_percent()

        self.attempt_fall()

        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 10, 
            surface.get_width(),
            10
        ])

        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 10, 
            (surface.get_width() / 100) * self.percent,
            10
        ])