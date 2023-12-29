import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("Assets/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("Assets/sounds/game_over.ogg"),
            # 'destroyed_meteorite': pygame.mixer.Sound("Assets/sounds/destroyed_meteorite.ogg"),
            # 'tir': pygame.mixer.Sound("Assets/sounds/tir.ogg")
        }

    def play(self, name):
        self.sounds[name].play()