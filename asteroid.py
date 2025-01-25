import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_WIDTH, ASTEROID_VELOCITY_CHANGE, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_WIDTH)

    def update(self, dt):
        self.position+= self.velocity * dt

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        angle_diff = random.uniform(20, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = self.velocity * ASTEROID_VELOCITY_CHANGE
        a1.velocity = a1.velocity.rotate(angle_diff)

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = self.velocity * ASTEROID_VELOCITY_CHANGE
        a2.rotation = a1.velocity.rotate(-angle_diff)