import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = self.velocity.rotate(angle) * 1.2

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = self.velocity.rotate(-1 * angle) * 1.2