from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += ( self.velocity * dt )

    def split(self, screen):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            positive_angle = self.velocity.rotate(random_angle)
            negative_angle = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x,self.position.y, new_radius)
            asteroid.velocity = positive_angle * 1.2
            asteroid_two = Asteroid(self.position.x,self.position.y, new_radius)
            asteroid_two.velocity = negative_angle * 1.2
