import pygame
import random
from engine.tilesheet import TileSheet
from player import Player


class Game:
    def __init__(self):
        pygame.init()

        resolution = (256, 256)
        screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()

        self.running = True
        self.BaseTileMap = TileSheet(
            screen, 'res/tileset_game_1.png', 8, 8, 3, 4, 32)
        self.decoration = TileSheet(
            screen, 'res/Sprite-0001.png', 8, 8, 1, 1, 32)
        playerImg = self.player = TileSheet(
            screen, 'res/player.png', 8, 8, 1, 2, 32)
        self.player = Player(playerImg)

        self.game_loop()

    def eventmanager(self):
        for event in pygame.event.get():
            self.player.update(event)
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

    def draw(self):
        test = [[0, 3, 3, 3, 3, 3, 3, 6],
                [1, 4, 4, 4, 4, 4, 4, 7],
                [1, 4, 4, 4, 4, 4, 4, 7],
                [1, 4, 4, 4, 4, 4, 4, 7],
                [1, 4, 4, 4, 4, 4, 4, 7],
                [1, 4, 4, 4, 4, 4, 4, 7],
                [1, 4, 4, 4, 4, 4, 4, 7],
                [2, 5, 5, 5, 5, 5, 5, 8]]
        y = 0
        for row in test:
            x = 0
            for tile in row:
                self.BaseTileMap.get_tile(tile, x, y)
                x += 1
            y += 1

    def game_loop(self):
        while self.running:
            self.draw()

            self.player.drawPlayer()

            self.eventmanager()
            pygame.display.flip()
            self.clock.tick(120)


if __name__ == '__main__':
    Game()
