import pygame
import pymunk

import constants as c

class Player:
    def __init__(self, window, space):
        self.window = window
        self.space = space
        self.body = pymunk.Body(1, 100, body_type = pymunk.Body.KINEMATIC)
        self.body.position = (c.WIDTH / 2, 540)

        #self.shape = pymunk.Circle(self.body, 80)
        self.shape = pymunk.Poly.create_box(self.body, (30, 80))

        self.space.add(self.body, self.shape)
        self.rect = pygame.Rect(self.body.position.x, self.body.position.y, 30, 80)

    def update(self):
        self.move_player()
        self.rect.center = self.body.position
    
    def move_player(self):
        mouse_position = pygame.mouse.get_pos()

        self.body.position = (mouse_position[0], 540)

    def draw(self):
        #pygame.draw.circle(self.window, (0, 0, 0), self.body.position, 80)
        pygame.draw.rect(self.window, (0, 0, 0), self.rect)
