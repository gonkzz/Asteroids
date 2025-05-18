# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    # initialize all pygame imported modules
    pygame.init()

    # create new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # object to help track time
    clock = pygame.time.Clock()
    # delta time, time passed since last frame was drawn
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # game loop
    while True:
        # check if the user has closed the window
        # if so exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill black screen
        screen.fill("black")
        # re-render player each frame
        player.draw(screen)
        player.update(dt)
        # refresh the screen
        pygame.display.flip()
        # pause the loop until 1/60th of a sec have passed
        # store that time in milliseconds inside dt
        dt = clock.tick(60) / 1000

    # Print text out to the console
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
