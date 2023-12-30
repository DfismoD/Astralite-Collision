import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("Assets/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("Assets/sounds/game_over.ogg"),
            # 'destroyed_meteorite': pygame.mixer.Sound("Assets/sounds/destroyed_meteorite.ogg"),
            'tir': pygame.mixer.Sound("Assets/sounds/tir.ogg"),
            'tir2': pygame.mixer.Sound("Assets/sounds/tir2.ogg"),
            'tir3': pygame.mixer.Sound("Assets/sounds/tir3.ogg"),
            'background' : pygame.mixer.Sound("Assets/sounds/Pulse.ogg"),
            'levelup' : pygame.mixer.Sound("Assets/sounds/levelup.ogg")
        }

    def play(self, name):
        self.sounds[name].play()