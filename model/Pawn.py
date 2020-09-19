import pygame
import os
from pathlib import Path
dir_path = os.path.dirname(os.path.realpath(__file__))
from model.Piece import Piece as Piece

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__((x, y, 200, 200), color)
        if self.color == "white":
            self.image = pygame.image.load(str(Path(dir_path).parent) + "/view/w_pawn.png")
        else:
            self.image = pygame.image.load(str(Path(dir_path).parent) + "/view/pawn.png")

    def update(self, surface):
        super().update(surface)

    def fail_update(self, surface, start):
        super().fail_update(surface, start)

    # def is_valid_move(self, start, dest: tuple, board) -> bool:
    #     curr_x, curr_y = ((start[0] + 50) // 200), ((start[1] + 50) // 200)
    #     dest_x, dest_y = (dest[0] // 200), (dest[1] // 200)
    #     print()
    #     print(start[0], start[1])
    #     print(dest)
    #     print(self.rect.center)
    #     print(curr_x, curr_y)
    #     print(dest_x, dest_y)
    #     if abs(dest_y - curr_y) == 1:
    #         print("Y 1")
    #         if abs(dest_x - curr_x) == 1 and board.spaces[dest_y][dest_x] != []:
    #             print("Captured")
    #             return True
    #         elif dest_x - curr_x == 0:
    #             print("Just moved")
    #             return True
    #         return False        
    #     return False



