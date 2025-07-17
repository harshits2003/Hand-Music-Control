import pygame
import numpy as np

class MusicController:
    def __init__(self, music_path):
        pygame.init()
        pygame.mixer.init()
        self.music = pygame.mixer.music
        self.music.load(music_path)
        self.music.play(-1)  # Play in loop

    def set_volume(self, distance):
        volume = np.interp(distance, [50, 300], [0.0, 1.0])  # Map hand distance to volume
        self.music.set_volume(volume)

    def set_speed(self, speed_factor):
        fade_time = int(1000 / speed_factor)
        self.music.play(-1, start=0, fade_ms=fade_time)  # Adjust playback speed

    def set_pitch(self, pitch_factor):
        volume_adjust = np.interp(pitch_factor, [10, 100], [0.5, 2.0])
        pygame.mixer.Sound.set_volume(pygame.mixer.Sound('music/sample.mp3'), volume_adjust)
