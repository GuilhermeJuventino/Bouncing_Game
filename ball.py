import pygame
import pymunk

import constants as c


class Ball:
    def __init__(self, window, space):
        self.window = window
        self.space = space
        self.body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
        self.body.position = (c.WIDTH / 2, 0)

        self.shape = pymunk.Circle(self.body, 10)
        self.shape.elasticity = 0.9
        self.shape.friction = 0.2
        self.space.add(self.body, self.shape)
    
    def draw(self):
        pygame.draw.circle(self.window, "purple", self.body.position, 10)
