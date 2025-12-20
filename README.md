# Python Terraria Clone

A Pygame-based clone of Terraria, featuring procedural world generation, tile-based rendering, and efficient 2D data structures for optimal performance.

## Project Overview

This project implements a Terraria-like game engine using Pygame Community Edition. It focuses on:
- Efficient 2D data storage using 1D arrays
- Modular architecture with separation of concerns
- Comprehensive unit testing
- Tileset-based rendering system

## Project Structure

```
.
├── LICENSE                    # Project license
├── README.md                  # This file
├── aseprite/                  # Pixel art assets
│   └── tileset.aseprite       # Tileset project file
├── src/                       # Source code directory
│   ├── __main__.py            # Main entry point and game loop
│   ├── __pycache__/           # Python cache directory
│   ├── arr1d_as_2d.py         # 1D-as-2D array utilities
│   ├── const.py               # Game constants and configuration
│   ├── testing.py             # Unit tests
│   ├── world.py.txt           # World generation (in development)
│   └── assets/                # Game assets (textures, sprites)
└── .venv/                     # Python virtual environment
```

## Module Documentation

### arr1d_as_2d.py
Provides efficient 2D data storage using 1D arrays. Two implementations are available:

**NumPy Implementation** (faster, single type):
- `create_1d_as_2d_np(width, height)` - Creates a 1D numpy array representing 2D data
- `set_1d_as_2d_np(arr, val, row, col)` - Sets a value at (row, col)
- `get_1d_as_2d_np(arr, row, col)` - Gets a value at (row, col)

**List Implementation** (flexible, multiple types):
- `create_1d_as_2d_ls(width, height)` - Creates a 1D list representing 2D data
- `set_1d_as_2d_ls(ls, val, row, col)` - Sets a value at (row, col)
- `get_1d_as_2d_ls(ls, row, col)` - Gets a value at (row, col)

**Data Format**: Metadata (width, height) is stored in indices 0-1, followed by array data.

### const.py
Manages game configuration and resources:

- `Constants` class handles:
  - Screen dimensions (1280x720)
  - Tileset loading from assets
  - Tile parsing and storage (4x4 pixel tiles)
  - World dimensions (512x256 tiles)

### __main__.py
Main entry point for the game:
- Initializes Pygame
- Creates the game window
- Runs the game loop at 60 FPS
- Handles window close events

### testing.py
Unit tests for core components:

- `TestConstants` - Verifies Constants class initialization
- `Test1DArrayAs2d` - Tests both numpy and list-based array implementations

## Running the Project

### Prerequisites
```bash
pip install pygame numpy
```

### Run the Game
```bash
python -m src
```

### Run Tests
```bash
python -m unittest src.testing
```

## Asset Pipeline

Pixel art assets are created in Aseprite (`aseprite/tileset.aseprite`) and exported as PNG to `src/assets/tileset.png` for use in the game.

## Future Development

- [ ] Complete world generation system
- [ ] Player sprite and movement
- [ ] Block placement and destruction
- [ ] Enemy AI
- [ ] Inventory system
- [ ] Crafting system