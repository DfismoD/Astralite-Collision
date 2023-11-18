import pygame

class Game:
    def __init__(self, screen ,screen_size):
        self.screen = screen
        self.screen_size = screen_size

        pygame.display.set_caption("Astralite Collision: Game")

        # Initialisation des assets
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.scale(self.background, self.screen_size)

        self.astralite_laser = pygame.image.load("assets/astralite_laser.png")

        def font(size):
            return pygame.font.Font("assets/font.ttf", size)

        def main():
            self.run = True
            self.FPS = 60
            self.level = 1
            self.lives = 3

            self.clock = pygame.time.Clock()

            while self.run:
                self.clock.tick(self.FPS)

                self.screen.blit(self.background, (0, 0))
                
                text_lives = font(75).render(f"Vie: {self.lives}", 1, "WHITE")
                text_level = font(75).render(f"Niveau: {self.level}", 1, "WHITE")

                screen.blit(text_level, (10, 0))
                screen.blit(text_lives, (screen_size[0] - text_lives.get_width() - 10, 0))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                        pygame.QUIT()

                pygame.display.update()
        
        main()