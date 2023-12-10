import pygame


#def la classe qui va gérer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):


    #def le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 20
        self.player = player
        self.image = pygame.image.load('Assets/Laser_1.png')
        self.image = pygame.transform.scale(self.image, (20,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 86
        self.rect.y = player.rect.y - 40
        self.origin_image = self.image
        self.angle = 0

    # def rotate(self):
    #     #tourner le projectile
    #     self.angle += 20
    #     self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
    #     self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move_right(self):
        self.rect.y -= self.velocity

        if self.rect.y < 0:
            #supprimer le porjectile
            self.remove()

        # for comet in self.player.game.check_collision(self, self.player.game.all_comets):
        #      self.remove()
        #      comet.damage(self.player.attack)

        for comet in self.player.game.check_collision(self, self.player.game.comet_event.all_comets):
            comet.damage(self.player.attack)
            # self.player.game.comet_event.comet.damage(self.player.attack)
            # print(str(self.player.game.comet_event.comet.health))
            self.remove()

        for pointbuff in self.player.game.check_collision(self, self.player.game.comet_event.comet.all_pointbuffs):
            self.remove()
            print('d')

        #Vérif si le proj entre en collision avec un monstre
        # if self.player.game.check_collision(self, self.player.game.all_comets):
        #     #supr le proj
        #     self.remove()
        #     #infliger des degats
        #     self.game.comet_event.comet.comet.damage(self.player.attack)

    # def move_left(self):
    #     self.rect.x -= self.velocity
    #     # self.rotate()


        #vérif si le projectile n'est plus sur l'écran
