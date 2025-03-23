import pygame
from sys import exit

pygame.init()

font = pygame.font.Font('Assets/Fonts/BagelFatOne-Regular.ttf', 70)

clock = pygame.time.Clock()
pygame.display.set_caption('Tic Tac Toe')
screen = pygame.display.set_mode((480, 580))

back_surf = pygame.image.load('Assets/Images/backgrnd.png').convert_alpha()

title = font.render('Tic Tac Toe', True, '#ede1c7')
title_rect = title.get_rect(midbottom = (240, 100))

click = pygame.mouse.get_just_pressed
pos = pygame.mouse.get_pos

x_surf = pygame.image.load('Assets/Images/x.png').convert_alpha()
o_surf = pygame.image.load('Assets/Images/o.png').convert_alpha()

xo = x_surf

tp = False
tlp = False
trp = False
mp = False
mlp = False
mrp = False
bp = False
blp = False
brp = False


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(back_surf,(0,0))
    screen.blit(title,title_rect)

    #top
    if pygame.draw.rect(screen, 'Red', (187,195,112,103)).collidepoint(pos()) and click()[0]:
        if tp == False:
            print('collision top')
            tp = True

    #top left
    if pygame.draw.rect(screen, 'Red', (76,195,101,103)).collidepoint(pos()) and click()[0]:
        if tlp == False:
            print('collision top left')
            tlp = True

    #top right
    if pygame.draw.rect(screen, 'Red', (308,195,103,103)).collidepoint(pos()) and click()[0]:
        if trp == False:
            print('collision top right')
            trp = True

    #middle
    if pygame.draw.rect(screen, 'Red', (187,306,112,113)).collidepoint(pos()) and click()[0]:
        if mp == False:
            print('collision middle')
            mp = True

    #midlle left
    if pygame.draw.rect(screen, 'Red', (76,306,101,113)).collidepoint(pos()) and click()[0]:
        if mlp == False:
            print('collision middle left')
            mlp = True

    #midlle right
    if pygame.draw.rect(screen, 'Red', (308,306,103,113)).collidepoint(pos()) and click()[0]:
        if mrp == False:
            print('collision middle right')
            mrp = True

    #bottom
    if pygame.draw.rect(screen, 'Red', (187,427,112,102)).collidepoint(pos()) and click()[0]:
        if bp == False:
            print('collision bottom')
            bp = True

    #bottom left
    if pygame.draw.rect(screen, 'Red', (76,427,101,102)).collidepoint(pos()) and click()[0]:
        if blp == False:
            print('collision bottom left')
            blp = True

    #bottom right
    if pygame.draw.rect(screen, 'Red', (308,427,103,102)).collidepoint(pos()) and click()[0]:
        if brp == False:
            print('collision bottom right')
            brp = True

    pygame.display.update()
    clock.tick(60)