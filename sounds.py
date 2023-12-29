import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("Assets/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("Assets/sounds/click.ogg"),
            'destroyed_meteorite': pygame.mixer.Sound("Assets/sounds/destroyed_meteorite.ogg"),
            'tir': pygame.mixer.Sound("Assets/sounds/tir.ogg")
        }