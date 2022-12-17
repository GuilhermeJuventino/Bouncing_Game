import pygame
import pymunk


class Player:
    def __init__(self, window, space):
        self.window = window
        self.space = space
        self.body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
        self.body.position = (400, 100)

        self.shape = pymunk.Circle(self.body, 80)

        self.space.add(self.body, self.shape)

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.window, (0, 0, 0), self.body.position, 80)
