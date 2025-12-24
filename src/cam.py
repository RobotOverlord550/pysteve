from numpy import Vec2D
from world import World
from pygame import Screen
from const import Constants
import data_structures


class Camera():
    def __init__(self, width: float, height: float):
        self.position: Vec2D = Vec2D(0, 0)
        self.width = width
        self.height = height
        
    
    def render_frame(self, world: World, const: Constants):
        render_screen = Screen(self.width, self.height)
        block_width = round(self.width / const.TILE_PXL_SIZE)
        block_height = round(self.height / const.TILE_PXL_SIZE)
        for x in range(block_width):
            for y in range(block_height):
                scan_position: Vec2D = self.position + Vec2D(x, y)
                scan_tile = data_structures.get_1d_as_2d_np(world.world_tilemap, 
                                                        scan_position.x, scan_position.y)
                if scan_tile != None:
                    tile = const.TILESET[scan_tile]
                    render_screen.blit(tile, (x, y))