import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

time = pygame.time.Clock()
dt = 0.0

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    while (True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Update Player
        dt = time.tick(60) / 1000
        player.update(dt)

        #Render Screen
        screen.fill('black')
        player.draw(screen)

        pygame.display.flip()






if __name__ == "__main__":
    main()
