import pygame
from circleshape import *
from constants import *

class Bullet(CircleShape):
    def __init__(self, x, y ,radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS
        

    def draw(self, screen):
        pygame.draw.circle(screen, color=(255,255,255), center=self.position, radius=self.radius , width=2)

    def update(self, dt):
        self.position += self.velocity * dt
