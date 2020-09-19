import pygame

class Piece():
    def __init__(self, rect, color):
        self.rect = pygame.Rect(rect)
        self.image = None
        self.x = rect[0]
        self.y = rect[1]
        self.w = rect[2]
        self.h = rect[3]
        self.id = -1
        self.color = color
    
    def update(self, surface):
        self.rect.center = pygame.mouse.get_pos()
        self.x = self.rect[0]
        self.y = self.rect[1]
        surface.blit(self.image, self.rect)
    
    def fail_update(self, surface, start):
        self.rect[0] = start[0]
        self.rect[1] = start[1]
        surface.blit(self.image, self.rect)
    
    
