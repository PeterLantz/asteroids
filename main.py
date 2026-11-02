import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    # Setup Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = updatable
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # Spawn in player
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    AsteroidField()

    # this is the update loop
    while True:
        log_state()

        # this allows the game to quit when you press the x button on the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # this clears the screen
        screen.fill("black")

        # this is where game logic happens, and where things get drawn too
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)

        # update the screen
        pygame.display.flip()

        # this both updates delta time and caps the framerate to 60
        dt = clock.tick(60) / 1000

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()


if __name__ == "__main__":
    main()
