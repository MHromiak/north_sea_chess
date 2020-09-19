import pygame
import os
from pathlib import Path
dir_path = os.path.dirname(os.path.realpath(__file__))
from model.Piece import Piece as Piece

class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__((x, y, 200, 200), color)
        if self.color == "white":
            self.image = pygame.image.load(str(Path(dir_path).parent) + "/view/w_bishop.png")
        else:
            self.image = pygame.image.load(str(Path(dir_path).parent) + "/view/bishop.png")

    def update(self, surface):
        super().update(surface)


