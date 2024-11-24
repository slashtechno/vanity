import importlib
from pathlib import Path
import pygame

pygame.init()

FONT = pygame.font.SysFont("Consolas", 24)
with importlib.resources.path("assets", "__init__.py") as p:
    ASSETS = Path(p).parent
SPRITES = f"{ASSETS}/sprites"