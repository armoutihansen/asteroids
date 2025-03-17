import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
import constants
from player import Player
import sys

from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    
    dt = 0
    
    print("Starting Asteroids!")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        
        for ast in asteroids:
            if ast.check_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if ast.check_collision(shot):
                    shot.kill()
                    ast.split()
                    
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        
        #limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()