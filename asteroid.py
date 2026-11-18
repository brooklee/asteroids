from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        # Implementation for splitting the asteroid
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
           
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            a1= Asteroid(self.position.x, self.position.y, new_radius)
            a2= Asteroid(self.position.x, self.position.y, new_radius)

            a1.velocity = v1*1.2
            a2.velocity = v2*1.2

