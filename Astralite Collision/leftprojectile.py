import pygame

#def la classe qui va gérer le projectile de notre joueur
class LeftProjectile(pygame.sprite.Sprite):


    #def le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 10
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 20
        self.rect.y = player.rect.y + 70
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectile
        self.angle -= 20
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_leftprojectiles.remove(self)

    def move_left(self):
        self.rect.x -= self.velocity
        self.rotate()
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            #supr le proj
            self.remove()

    

        #vérif si le projectile n'est plus sur l'écran
        if self.rect.x < 0:
            #supprimer le porjectile
            self.remove()