import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

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
        player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
        player.draw(screen=screen)

        # update the screen
        pygame.display.flip()

        # this both updates delta time and caps the framerate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
