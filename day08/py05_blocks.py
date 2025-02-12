import pygame   
from pygame.locals import QUIT , KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, Rect
import sys      

import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
pygame.init()
screen_surface = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT ))
pygame.display.set_icon(pygame.image.load('./day08/block.png'))
FPSCLOCK= pygame.time.Clock()
pygame.display.set_caption('Blocks Pygame')
pygame.key.set_repeat(10,10)


def main():
    is_game_str = False
    score = 0
    Block = []

    # 클래스 생성

    # 벽돌 색 (무지개색)
    colors = [(255,0,0),(255,150,0),(255,228,0),(11,201,4),(0,80,255),(0,0,147),(201,0 ,167)]
    
    bigFont = pygame.font.SysFont('NanumGothic',80)
    smallFont = pygame.font.SysFont('NanumGothic',45)

    M_GAME_TITLE = bigFont.render('GAME START?' , True, 'white')
    M_GAME_SUBTITLE = smallFont.render('PRESS SPACE_BAR' , True, 'white')
    M_CLEAR = bigFont.render('CLEAR!' , True, 'green')
    M_FAIL = bigFont.render('FAILED!' , True, 'red')

    while True:
        screen_surface.fill(color= 'black')  
        for event in pygame.event.get():   
            if event.type == QUIT :
                pygame.quit()             
                sys.exit()                  
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pass
                elif event.key == K_RIGHT:
                    pass
                elif event.key == K_SPACE:
                    is_game_str = True

        if is_game_str ==False:
            screen_surface.blit(M_GAME_TITLE, (SCREEN_WIDTH/2 - (400/2),SCREEN_HEIGHT/2 - (50/2)))
            screen_surface.blit(M_GAME_SUBTITLE,(SCREEN_WIDTH/2 - (300/2),SCREEN_HEIGHT/2 +50))
        
        else :  # 게임시작 후 블록화면 구현, 볼이 움직이도록, 바도 움직이도록 
            screen_surface.blit(M_CLEAR, (80,280))


        pygame.display.update()            
        FPSCLOCK.tick(30)                   

if __name__ == '__main__' :
    main()
