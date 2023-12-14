import pygame, random

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'Assets/{sprite_name}.png')
        self.current_image = 0 #commencer l'anim à l'img 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #méthode pour démarer l'animation
    def start_animation(self):
        self.animation = True

    #définir une méthode pour animer le sprite
    def animate(self, loop=False):

        if self.animation:

            #passer à l'image suivante
            self.current_image += random.randint(0,1)

            #vérif si on a atteint la fin de l'anim
            if self.current_image >= len(self.images):
                #remettre l'animation au départ
                self.current_image = 0
                
            if loop is False:

                #désactivation de l'animation
                self.animation = False

            #modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]

#déd pour charger les images d'un sprite car si on charge les images des la classe cv buguer
def load_animation_images(sprite_name):
    images = []
    path = f"Assets/{sprite_name}/{sprite_name}"

    #boucler sur chaque image dans ce dossier
    for num in range(1, 2):
        image_path = path + str(num) + '.png'
        images.append(pygame.transform.scale(pygame.image.load(image_path), (200,200)))

    #renboyer le contenu de la liste d'images
    return images


animations = {'Vaisseau_Gold': load_animation_images('Vaisseau_Gold')}