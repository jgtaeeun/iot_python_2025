import pygame   
from pygame.locals import QUIT , KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, Rect
import sys      

import random
import math


pygame.init()
screen_surface = pygame.display.set_mode(size=(600,400))
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
    
    while True:
        screen_surface.fill(color= '#ffbaca')  
        for event in pygame.event.get():   
            if event.type == QUIT :
                pygame.quit()             
                sys.exit()                  
        pygame.display.update()            
        FPSCLOCK.tick(30)                   

if __name__ == '__main__' :
    main()
