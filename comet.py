import pygame, random
from pointbuff import Pointbuff

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.image = pygame.image.load("Assets/Meteorite_1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 5)
        self.comet_event = comet_event
        self.pointbuff = Pointbuff(self)
        self.all_pointbuffs = pygame.sprite.Group()
        self.rect.x = random.randint(100, self.comet_event.game.screen_size[0]-100)
        self.rect.y = -random.randint(100, self.comet_event.game.screen_size[1]/3)
        
    def damage(self, amount):
        #infliger les dégats
        self.health -= amount
        self.comet_event.game.sound_manager.play('click')

        if self.health <= 0:
            self.remove()
            self.comet_event.game.add_meteor1_score()
            self.comet_event.game.add_meteor1_xp()
            if random.randint(1,8) == 5:
                self.comet_event.game.spawn_monster()
            elif random.randint(1,8) == 6:
                self.comet_event.game.spawn_pointbuff()

    def update_health_bar(self, surface):
        #déssiner la barre de vie:
        pygame.draw.rect(surface, (60,63,60), [self.rect.x - 10, self.rect.y - 15, self.max_health, 5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x - 10, self.rect.y - 15, self.health, 5])       

    def remove(self):
        self.comet_event.position_x_avant_suppression = self.rect.x
        self.comet_event.position_y_avant_suppression = self.rect.y
        self.comet_event.all_comets.remove(self)

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 1000:
            self.comet_event.game.planet.damage()
            self.remove()

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.remove()
            self.comet_event.game.player.damage(20)