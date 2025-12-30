import pygame
import numpy as np


def create(
        tile_size: int, 
        world_dimensions: tuple[int, int]
    ) -> pygame.Surface:
    return pygame.Surface(
        (
            world_dimensions[0] * tile_size, 
            world_dimensions[1] * tile_size
        )
    )
    
    
def initialize(
        world_surface: pygame.Surface, 
        color: tuple, 
        tilemap: np.ndarray,
        tileset: list, 
        tile_size: int
    ) -> pygame.Surface:
    world_surface.fill(color)
    world_surface = draw_world(
        world_surface=world_surface,
        tilemap=tilemap,
        tileset=tileset,
        tile_size=tile_size,
    )
    return world_surface;


def draw_tile(
    world_surface: pygame.Surface,
    tileset: list,
    tile_index: int,
    tile_size: int,
    x: int,
    y: int,
) -> pygame.Surface:
    world_surface.blit(
        tileset[tile_index],
        pygame.Rect(
                x * tile_size, 
                y * tile_size, 
                tile_size, 
                tile_size
        ),
    )
    return world_surface


def draw_world(
    world_surface: pygame.Surface,
    tilemap: np.ndarray,
    tileset: list,
    tile_size: int,
) -> pygame.Surface:
    height = tilemap.shape[0]
    width = tilemap.shape[1]
    for y in range(height):
        for x in range(width):
            tile_index = tilemap.item(y, x)
            world_surface = draw_tile(
                world_surface=world_surface,
                tileset=tileset,
                tile_index=tile_index,
                tile_size=tile_size,
                x=x,
                y=y,
            )
    return world_surface


def fill(
    world_surface: pygame.Surface,
    color: tuple,
) -> pygame.Surface:
    world_surface.fill(color)
    return world_surface