import pygame


def create(
        file_name: str, 
        file_ext: str, 
        assets_dir_global: str, 
        tile_size_p: int) -> list:
    tileset: pygame.Surface = pygame.image.load(
        "" + assets_dir_global + "/" + file_name + file_ext
    )

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
            
    print("Created tileset with", len(tiles), "tiles")
    return tiles