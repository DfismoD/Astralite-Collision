import pygame
import pickle

class Score():
    def __inti__(self):
        pygame.display.set_caption("Astralite Collision: Score")

        self.objects = []

    def main(self):

        with open("save.bin", "rb") as f:
            self.objects.append(pickle.load(f))
        
        print(self.objects)