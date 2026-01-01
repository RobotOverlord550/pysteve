import tileset, tilemap, world, pygame, directory, numpy, noise
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
    
    rng = numpy.random.default_rng()
    
    assets_folder = directory.get_global_path(ASSETS_FOLDER_NAME)
    g_tileset = tileset.create(TILESET_FILE_NAME, TILESET_FILE_EXT, assets_folder, TILESIZE_PX)
    g_tilemap = tilemap.create(height=WORLD_DIMENSIONS[1], width=WORLD_DIMENSIONS[0])
    tilemap.fill(g_tilemap, TileIndex.GRASS.value)
    simplex = noise.new_simplex(seed=42)
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
    move_x = 0.0
    move_y = 0.0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit event received")
                running = False

        world_height, world_width = g_world.get_size()
        if world_height > world_width:
            window_rect = pygame.Rect(0, 0, world_height, world_height)
            print("Creating window rect based on height:", window_rect)
        else:
            window_rect = pygame.Rect(0, 0, world_width, world_width)
            print("Creating window rect based on width:", window_rect)

        # Escape
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            print("Escape pressed, quitting")
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
                move_x -= 10 * zoom
                print("move_x:", move_x)
            if keys[pygame.K_RIGHT or pygame.K_d]:
                move_x += 10 * zoom
                print("move_x:", move_x)
            if keys[pygame.K_UP or pygame.K_w]:
                move_y -= 10 * zoom
                print("move_y:", move_y)
            if keys[pygame.K_DOWN or pygame.K_s]:
                move_y += 10 * zoom
                print("move_y:", move_y)

        window_rect.width = g_world.get_width() * zoom
        print("window_rect.width:", window_rect.width)
        window_rect.height = g_world.get_height() * zoom
        print("window_rect.height:", window_rect.height)

        move_x = clamp(
            move_x,
            0,
            g_world.get_width() - window_rect.width
        )
        print("clamped move_x:", move_x)
        move_y = clamp(
            move_y,
            0, 
            g_world.get_height() - window_rect.height
        )
        print("clamped move_y:", move_y)
        window_rect.x = move_x
        print("window_rect.x:", window_rect.x)
        window_rect.y = move_y
        print("window_rect.y:", window_rect.y)


        pygame.transform.scale(g_world.subsurface(window_rect), WINDOW_DIMENSIONS, screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
