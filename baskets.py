import pygame
import pymunk

import constants as c


class Basket:
    def __init__(self, window, space, pos, color):
        self.window = window
        self.space = space
        self.pos = pos
        self.color = color
        self.body = pymunk.Body(1, 100, body_type = pymunk.Body.STATIC)
        self.body.position = self.pos

        self.shape = pymunk.Poly.create_box(self.body, (150, 100))
        
        self.space.add(self.body, self.shape)
        self.rect = pygame.Rect(self.body.position.x, self.body.position.y, 150, 100)
        self.rect.center = (self.body.position.x, self.body.position.y)

    def draw(self):
       pygame.draw.rect(self.window, self.color, self.rect)