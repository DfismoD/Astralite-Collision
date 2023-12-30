import pygame


#def la classe qui va gérer le projectile de notre joueur
class Projectile5(pygame.sprite.Sprite):


    #def le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 35
        self.player = player
        self.image = pygame.image.load('Assets/Laser_5.png')
        self.image = pygame.transform.scale(self.image, (20,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 86
        self.rect.y = player.rect.y - 40
        self.origin_image = self.image
        self.angle = 0

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move_right(self):
        self.rect.y -= self.velocity

        if self.rect.y < 0:
            #supprimer le porjectile
            self.remove()

        for comet in self.player.game.check_collision(self, self.player.game.comet_event.all_comets):
            comet.damage(self.player.attack)
            if self.player.attack_check > 0:
                self.player.attack_check -= 1
            if self.player.attack_check == 0:
                self.player.attack = self.player.base_attack
            # self.player.game.comet_event.comet.damage(self.player.attack)
            # print(str(self.player.game.comet_event.comet.health))
            self.remove()

        for pointbuff in self.player.game.check_collision(self, self.player.game.comet_event.comet.all_pointbuffs):
            self.remove()