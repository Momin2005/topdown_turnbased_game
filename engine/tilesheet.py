import pygame


class TileSheet:
    def __init__(self, screen, fn, width, height, rows, cols, size):
        image = pygame.image.load(fn)
        self.screen = screen
        self.size = size
        self.tile_table = []
        self.all_tiles = []
        for tile_x in range(0, cols):
            line = []
            self.tile_table.append(line)
            for tile_y in range (0, rows):
                rect = (tile_x * width, tile_y * height, width, height)
                line.append(image.subsurface(rect))
        self.create_tilesheet()

    def get_tile(self, tileNumber, x, y):
        x *= self.size
        y *= self.size
        tile = self.all_tiles[tileNumber]
        tile = pygame.transform.scale(tile, (self.size, self.size))
        self.screen.blit(tile, (x, y))

    def create_tilesheet(self):
        for x, row in enumerate(self.tile_table):
            for y, tile in enumerate(row):
                tile = pygame.transform.scale(tile, (self.size, self.size))
                self.all_tiles.append(tile)
                

