# 함수로 기능 묶기
import pygame   
from pygame.locals import QUIT , KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, Rect
import sys      

import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800



class Block():
    def __init__(self, color, rect, speed=0):
        self.color= color
        self.rect = rect
        self.speed =speed
        self.direction = random.randint(-45,45) + 90 

    def move(self):
        self.rect.centerx += math.cos(math.radians(self.direction)) * self.speed    
        self.rect.centery -= math.sin(math.radians(self.direction)) * self.speed    

 
    def draw_E(self):   
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

def make_block():
    BLOCK = []

    colors = [(255,0,0),(255,150,0),(255,228,0),(11,201,4),(0,80,255),(0,0,147),(201,0 ,167)]
    
    
    for y, color in enumerate(colors):
        for x in range(0,9):
            BLOCK.append(Block(color, Rect(x*80+150,y*40+40, 60,20)))
    
    return BLOCK

def make_ball():
    BALL = Block('white', Rect(375,650,20,20), 10)
    return BALL

def make_PADDLE():
    PADDLE =Block('yellow', Rect(375,700,100,30))
    return PADDLE

def main():
    
    bigFont = pygame.font.SysFont('NanumGothic',80)
    smallFont = pygame.font.SysFont('NanumGothic',45)

    M_GAME_TITLE = bigFont.render('GAME START?' , True, 'white')
    M_GAME_SUBTITLE = smallFont.render('PRESS SPACE_BAR' , True, 'white')
    M_CLEAR = bigFont.render('CLEAR! ' , True, 'green')
    M_FAIL = bigFont.render('FAILED!' , True, 'red')
    
    is_game_start = False
    score = 0
    PADDLE =make_PADDLE()
    BLOCK = make_block()
    BALL = make_ball()

    while True:
        M_SCORE = smallFont.render(f'score:{score}', True, 'white')
        M_SPEED = smallFont.render(f'speed:{BALL.speed}', True, 'white')

        screen_surface.fill(color= 'black')  
        for event in pygame.event.get():   
            if event.type == QUIT :
                pygame.quit()             
                sys.exit()                  
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if PADDLE.rect.centerx <50 :
                        PADDLE.rect.centerx =50
                    else :
                        PADDLE.rect.centerx -= 10
                elif event.key == K_RIGHT:
                    if PADDLE.rect.centerx >(SCREEN_WIDTH-50) :
                        PADDLE.rect.centerx =(SCREEN_WIDTH-50)
                    else :
                        PADDLE.rect.centerx += 10
                elif event.key == K_SPACE:
                    is_game_start = True

        if is_game_start ==False:
            screen_surface.blit(M_GAME_TITLE, (SCREEN_WIDTH/2 - (400/2),SCREEN_HEIGHT/2 - (50/2)))
            screen_surface.blit(M_GAME_SUBTITLE,(SCREEN_WIDTH/2 - (300/2),SCREEN_HEIGHT/2 +50))
        
        else : 
            screen_surface.blit(M_SCORE, (10,770))
            screen_surface.blit(M_SPEED, (SCREEN_WIDTH-220,770))
            
            LenBlock = len(BLOCK) 

           
            BLOCK = [x for x in BLOCK if not x.rect.colliderect(BALL.rect)]
            if len(BLOCK) != LenBlock : 
                BALL.speed += 0.25
                BALL.direction = -BALL.direction
                score += 10
            
            if BALL.rect.centery <SCREEN_HEIGHT +BALL.rect.height / 2  :
                   BALL.move()

            if PADDLE.rect.colliderect(BALL.rect) : 
                BALL.speed += 0.25
                BALL.direction =90+ (PADDLE.rect.centerx - BALL.rect.centerx)/ PADDLE.rect.width * 100

            if BALL.rect.centerx <10 or BALL.rect.centerx > (SCREEN_WIDTH-10) :
                BALL.direction = 180 -BALL.direction
            elif BALL.rect.centery <10 :
                BALL.direction = -BALL.direction
            
            if len(BLOCK) == 0 :
                screen_surface.blit(M_CLEAR,( (SCREEN_WIDTH/2)-(240/2), (SCREEN_HEIGHT/2)-(50/2)))
                is_game_start=False
                previous_speed=BALL.speed
                BALL = make_ball()
                BALL.speed = previous_speed
                PADDLE =make_PADDLE()
                BLOCK = make_block()

            if BALL.rect.centery >= SCREEN_HEIGHT +BALL.rect.height / 2  :
                screen_surface.blit(M_FAIL,( (SCREEN_WIDTH/2)-(240/2), (SCREEN_HEIGHT/2)-(50/2)))
                is_game_start=False
                previous_speed=BALL.speed
                BALL = make_ball()
                BALL.speed = previous_speed
                PADDLE =make_PADDLE()

            BALL.draw_E()
            PADDLE.draw_R()
            for i in BLOCK :
                i.draw_R()

        pygame.display.update()            
        FPSCLOCK.tick(30)                   

if __name__ == '__main__' :
    main()
