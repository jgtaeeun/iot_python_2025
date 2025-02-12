import pygame   
from pygame.locals import QUIT , KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, Rect
import sys      

import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# 1. 클래스(볼, 벽돌 만들기)

class Block():
    def __init__(self, color, rect, speed=0):
        self.color= color
        self.rect = rect
        self.speed =speed
        self.direction = random.randint(-45,45) + 270   #direction 값 범위 : 225~315 

    def move(self): # 공 움직임
        self.rect.centerx += math.cos(math.radians(self.direction)) * self.speed    # 공이 움직이는 x축 값
        self.rect.centery -= math.sin(math.radians(self.direction)) * self.speed    # 공이 움직이는 y축 값

    # 공 그리기
    def draw_E(self):   # 공을 circle이 아니라 ellipse로 생성
        pygame.draw.ellipse(screen_surface, self.color, self.rect )
    
    # 벽돌 그리기
    def draw_R(self):
        pygame.draw.rect(screen_surface, self.color, self.rect )


pygame.init()
screen_surface = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT ))
pygame.display.set_icon(pygame.image.load('./day08/block.png'))
FPSCLOCK= pygame.time.Clock()
pygame.display.set_caption('Blocks Pygame')
pygame.key.set_repeat(10,10)


def main():
    is_game_str = False
    score = 0
    BLOCK = []

    # 3. 공 생성
    BALL = Block((200,200,0), Rect(375,650,20,20), 10)


    # 벽돌 색 (무지개색)
    colors = [(255,0,0),(255,150,0),(255,228,0),(11,201,4),(0,80,255),(0,0,147),(201,0 ,167)]
    
    # 2. 게임 첫 화면에서 생성되어 있는 벽돌(7가지 색 * 9개 =63개)
    for y, color in enumerate(colors):
        for x in range(0,9):
            BLOCK.append(Block(color, Rect(x*80+150,y*40+40, 60,20)))

    bigFont = pygame.font.SysFont('NanumGothic',80)
    smallFont = pygame.font.SysFont('NanumGothic',45)

    M_GAME_TITLE = bigFont.render('GAME START?' , True, 'white')
    M_GAME_SUBTITLE = smallFont.render('PRESS SPACE_BAR' , True, 'white')
    M_CLEAR = bigFont.render('CLEAR!' , True, 'green')
    M_FAIL = bigFont.render('FAILED!' , True, 'red')

    while True:
        # 스코어, 스피드 글자
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
        
        else :  # 3. 게임시작 후 블록화면 구현, 볼이 움직이도록, 바도 움직이도록 

            LenBlock = len(BLOCK) 


            if BALL.rect.centery <800:
               BALL.move()
            if BALL.rect.centerx <0 or BALL.rect.centerx > 1000 :
                BALL.direction = 180 -BALL.direction
            elif BALL.rect.centery <0 :
                BALL.direction = -BALL.direction
            
            BALL.draw_E()

            for i in BLOCK :
                i.draw_R()

        pygame.display.update()            
        FPSCLOCK.tick(30)                   

if __name__ == '__main__' :
    main()
