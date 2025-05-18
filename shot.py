import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # bullet center (x, y)
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "yellow", center, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
