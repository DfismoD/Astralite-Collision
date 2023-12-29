import pygame
import math
from game import Game
pygame.init()

clock = pygame.time.Clock()
FPS = 120


#générer fenetre du jeu
pygame.display.set_caption("Astralite Tycoon") #titre du jeu
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #taille de la fenêtre
screen_size = screen.get_size() #récupère la taille de l'image

background = pygame.image.load('Assets/Fond_espace.png') #importer le bg 
background = pygame.transform.scale(background, screen_size) #modifier taille de l'image

#importer charger notre bannière
banner = pygame.image.load('Assets/Logo2.png')
banner = pygame.transform.scale(banner,(screen_size[0]/3, screen_size[1]/3.5))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen_size[0]/3) #le [0] désigne la taille x et [1] la taille en y
banner_rect.y = 30

#import charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/Jouer.png')
play_button = pygame.transform.scale(play_button,(screen_size[0]/4, screen_size[1]/2.5))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen_size[0] / 2.65)
play_button_rect.y = 120

#charger notre jeu 
game = Game(screen, screen_size)

running = True

#boucle tant que cette condition est vraie
while running:

    #appliquer le bg au jeu
    screen.blit(background, (0,0))

    #vérifier si notre jeu à commencé ou non
    if game.is_playing:
        #déclencher les instructions de la partie
        game.update(screen)
    #vérif di le jeu n'as pas commencé
    else:
        #ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

        save = open("save.txt", "r")
        best_score = save.read()
        font = pygame.font.SysFont('Comic Sans MS', 30)
        score = font.render(f"Meilleur score: {best_score}", False, (255, 255, 255))
        score_rect = score.get_rect()
        screen.blit(score, score_rect)
    
    if game.pressed.get(pygame.K_d):
        game.player.move_right()

    elif game.pressed.get(pygame.K_q):
        game.player.move_left()

    if game.pressed.get(pygame.K_z):
        game.player.move_forward()

    elif game.pressed.get(pygame.K_s):
        game.player.move_back()

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # que l'event est fermeture fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True


            #détecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile_right()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False # fait office d'une fonction input dirrectement proposée par pygame

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #vérif pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.start()
                game.sound_manager.play('click')

    clock.tick(FPS)