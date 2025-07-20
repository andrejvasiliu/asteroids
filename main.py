import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    print("Starting Asteroids!")
    print(
f"""Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)

    AsteroidField.containers = (updatables)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))  # Fill the screen with black
        # player.draw(screen)  # Draw the player
        # player.update(dt)
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()  # Update the display
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
