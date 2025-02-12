import pygame   
from pygame.locals import QUIT
from pygame.draw import *
import  pygame.image as img
import sys      
import os
pygame.init()
screen_surface = pygame.display.set_mode(size=(640,400))
pygame.display.set_icon(pygame.image.load('./day08/apink.png'))
FPSCLOCK= pygame.time.Clock()
pygame.display.set_caption('MyMy Pygame')


def main():
    #  이미지 로드
    yesyes = img.load('./day08/yesyes.png')
    
    # 텍스트 변수
    font=pygame.font.SysFont('NanumGothic', 50)
    message1 = font.render('Apink',True, 'black')
    message2 = font.render('Panda',False, 'black')

    while True:
        screen_surface.fill(color= '#ffbaca')  
        for event in pygame.event.get():   
            if event.type == QUIT :
                pygame.quit()             
                sys.exit()      
        # 화면 표현
        # 선
        pygame.draw.line(screen_surface, color='white', start_pos=(200,50), end_pos=(400,50), width=3) 
        line(screen_surface, color='white', start_pos=(200,350), end_pos=(400,350), width=3) 
        for i in range(200, 401, 10):
            line(screen_surface, 'white', (i, 50), (i,350))
        line(screen_surface, 'gray', (260, 270), (340,130) , width=5)
     
        for i in range(20):
            line(screen_surface, 'white', (200+10*i, 50), (400,350-15*i) )
            line(screen_surface, 'white', (200, 50+15*i), (400-10*i,350) )


        # 사각형
        rect(screen_surface, 'gray' , (150,370,20,20)) 
        rect(screen_surface, 'gray' , (450,370,20,20),4)
        rect(screen_surface, 'gray' , (150,30,20,20),4) 
        rect(screen_surface, 'gray' , (450,30,20,20))

        # 원
        circle(screen_surface, 'gray', (350,250), 20 ,4 ) 
        circle(screen_surface, 'gray', (250,150), 20 ,4) 

        # 타원
        ellipse(screen_surface, 'gray', (30,30,20,50),3)
        line(screen_surface, 'gray', (80, 20), (40,110) , width=3)
        ellipse(screen_surface, 'gray', (70,70,20,50),3)
        
        # polygon 다각형(별)
        pos = [(550,0),(540,20),(500,30),(530,70),(520,90),(550,70),(580,90),(570,50),]
        # polygon(screen_surface, 'white',pos,3)
        # 이미지 flaticon.com
        screen_surface.blit(yesyes, (420, 150))  # 이미지 위치 변경
        screen_surface.blit(yesyes, (280, 370),(90,50,40,10))  # 이미지 위치 변경

        # 메시지
        screen_surface.blit(message1, (10,200))
        screen_surface.blit(message2, (10,300))

        pygame.display.update()            
        FPSCLOCK.tick(30)                   

        
if __name__ == '__main__' :
    main()
