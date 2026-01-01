# internal modules
import tileset, tilemap, world, directory, noise, generalmath
# external libraries
import numpy, pygame
from enum import Enum


# constants
WINDOW_DIMENSIONS = (720, 720)
ASSETS_FOLDER_NAME = "assets"
TILESET_FILE_NAME = "tileset"
TILESET_FILE_EXT = ".png"
TILESIZE_PX = 4
WORLD_DIMENSIONS = (512, 512)
BACKGROUND_COLOR = (135, 206, 235)


# reference for tileset
class TileIndex(Enum):
    AIR = 0
    GRASS = 1
    

# main
if __name__ == "__main__":
    # initialize pygame
    pygame.init()
    print("pygame initialized")
    
    # assets directory path
    assets_folder = directory.get_global_path(ASSETS_FOLDER_NAME)
    print(f"set assets directory: {str(assets_folder)}")
    
    # tileset and tilemap setup
    g_tileset = tileset.create(TILESET_FILE_NAME, TILESET_FILE_EXT, assets_folder, TILESIZE_PX)
    print(f"initialized tileset: {str(g_tileset)}")
    g_tilemap = tilemap.create(height=WORLD_DIMENSIONS[1], width=WORLD_DIMENSIONS[0])
    print(f"initialized tilemap: {str(g_tilemap)}")
    tilemap.fill(g_tilemap, TileIndex.GRASS.value)
    print(f"filled tilemap with {str(TileIndex.GRASS.value)}")
    
    # initialize noise with universal seed and apply noise to tilemap to create terrain
    simplex = noise.new_simplex(seed=42)
    print(f"initialized simplex noise algorithm: {str(simplex)}")
    noise.generate_noise2(
        grid=g_tilemap,
        simplex=simplex,
        octaves=4,
        frequency=0.1,
        amplitude=0.5,
        lacunarity=2.0,
        persistance=0.5,
        threshold=0.55,
        new_val=TileIndex.AIR.value,
    )
    print(f"generated caves onto tilemap: {str(g_tilemap)}")
    
    # initialize world and draw tiles onto world
    g_world = world.create(
        tile_size=TILESIZE_PX,
        world_dimensions=WORLD_DIMENSIONS,
        initial_color=BACKGROUND_COLOR
    )
    print(f"initialized world screen: {str(g_world)}")
    world.draw_world(
        world_surface=g_world,
        tilemap=g_tilemap,
        tileset=g_tileset,
        tile_size=TILESIZE_PX
    )
    print(f"drew tilemap onto world: {str(g_world)}")

    # pygame initializations
    screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
    print(f"initialized main screen: {str(screen)}")
    clock = pygame.time.Clock()
    print(f"initialized game clock as {str(clock)}")
    running = True
    
    # debug camera variables
    zoom = 1.0
    move_x = 0.0
    move_y = 0.0

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
        if world_height > world_width:
            window_rect = pygame.Rect(0, 0, world_height, world_height)
        else:
            window_rect = pygame.Rect(0, 0, world_width, world_width)
            
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
        window_rect.width = g_world.get_width() * zoom
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
        pygame.transform.scale(g_world.subsurface(window_rect), WINDOW_DIMENSIONS, screen)

        # reset display
        pygame.display.flip()

        # clock stuff
        clock.tick(60)

    # send a quit event when loop is ended
    print("quiting")
    pygame.quit()
