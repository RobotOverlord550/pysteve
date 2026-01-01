import pygame
import numpy as np


def draw_world(
    world_surface: pygame.Surface,
    tilemap: np.ndarray,
    tileset: list,
    tile_size: int,
): 
    """draws world based on tilemap

    Args:
        world_surface (pygame.Surface): initialized world surface
        tilemap (np.ndarray): tilemap to reference
        tileset (list): tileset to reference
        tile_size (int): tile size in pixels
    """    
    height = tilemap.shape[0]
    width = tilemap.shape[1]
    for y in range(height):
        for x in range(width):
            tile_index = tilemap.item(y, x)
            world_surface = _draw_tile(
                world_surface=world_surface,
                tileset=tileset,
                tile_index=tile_index,
                tile_size=tile_size,
                row=x,
                col=y,
            )


def _draw_tile(
    world_surface: pygame.Surface,
    tileset: list,
    tile_index: int,
    tile_size: int,
    row: int,
    col: int,
):
    """draw tile at specified location

    Args:
        world_surface (pygame.Surface): surface to draw on
        tileset (list): tileset to reference
        tile_index (int): tile index to use
        tile_size (int): tile size in pixels
        row (int): row to use
        col (int): collumn
    """    
    world_surface.blit(
        tileset[tile_index],
        pygame.Rect(
                row * tile_size, 
                col * tile_size, 
                tile_size, 
                tile_size
        ),
    )
    return world_surface


def create(
        tile_size: int, 
        world_dimensions: tuple[int, int],
        initial_color: tuple,
    ) -> pygame.Surface:
    """create new world surface to draw objects on

    Args:
        tile_size (int): size of tiles in pixels
        world_dimensions (tuple[int, int]): dimensions of the world in tiles
        initial_color (tuple): background color

    Returns:
        pygame.Surface: initialized world represented as a Pygame Surface
    """    
    width = world_dimensions[1] * tile_size
    height = world_dimensions[0] * tile_size
    world: pygame.Surface = pygame.Surface((width, height))
    world.fill(color=initial_color)
    return world