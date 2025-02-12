import pygame   
from pygame.locals import QUIT
import sys      

pygame.init()
screen_surface = pygame.display.set_mode(size=(600,400))
pygame.display.set_icon(pygame.image.load('./day08/apink.png'))
FPSCLOCK= pygame.time.Clock()
pygame.display.set_caption('MyMy Pygame')

def main():
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
