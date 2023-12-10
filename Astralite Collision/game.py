import pygame
from player import Player
from comet import Comet
from comet_event import CometFallEvent
from pointbuff import Pointbuff
from monster import Monster

# creer une 2e classe qui va repr le jeu
class Game:

    def __init__(self, screen , screen_size):
        self.screen = screen
        self.screen_size = screen_size
        self.is_playing = False
        #générer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #genérer le manager 
        self.comet_event = CometFallEvent(self)
        #grp de monstres
        self.all_comets = pygame.sprite.Group()

        self.pointbuff = Pointbuff(self)
        self.all_pointbuffs = pygame.sprite.Group()
        #METTRE LE SCORE A 0
        self.score = 0
        self.pressed = {}

        self.monster = Monster(self)
        self.all_monsters = pygame.sprite.Group()

        self.hp_pos_x = 700
        self.hp_pos_y = 40
        


    def start(self):
        # if self.is_playing == False:
            # self.spawn_monster()
            # self.spawn_monster()
        self.is_playing = True

    def def_hp_pos_x(self, amount):
        self.monster.pos_x = amount

    def add_meteor1_score(self, points=100):
        self.score += points*self.player.boostcoef


    def game_over(self):
        #remettre le jeu à neuf, retirer les monstres, remettre le joueur à 100hp et jeu en attente
        self.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0

    def update(self, screen):
        #afficher le score sur l'écran
        font = pygame.font.SysFont("monospace", 24)
        score_text = font.render(f"Score : {self.score}", 1, (255, 255, 255))
        # screen_size = screen.get_size()
        
        
        

        
        #appliquer l'img de mon joueur
        screen.blit(self.player.image, self.player.rect)

        #actu la barre de vie du joueur
        self.player.update_health_bar(screen)
        hp_bar = pygame.image.load('Assets/HP_bar.png')
        hp_bar = pygame.transform.scale(hp_bar,(500, 70))
        screen.blit(hp_bar, (self.screen_size[0]/20, self.screen_size[1]/1.12))
        screen.blit(score_text, (self.screen_size[0]/2.15, 50))

        #actu la barre d'event du jeu
        self.comet_event.update_bar(screen)

        self.comet_event.comet.update_health_bar(screen)
        
        
    
        # self.player.update_animation()

                #récup les comètes
        for comet in self.comet_event.all_comets:
            comet.fall()
            comet.update_health_bar(screen)

        for pointbuff in self.all_pointbuffs:
            pointbuff.forward()

        #récup les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move_right()


        #récup les monstres
        for monster in self.all_monsters:
            monster.forward()
            # monster.update_health_bar(screen)


            
            

        #aplliquer les projectiles
        self.player.all_projectiles.draw(screen)
        # self.player.all_leftprojectiles.draw(screen)

        # appliquer l'ennsemble des images de mon grp de monstre
        self.all_monsters.draw(screen)

        self.all_pointbuffs.draw(screen)

        # appliquer l'ennsemble des images de mon grp de comètes
        self.comet_event.all_comets.draw(screen)

        

        #verif si le joueur souhaite aller à gauche ou a droite
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self):
        self.monster.pos_x = self.hp_pos_x
        self.monster.pos_y = self.hp_pos_y
        monster = Monster(self)
        self.all_monsters.add(monster)

    def spawn_pointbuff(self):
        self.pointbuff.pos_x = self.hp_pos_x
        self.pointbuff.pos_y = self.hp_pos_y
        pointbuff = Pointbuff(self)
        self.all_pointbuffs.add(pointbuff)
        

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite,group, False, pygame.sprite.collide_mask)
