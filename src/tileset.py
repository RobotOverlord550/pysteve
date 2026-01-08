import pygame


def create(
    file_name: str,
    file_ext: str,
    tileset_resource_path: str,
    tile_size_p: int
) -> list:
    """Create a new tileset by preloading from tileset asset

    Args:
        file_name (str): filename of tileset asset
        file_ext (str): extension of tileset asset
        assets_dir_global (str): path to assets directory
        tile_size_p (int): size of the tiles in pixels

    Returns:
        list: _description_"""
    tileset = pygame.image.load(tileset_resource_path)
    tileset_width_pxl = tileset.get_size()[0]
    tileset_height_pxl = tileset.get_size()[1]

    tiles = []

    for y in range(
            0,
            tileset_height_pxl,
            tile_size_p):
        for x in range(
                0,
                tileset_width_pxl,
                tile_size_p):
            tiles.append(
                tileset.subsurface(
                    pygame.Rect(
                        x,
                        y,
                        tile_size_p,
                        tile_size_p
                    )
                )
            )
    return tiles
