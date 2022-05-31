import pygame


class Projectile:
    def __init__(self, img):
        self.projectile = img

    def drawProjectile(self, x, y):
        self.projectile.get_tile(1, x, y)

    def moveProjectiles(self, x, y):
        x += 1


