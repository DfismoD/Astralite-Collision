import pygame
import numpy
import math
from player import Player
from comet import Comet
from comet_event import CometFallEvent
from pointbuff import Pointbuff
from bonus_vie import Bonus_vie
from sounds import SoundManager

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

        self.sound_manager = SoundManager()

        self.pointbuff = Pointbuff(self)
        self.all_pointbuffs = pygame.sprite.Group()
        #METTRE LE SCORE A 0
        self.score = 0
        self.pressed = {}

        self.bonus_vie = Bonus_vie(self)
        self.all_bonus_vie = pygame.sprite.Group()

        self.hp_pos_x = 700
        self.hp_pos_y = 40

    def start(self):
        self.is_playing = True

    def add_meteor1_score(self, points=100):
        self.score += points*self.player.boostcoef
        if self.score >= 1000:
            self.comet_event.percent_speed = 200

    def add_meteor2_score(self, points=250):
        self.score += points*self.player.boostcoef
        if self.score >= 1000:
            self.comet_event.percent_speed = 200

    def add_meteor1_xp(self, points=5):
        self.player.xp += points
        if self.player.xp >= self.player.max_level_xp:
            self.player.xp = 0
            self.player.level += 1

    def add_meteor2_xp(self, points=10):
        self.player.xp += points
        if self.player.xp >= self.player.max_level_xp:
            self.player.xp = 0
            self.player.level += 1

    def game_over(self):
        save_read = open("save.txt", "r")
        last_score = int(save_read.read())

        if last_score < self.score:
            save_score = self.score
            save_write = open("save.txt", "w")
            save_repr = repr(save_score)
            save_write.write(save_repr)
            save_write.close()

        #remettre le jeu à neuf, retirer les monstres, remettre le joueur à 100hp et jeu en attente
        self.all_comets = pygame.sprite.Group()
        for comet in self.comet_event.all_comets:
            comet.remove()
        self.player.health = self.player.max_health
        self.player.rect.x = self.screen_size[0]/2
        self.player.rect.y = self.screen_size[1]-200 
        self.is_playing = False
        self.score = 0
        self.player.level = 0

    def update(self, screen):
        #AFFICHER LE BOUTON QUITTER 
        playing_quit_button = pygame.image.load('assets/Quitter.png')
        playing_quit_button = pygame.transform.scale(playing_quit_button,(self.screen_size[0]/4, self.screen_size[1]/2.5))
        playing_quit_button_rect = playing_quit_button.get_rect()
        playing_quit_button_rect.x = math.ceil(self.screen_size[0] / 2.65)
        playing_quit_button_rect.y = 120

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

        self.player.update_xp_bar(screen)
        xp_bar = pygame.image.load('Assets/EXP_bar.png')
        xp_bar = pygame.transform.scale(xp_bar,(500, 70))
        screen.blit(xp_bar, (self.screen_size[0]/20, self.screen_size[1]/1.232))
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
        for bonus_vie in self.all_bonus_vie:
            bonus_vie.forward()
            # monster.update_health_bar(screen)

        #aplliquer les projectiles
        self.player.all_projectiles.draw(screen)
        # self.player.all_leftprojectiles.draw(screen)

        # appliquer l'ennsemble des images de mon grp de monstre
        self.all_bonus_vie.draw(screen)

        self.all_pointbuffs.draw(screen)

        # appliquer l'ennsemble des images de mon grp de comètes
        self.comet_event.all_comets.draw(screen)

        #verif si le joueur souhaite aller à gauche ou a droite
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()
        if self.pressed.get(pygame.K_ESCAPE):
            self.game_over()


    def spawn_monster(self):
        self.bonus_vie.pos_x = self.hp_pos_x
        self.bonus_vie.pos_y = self.hp_pos_y
        bonus_vie = Bonus_vie(self)
        self.all_bonus_vie.add(bonus_vie)

    def spawn_pointbuff(self):
        self.pointbuff.pos_x = self.hp_pos_x
        self.pointbuff.pos_y = self.hp_pos_y
        pointbuff = Pointbuff(self)
        self.all_pointbuffs.add(pointbuff)
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite,group, False, pygame.sprite.collide_mask)
