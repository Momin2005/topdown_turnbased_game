import pygame
from projectile import Projectile


class Player:
    def __init__(self, image):
        self.player = image
        self.x = 0
        self.y = 0
        # make player and projectile in a group
        self.projectiles = pygame.sprite.Group()
        self.projectile = Projectile(image)

    def drawPlayer(self):
        self.player.get_tile(0, self.x, self.y)
        for i in self.projectiles:
            self.projectile.drawProjectile(i[0], i[1])
            self.projectile.moveProjectiles(i[0], i[1])

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.x -= 1
            elif event.key == pygame.K_d:
                self.x += 1
            elif event.key == pygame.K_z:
                self.y -= 1
            elif event.key == pygame.K_s:
                self.y += 1
            elif event.key == pygame.K_SPACE:
                self.projectiles.append((self.x, self.y))

    def projectile(self):
        self.player.get_tile(1, self.x, self.y)
