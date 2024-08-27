# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    oClock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = updatable, drawable

    oPlayer = Player( ( SCREEN_WIDTH / 2 ), ( SCREEN_HEIGHT / 2 ))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)



        pygame.display.flip()
        dt = oClock.tick(60) / 1000
        

if __name__ == "__main__":
    main()