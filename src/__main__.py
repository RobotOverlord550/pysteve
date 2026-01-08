import tileset
import tilemap
import world
import directory
import noise
import generalmath
import pygame
import configparser
import os
from pathlib import Path
from enum import Enum


# constants
SEED = 42
ASSETS_FOLDER_NAME = "assets"
SETTINGS_FOLDER_NAME = "settings"
CONFIG_FILE_NAME = "config"
CONFIG_FILE_EXTENSION = ".ini"
TILESET_FILE_NAME = "tileset"
TILESET_FILE_EXT = ".png"
TILESIZE_PX = 8
WORLD_DIMENSIONS = (256, 256)
BACKGROUND_COLOR = (135, 206, 235)


# reference for tileset
class TileIndex(Enum):
    AIR = 0
    GRASS = 1


def create_config(config_file_path: Path):
    """create a config file to persistently store settings in"""
    config = configparser.ConfigParser()
    config['video'] = {
        'window-height': 720,
        'window-width': 720
    }
    with open(config_file_path, 'w') as configfile:
        config.write(configfile)


def read_config(config_file_path: Path) -> dict:
    """read the current config file

    Returns:
        dict: dictionary of config values"""
    config = configparser.ConfigParser()
    config.read(config_file_path)
    window_height = config.getint('video', 'window-height')
    window_width = config.getint('video', 'window-width')
    config_values = {
        'window_height': window_height,
        'window_width': window_width
    }
    return config_values

if __name__ == "__main__":
    #___Initialization Phase___
    # initialize pygame
    pygame.init()
    print("pygame initialized")
    # tileset resource path
    tileset_resource_path = directory.resource_path(
        ASSETS_FOLDER_NAME + "/" + TILESET_FILE_NAME + TILESET_FILE_EXT
        )
    print("set tileset filepath: " + str(tileset_resource_path))
    # config file
    config_file = "" + CONFIG_FILE_NAME + CONFIG_FILE_EXTENSION
    config_file_path = directory.resource_path(
        "" + SETTINGS_FOLDER_NAME + "/" + config_file
        )
    # initialize config
    config_values = read_config(config_file_path=config_file_path)
    print(config_values['window_height'])
    print(config_values['window_width'])
    # tileset and tilemap setup
    g_tileset = tileset.create(
        TILESET_FILE_NAME,
        TILESET_FILE_EXT,
        tileset_resource_path,
        TILESIZE_PX
        )
    print("initialized tileset: " + str(g_tileset))
    g_tilemap = tilemap.create(
        WORLD_DIMENSIONS[0],
        WORLD_DIMENSIONS[1]
    )
    print("initialized tilemap: " + str(g_tilemap))
    tilemap.fill(g_tilemap, TileIndex.GRASS.value)
    print("filled tilemap with " + str(TileIndex.GRASS.value))
    # initialize noise with universal seed and apply noise to
    # tilemap to create terrain
    simplex = noise.new_simplex(seed=42)
    print("initialized simplex noise algorithm: " + str(simplex))
    noise.generate_noise2(
        grid=g_tilemap,
        simplex=simplex,
        octaves=2,
        frequency=0.2,
        amplitude=0.5,
        lacunarity=2.0,
        persistance=0.5,
        threshold=0.56,
        new_val=TileIndex.AIR.value,
    )
    print("generated caves onto tilemap: " + str(g_tilemap))
    noise.generate_noise1(
        grid=g_tilemap,
        max_row=64,
        min_row=32,
        simplex=simplex,
        octaves=4,
        frequency=0.2,
        amplitude=0.5,
        lacunarity=2.0,
        persistence=0.5,
        new_val=TileIndex.AIR.value
    )
    tilemap.fill_subsection(
        tilemap=g_tilemap,
        subsection_tl_col=0,
        subsection_tl_row=0,
        subsection_br_col=g_tilemap.shape[0],
        subsection_br_row=32,
        tile_index=TileIndex.AIR.value
    )
    # initialize world and draw tiles onto world
    g_world = world.create(
        tile_size=TILESIZE_PX,
        world_dimensions=WORLD_DIMENSIONS,
        initial_color=BACKGROUND_COLOR
    )
    print("initialized world screen: " + str(g_world))
    world.draw_world(
        world_surface=g_world,
        tilemap=g_tilemap,
        tileset=g_tileset,
        tile_size=TILESIZE_PX
    )
    print("drew tilemap onto world: " + str(g_world))

    # pygame initializations
    screen = pygame.display.set_mode((
        config_values['window_width'],
        config_values['window_height']
    ))
    print("initialized main screen: " + str(screen))
    clock = pygame.time.Clock()
    print("initialized game clock as " + str(clock))
    running = True
    # debug camera variables
    zoom = 1.0
    move_x = 0.0
    move_y = 0.0

    #___Game Loop Phase___
    # main game loop
    while running:
        # event handling
        for event in pygame.event.get():
            # handle quit
            if event.type == pygame.QUIT:
                print("Quit event received")
                running = False
        # Escape
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            print("Escape pressed, quitting")
            running = False

        # sets initial view rect size
        world_height, world_width = g_world.get_size()
        window_rect = pygame.Rect(0, 0, world_height, world_height)
        # Zoom in/out
        if keys[pygame.K_z]:
            if keys[pygame.K_z and pygame.K_UP]:
                zoom = zoom * .9
            if keys[pygame.K_z and pygame.K_DOWN]:
                zoom = zoom / .9
            zoom = generalmath.clamp(zoom, 0.01, 1)

        # move around world
        else:
            if keys[pygame.K_LEFT or pygame.K_a]:
                move_x -= 10 * zoom
            if keys[pygame.K_RIGHT or pygame.K_d]:
                move_x += 10 * zoom
            if keys[pygame.K_UP or pygame.K_w]:
                move_y -= 10 * zoom
            if keys[pygame.K_DOWN or pygame.K_s]:
                move_y += 10 * zoom

        # set size of view rect based on input
        window_rect.width = g_world.get_height() * zoom
        window_rect.height = g_world.get_height() * zoom

        # set location of view rect based on input
        move_x = generalmath.clamp(
            move_x,
            0,
            g_world.get_width() - window_rect.width
        )
        move_y = generalmath.clamp(
            move_y,
            0,
            g_world.get_height() - window_rect.height
        )
        window_rect.x = move_x
        window_rect.y = move_y

        # scale view rect to window
        pygame.transform.scale(
            g_world.subsurface(window_rect),
            (
                config_values['window_width'],
                config_values['window_height']
            ),
            screen
        )

        # reset display
        pygame.display.flip()

        # clock stuff
        clock.tick(60)

    #___Game End Phase___
    # send a quit event when loop is ended
    print("quiting")
    pygame.quit()
