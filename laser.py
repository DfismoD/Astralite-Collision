import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("assets/laser_astralite.png")
        self.image = pygame.transform.scale(self.image, (10, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 42
        self.rect.y = player.rect.y - 50

    def move(self):
        self.rect.y -= self.velocity

        if self.rect.y < -50:
            self.player.all_lasers.remove(self)