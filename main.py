import asyncio
import pygame
import pymunk

import player
import baskets

import constants as c

from sys import exit

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Bouncing_Game")

space = pymunk.Space()
space.gravity = 0, 981

player = player.Player(window, space)
blue_basket = baskets.Basket(window, space, (c.BLUE_BASKET_X, 540), "blue")
red_basket = baskets.Basket(window, space, (c.RED_BASKET_X, 540), "red")

async def main():
    while True:
        clock.tick(60)
        space.step(1/50)
        keystate = pygame.key.get_pressed()

        window.fill((217, 217, 217))

        player.draw()
        blue_basket.draw()
        red_basket.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
            if keystate[pygame.K_ESCAPE]:
                pygame.quit()
                exit()

        player.update()
        pygame.display.update()

        await asyncio.sleep(0) # Important! And should be kept at 0

if __name__ == "__main__":
    asyncio.run(main())
