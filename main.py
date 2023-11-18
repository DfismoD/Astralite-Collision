import pygame, math
from button import Button
from game import Game

# Initialisation de pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_size = screen.get_size()

# Initialisation des assets
img_astralite_icon = pygame.image.load("assets/icon.png")

background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, screen_size)

img_astralite_logo = pygame.image.load("assets/logo.png")
img_astralite_logo = pygame.transform.scale(img_astralite_logo, (screen_size[0]/3, screen_size[1]/3))
img_astralite_logo_rect = img_astralite_logo.get_rect()
img_astralite_logo_rect.x = math.ceil(screen_size[0] / 3)

img_play_btn = pygame.image.load("assets/play_button.png")
img_play_btn = pygame.transform.scale(img_play_btn, (screen_size[0]/4, screen_size[1]/4))
img_play_btn_rect = img_astralite_logo.get_rect()
img_play_btn_rect.x = math.ceil(screen_size[0]/2)
img_play_btn_rect.y = math.ceil(screen_size[1]/2)

# Initialisation de la fenêtre
run = True
clock = pygame.time.Clock()
pygame.display.set_caption("Astralite Collision: Menu")
pygame.display.set_icon(img_astralite_icon)

# Initialisation des variables de couleur
background_color = "#2A5C2F"
font_color = "#ffffff"

#Initialisation de la fonction pour la police d'écriture
def font(size):
    return pygame.font.Font("assets/font.ttf", size)

# bouvle du jeu
while run:

    mouse_pos = pygame.mouse.get_pos()
    keys_pressed = pygame.key.get_pressed()

    # text_menu = font(75).render("ASTRALITE COLISION", True, font_color)
    # rect_menu = text_menu.get_rect(center=(screen_size[0]/2, screen_size[1]/5))

    play_button = Button(image=img_play_btn, pos=img_play_btn_rect, text_input="", font=font(75), base_color=font_color)

    screen.fill(background_color)
    screen.blit(background, (0, 0))
    screen.blit(img_astralite_logo, img_astralite_logo_rect)
    # screen.blit(text_menu, rect_menu)

    for button in [play_button]:
        button.update(screen)

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.chek(mouse_pos):
                game = Game(screen, screen_size)
                game.run()
                pygame.display.quit()




        # █████╗ ███████╗████████╗██████╗  █████╗ ██╗     ██╗████████╗███████╗     ██████╗ ██████╗ ██████╗ ██████╗ 
        # ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔══██╗
        # ███████║███████╗   ██║   ██████╔╝███████║██║     ██║   ██║   █████╗      ██║     ██║   ██║██████╔╝██████╔╝
        # ██╔══██║╚════██║   ██║   ██╔══██╗██╔══██║██║     ██║   ██║   ██╔══╝      ██║     ██║   ██║██╔══██╗██╔═══╝ 
        # ██║  ██║███████║   ██║   ██║  ██║██║  ██║███████╗██║   ██║   ███████╗    ╚██████╗╚██████╔╝██║  ██║██║     
        # ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝   ╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     





                                                #          ██         
                                                #          ██         
                                                #       ████████      
                                                #       ████████      
                                                #       ████████      
                                                #         ████        
                                                #  ████ ████████ ████ 
                                                # ████████████████████
                                                # ████████████████████
                                                #  ████   ████   ████ 
                                                #   ██            ██  