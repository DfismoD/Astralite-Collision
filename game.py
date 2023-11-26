import pygame
from player import Player
from meteorite_event import MeteoriteFallEvent

class Game:
    def __init__(self, screen ,screen_size):
        self.screen = screen
        self.screen_size = screen_size

        self.player = Player()
        self.all_players = pygame.sprite.Group()

        self.meteorite_event = MeteoriteFallEvent()

        self.img_life_bar = pygame.image.load("assets/life_bar.png")
        self.img_life_bar = pygame.transform.scale(self.img_life_bar, (self.screen_size[0]/4, self.screen_size[1]/15))
        self.img_life_bar_size = self.img_life_bar.get_size()
        self.img_life_bar_position = (10, self.screen_size[1] - self.img_life_bar_size[1] - 10)

        self.img_ulti_bar = pygame.image.load("assets/ulti_bar.png")
        self.img_ulti_bar = pygame.transform.scale(self.img_ulti_bar, (self.screen_size[0]/4, self.screen_size[1]/15))
        self.img_ulti_bar_size = self.img_ulti_bar.get_height()

        pygame.display.set_caption("Astralite Collision: Game")

        # Initialisation des assets
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.scale(self.background, self.screen_size)

    def font(self, size):
        return pygame.font.Font("assets/font.ttf", size)
 

    def main(self):
        run = True

        clock = pygame.time.Clock()

        while run:

            self.screen.blit(self.background, (0, 0))

            self.level = 0
            
            self.player.handle_input()
            self.screen.blit(self.player.img, self.player.rect)
            self.player.update_health_bar(self.screen, self.img_life_bar_position)

            for laser in self.player.all_lasers:
                laser.move()

            self.player.all_lasers.draw(self.screen)

            self.meteorite_event.update_bar(self.screen)
            self.meteorite_event.all_meteorite.draw(self.screen)

            for meteorite in self.meteorite_event.all_meteorite:
                meteorite.fall()

            text_level = self.font(75).render(f"NIVEAU: {self.level}", 1, "WHITE")
            self.screen.blit(text_level, (10, 0))

            self.screen.blit(self.img_life_bar, self.img_life_bar_position)
            self.screen.blit(self.img_ulti_bar, (10, self.screen_size[1] - self.img_life_bar_size[1] - self.img_ulti_bar_size - 20))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()

            clock.tick(60)

            pygame.display.update()