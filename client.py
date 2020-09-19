import pygame
import socket
from model.Pawn import Pawn
from model.Rook import Rook
from model.Ship import Ship
from model.King import King
from model.Knight import Knight
from model.Bishop import Bishop
from model.NSBoard import NSBoard

id_counter = 0
height = 3000
width = 3600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0



def redrawWindow(white, black, board):
    win.fill((255,255,255))
    win.blit(pygame.transform.scale(board.image, (2600, 1600)), board.rect)
    for piece in white:
        win.blit(pygame.transform.scale(piece.image, (200, 200)), (piece.x, piece.y))
    for piece in black:
        win.blit(pygame.transform.scale(piece.image, (200, 200)), (piece.x, piece.y))
    pygame.display.update()


def setupPieces(pieces_b: list, pieces_w: list, id_counter):
    pawns = [Pawn(x * 200, 200, "black") for x in range(13)]
    rooks = [Rook(0, 0, "black"), Rook(2400, 0, "black")]
    bishops = [Bishop(600, 0, "black"), Bishop(800, 0, "black"), Bishop(1600, 0, "black"), Bishop(1800, 0, "black")]
    knights = [Knight(200, 0, "black"), Knight(400, 0, "black"), Knight(2000, 0, "black"), Knight(2200, 0, "black")]
    ships = [Ship(1000, 0, "black"), Ship(1400, 0, "black")]
    pieces_b += pawns + rooks + bishops + knights + [King(1200, 0, "black")] + ships
    ids = id_counter
    for piece in pieces_b:
        piece.id = ids
        ids += 1

    w_pawns = [Pawn(x * 200, 1200, "white") for x in range(13)]
    w_rooks = [Rook(0, 1400, "white"), Rook(2400, 1400, "white")]
    w_bishops = [Bishop(600, 1400, "white"), Bishop(800, 1400, "white"), Bishop(1600, 1400, "white"), Bishop(1800, 1400, "white")]
    w_knights = [Knight(200, 1400, "white"), Knight(400, 1400, "white"), Knight(2000, 1400, "white"), Knight(2200, 1400, "white")]
    w_ships = [Ship(1000, 1400, "white"), Ship(1400, 1400, "white")]
    pieces_w += w_pawns + w_rooks + w_bishops + w_knights + [King(1200, 1400, "white")] + w_ships
    ids = id_counter
    for piece in pieces_w:
        piece.id = ids
        ids += 1

    id_counter = ids
    return pieces_w, pieces_b
    
def main():
    run = True
    current_turn = "w"
    curr_id = None

    board = NSBoard((0, 0, 1300, 800))
    pieces_w, pieces_b = setupPieces([], [], id_counter)
    replace = -1
    dragging = None
    start = None
    while run:      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
             
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = None
                if current_turn == "w":
                    for i in range(len(pieces_w)):
                        if pieces_w[i].rect.collidepoint(pos):
                            clicked = pieces_w[i]
                            replace = i
                            break
                    if clicked:
                        start = (clicked.x, clicked.y)
                        dragging = clicked
                else:
                    for i in range(len(pieces_b)):
                        if pieces_b[i].rect.collidepoint(pos):
                            clicked = pieces_b[i]
                            replace = i
                            break
                    if clicked:
                        start = (clicked.x, clicked.y)
                        dragging = clicked
                
                    
                    

            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging != None and replace >= 0:
                    mouse_pos = pygame.mouse.get_pos()
                    # if current_turn == "w":
                    #     curr_piece = pieces_w[replace]
                    # else:
                    #     curr_piece = pieces_b[replace]
                    # print(curr_piece)
                    # print(mouse_pos)
                    # isvalid = curr_piece.is_valid_move(start, mouse_pos, board)
                    # print(isvalid)
                    # if isvalid:
                    if current_turn == "w":
                        pieces_w[replace] = dragging
                        current_turn = "b"
                    else:
                        pieces_b[replace] = dragging
                        current_turn = "w"
                    replace = -1
                        
                    # else:
                    #     curr_piece.fail_update(win, start)
                    start = None 
                dragging = None
                

                
                
            elif event.type == pygame.MOUSEMOTION and dragging:
                dragging.update(win)
        
        redrawWindow(pieces_w, pieces_b, board)





main()
