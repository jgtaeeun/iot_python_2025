import pygame   
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN,K_UP
import sys      

pygame.init()
screen_surface = pygame.display.set_mode(size=(600,400))
pygame.display.set_icon(pygame.image.load('./day08/apink.png'))
FPSCLOCK= pygame.time.Clock()
pygame.display.set_caption('MyMy Pygame_Event')
pygame.key.set_repeat(10,10)    # 키보드 연속 움직임 풀링

def main():
    xpos = 50
    ypos = 50
    while True:
        screen_surface.fill(color= '#ffbaca')  
        for event in pygame.event.get():   
            if event.type == QUIT :
                pygame.quit()             
                sys.exit()                  
            elif event.type == KEYDOWN : # 키보드 입력 시작
                if event.key == K_LEFT : 
                    if xpos <= 20 :
                       xpos =20
                    else :
                        xpos -= 10
                if event.key == K_RIGHT :
                    if xpos >=580 :
                       xpos =580
                    else :
                        xpos += 10

                if event.key == K_UP :
                    if  ypos <= 20 :
                        ypos =20
                    else :
                         ypos  -= 10
                if event.key == K_DOWN :
                    if  ypos >= 380 :
                        ypos =380
                    else :
                         ypos  += 10
        
        pygame.draw.circle(screen_surface, 'white', (xpos, ypos) , 20)
        pygame.display.update()            
        FPSCLOCK.tick(30)                   


if __name__ == '__main__' :
    main()
