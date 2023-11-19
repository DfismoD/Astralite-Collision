import pygame
from player import Player
from meteorite_event import MeteoriteFallEvent

class Game:
    def __init__(self, screen ,screen_size):
        self.screen = screen
        self.screen_size = screen_size

        # self.all_players = pygame.sprite.Group()
        self.player = Player()
        self.meteorite_event =  MeteoriteFallEvent(self)

        pygame.display.set_caption("Astralite Collision: Game")

        # Initialisation des assets
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.scale(self.background, self.screen_size)

    def font(self, size):
        return pygame.font.Font("assets/font.ttf", size)
    
    def chek_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False)

    def main(self):
        run = True

        clock = pygame.time.Clock()

        while run:

            self.screen.blit(self.background, (0, 0))

            self.level = 0
            self.lives = self.player.health

            self.screen.blit(self.player.img, self.player.rect)

            self.meteorite_event.update_bar(self.screen)
            self.meteorite_event.all_meteorite.draw(self.screen)

            for laser in self.player.all_lasers:
                laser.move()

            self.player.all_lasers.draw(self.screen)

            for meteorite in self.meteorite_event.all_meteorite:
                meteorite.fall()

            text_lives = self.font(75).render(f"Vies: {self.lives}", 1, "WHITE")
            text_level = self.font(75).render(f"Niveau: {self.level}", 1, "WHITE")

            self.screen.blit(text_level, (10, 0))
            self.screen.blit(text_lives, (self.screen_size[0] - text_lives.get_width() - 10, 0))

            self.player.handle_input()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()

            clock.tick(60)

            pygame.display.update()