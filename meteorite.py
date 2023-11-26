import pygame, random

class Meteorite(pygame.sprite.Sprite):
    def __init__(self, meteorite_event):
        super().__init__()
        self.image = pygame.image.load("assets/meteorite_astralite_1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 1920)
        self.meteorite_event = meteorite_event
    
    def remove(self):
        self.meteorite_event.all_meteorite.remove(self)

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 1000:
            self.remove()

        # if self.meteorite_event.game.chek_collision(self.meteorite_event.game.player, self.meteorite_event.all_meteorite):
        #     print("joueur toucher")
        #     self.remove()
        #     self.meteorite_event.game.player.damage(1)