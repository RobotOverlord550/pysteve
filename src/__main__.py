import tileset, tilemap, world, math, pygame, directory
from enum import Enum


def clamp(x, minimum, maximum):
    return max(minimum, min(x, maximum))


WINDOW_DIMENSIONS = (720, 720)
ASSETS_FOLDER_NAME = "assets"
TILESET_FILE_NAME = "tileset"
TILESET_FILE_EXT = ".png"
TILESIZE_PX = 4
WORLD_DIMENSIONS = (512, 512)
BACKGROUND_COLOR = (135, 206, 235)


class TileIndex(Enum):
    AIR = 0
    GRASS = 1
    

if __name__ == "__main__":
    pygame.init()
    
    assets_folder = directory.get_global_path(ASSETS_FOLDER_NAME)
    g_tileset = tileset.create(TILESET_FILE_NAME, TILESET_FILE_EXT, assets_folder, TILESIZE_PX)
    g_tilemap = tilemap.create(WORLD_DIMENSIONS[0], WORLD_DIMENSIONS[1])
    tilemap.fill(g_tilemap, TileIndex.GRASS.value)
    perlin = tilemap.init_perlin(seed=42)
    tilemap.apply_noise(
        tilemap=g_tilemap,
        opensimplex=perlin,
        octaves=10,
        scale=10,
        min_row=64,
        max_row=448,
        below_index=TileIndex.AIR.value,
    )
    g_world = world.create(tile_size=TILESIZE_PX, world_dimensions=WORLD_DIMENSIONS)
    world.initialize(
        world_surface=g_world,
        color=BACKGROUND_COLOR,
        tilemap=g_tilemap,
        tileset=g_tileset,
        tile_size=TILESIZE_PX
    )

    print("g_world pixel size:", g_world.get_size())

    screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
    clock = pygame.time.Clock()
    running = True
    zoom = 1.0
    move_x = 0.00
    move_y = 0.00

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window_rect = pygame.Rect(0, 0, g_world.get_width(), g_world.get_height())

        # Escape
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
            
        # Zoom in/out
        if keys[pygame.K_z]:
            print("Zoom mode")
            if keys[pygame.K_z and pygame.K_UP]:
                zoom = zoom * .9
                print("Zoomed in | Zoom: ", zoom)
            if keys[pygame.K_z and pygame.K_DOWN]:
                zoom = zoom / .9
                print("Zoomed out | Zoom: ", zoom)
            zoom = clamp(zoom, 0.01, 1)

        # Move around world
        else:
            print("Move mode (Default)")
            if keys[pygame.K_LEFT or pygame.K_a]:
                print("Moving left")
                move_x -= 10 * zoom
            if keys[pygame.K_RIGHT or pygame.K_d]:
                print("Moving right")
                move_x += 10 * zoom
            if keys[pygame.K_UP or pygame.K_w]:
                print("Moving up")
                move_y -= 10 * zoom
            if keys[pygame.K_DOWN or pygame.K_s]:
                print("Moving down")
                move_y += 10 * zoom

        window_rect.width = g_world.get_width() * zoom
        window_rect.height = g_world.get_height() * zoom

        move_x = clamp(
            move_x,
            0,
            g_world.get_width() - window_rect.width
        )
        move_y = clamp(
            move_y,
            0, 
            g_world.get_height() - window_rect.height
        )
        window_rect.x = move_x
        window_rect.y = move_y


        pygame.transform.scale(g_world.subsurface(window_rect), WINDOW_DIMENSIONS, screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
