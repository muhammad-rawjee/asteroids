import pygame
from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white",center=self.position, radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)

        asteroid_split_one_velocity = self.velocity.rotate(split_angle)
        asteroid_split_two_velocity = self.velocity.rotate(-split_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_one.velocity = asteroid_split_one_velocity * 1.2
        asteroid_two.velocity = asteroid_split_two_velocity * 1.2



        
