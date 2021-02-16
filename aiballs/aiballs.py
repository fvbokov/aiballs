import sys
import pygame
from pygame.locals import *
import random
import time
from pygame.math import Vector2 as vector

from .circle import Circle
from .character import Character
from .mouse import Mouse
from .collision import check_collisions

def play():
    pygame.init() 

    window = pygame.display.set_mode((800, 600))

    clock = pygame.time.Clock()
    milliseconds = 0
    FPS = 1000

    character = Character(400, 400, 100, pygame.Color("Red"))

    balls = []
    balls.append(Circle(200, 300, 70))    
    balls[0].velocity = vector(0,0)

    window.fill("Black")

    mouse = Mouse()

    while True:
        milliseconds = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        window.fill("Black")
        
        mouse.update()
        
        character.physics(milliseconds)
        character.borders(window)

        character.control(mouse.state, balls)
        check_collisions(character, balls)
        character.draw(window)

        if character.radius < 3:
            print("You lost")
            pygame.quit()

        i = 0
        for ball in balls:
            ball.physics(milliseconds)
            ball.borders(window)
            check_collisions(ball, balls)
            ball.draw(window)
            if (balls[i].radius < 3):
                del balls[i]
            i += 1 
        
        pygame.display.flip()