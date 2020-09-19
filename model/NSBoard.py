import pygame
import os
from pathlib import Path
dir_path = os.path.dirname(os.path.realpath(__file__))
from model.Piece import Piece as Piece

class NSBoard():
    def __init__(self, rect):
        self.spaces = [[None] * 18] * 8
        self.image = pygame.image.load(str(Path(dir_path).parent) + "/view/nsboard.png")
        self.rect = pygame.Rect(rect)

    # def add_piece(self, p: Piece):
    #     pass

    
