import pygame
from circleshape import CircleShape
import constants

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, -constants.PLAYER_SHOOT_SPEED)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt