import pygame
import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, surface):
        pygame.draw.circle(
            surface, 
            (255, 255, 255), 
            (self.position.x, self.position.y), 
            self.radius, 
            2
        )

    
    def update(self, dt):
        self.position += self.velocity * dt
        

    def split(self):

        old_radius = self.radius
        old_pos = self.position
        old_vel = self.velocity

        self.kill()


        if old_radius <= ASTEROID_MIN_RADIUS:
            return


        angle = random.uniform(20, 50)

        v1 = old_vel.rotate(+angle) * 1.2
        v2 = old_vel.rotate(-angle) * 1.2

        new_radius = old_radius - ASTEROID_MIN_RADIUS


        a1 = Asteroid(old_pos.x, old_pos.y, new_radius)
        a1.velocity = v1

        a2 = Asteroid(old_pos.x, old_pos.y, new_radius)
        a2.velocity = v2
