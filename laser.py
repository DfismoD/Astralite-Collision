import pygame
from meteorite_event import MeteoriteFallEvent

class Laser(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        
        self.velocity = 25
        self.player = player
        self.image = pygame.image.load("assets/laser_astralite.png")
        self.image = pygame.transform.scale(self.image, (10, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + 42
        self.rect.y = self.player.rect.y - 50
        self.meteorite = MeteoriteFallEvent()

    def move(self):
        self.rect.y -= self.velocity

        # if self.meteorite_event.game.chek_collision(self.meteorite_event.game.player, self.meteorite_event.all_meteorite):
        #     print("sa marche")

        if self.rect.y < -50:
            self.player.all_lasers.remove(self)