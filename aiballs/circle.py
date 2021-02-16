import pygame
import pygame.gfxdraw
import random
import math
from pygame.math import Vector2 as vector

class Circle:
    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.pos.x), int(self.pos.y)), int(self.radius))
    
    @property
    def mass(self):
        return (4/3) * (self.radius**3) * math.pi

    @property
    def impulse(self):
        return self.velocity * self.mass

    @mass.setter
    def mass(self, new_mass):
        self.radius = ((3 * new_mass) / (4 * math.pi)) ** (1/3) 

    def __init__(self, posx = 0, posy = 0, radius = 50, color = pygame.Color("White")):
        self.pos = vector(posx, posy)
        self.radius = radius
        self.color = color
        self.velocity = vector(0, 0)
       
    def borders(self, window):
        if self.pos.x - self.radius <= 0:
            self.velocity.x *= -1
            self.pos.x = self.radius
        if self.pos.x + self.radius >= window.get_size()[0]:
            self.velocity.x *= -1
            self.pos.x = window.get_size()[0] - self.radius
        if self.pos.y - self.radius <= 0:
            self.velocity.y *= -1
            self.pos.y = self.radius
        if self.pos.y + self.radius >= window.get_size()[1]:
            self.velocity.y *= -1
            self.pos.y = window.get_size()[1] - self.radius
       
    def physics(self, milliseconds):
        self.pos.x += self.velocity.x * milliseconds/1000
        self.pos.y += self.velocity.y * milliseconds/1000