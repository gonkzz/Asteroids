import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # Print text out to the console
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize all pygame imported modules
    pygame.init()

    # create new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # object to help track time
    clock = pygame.time.Clock()
    # delta time, time passed since last frame was drawn
    dt = 0

    # managing objects that need certain methods more easily
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # adding classes to the methods group
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # object initialized and stored in variable for later use
    # automatically added to updatable and drawable group
    # game loop interacts with the player through the groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # creating an asteroid field object
    AsteroidField()

    # game loop
    while True:
        # check if the user has closed the window
        # if so exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill black screen
        screen.fill("black")
        # updating follows the same pattern for all objects
        updatable.update(dt)
        # drawing varies between stripes
        for obj in drawable:
            obj.draw(screen)
        # checking for colision between asteroid and player
        for obj in asteroids:
            if obj.collide(player):
                print("Game over!")
                sys.exit()
        # detroying asteroids
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collide(asteroid):
                    asteroid.split()
                    bullet.kill()
        # refresh the screen
        pygame.display.flip()
        # pause the loop until 1/60th of a sec have passed
        # store that time in milliseconds inside dt
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
