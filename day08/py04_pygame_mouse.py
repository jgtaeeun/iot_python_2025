import pygame   
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
import sys      

pygame.init()
screen_surface = pygame.display.set_mode(size=(600,400))
pygame.display.set_icon(pygame.image.load('./day08/apink.png'))
FPSCLOCK= pygame.time.Clock()
pygame.display.set_caption('MyMy Pygame_MouseEvent')

def main():
    pos = []
    check = mousebutton =False

    while True:
        screen_surface.fill(color= '#ffbaca')  
        for event in pygame.event.get():   
            if event.type == QUIT :
                pygame.quit()             
                sys.exit()   
            elif event.type == MOUSEBUTTONDOWN:   
                # pos.append(event.pos)
                check =True
                mousebutton = True
            elif event.type == MOUSEMOTION :
                if mousebutton :
                    pos.append(event.pos)
            elif event.type == MOUSEBUTTONUP :
                    check =False
                    mousebutton = False
                    pos.clear()
        if check :
            if len(pos) >1:
                pygame.draw.lines(screen_surface, 'white',False, pos)
        # for mpos in pos:
        #     pygame.draw.circle(screen_surface, 'white', mpos, 5)

        pygame.display.update()            
        FPSCLOCK.tick(30)                   

if __name__ == '__main__' :
    main()
