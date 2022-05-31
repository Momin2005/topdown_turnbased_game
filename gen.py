import pygame
import random
import noise

pygame.init()


class generation():
    def __init__(self, surface):
        print("Generation")
        self.screen = surface

        self.x = -1
        self.y = self.screen.get_height() - 1

        self.list = []

    def gen(self):
        for i in range(0, 400):
            for j in range(0, 400):
                self.list.append((self.x, self.y))
        print(self.list)
        self.perlin()

    def perlin(self):
        for x in range(0, 400):
            for y in range(0, 400):
                a = noise.pnoise2(x*0.3, y)
                print(a)
