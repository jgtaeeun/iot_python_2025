import pygame   # pygame 모듈 추가
from pygame.locals import QUIT # 종료 처리 변수
import sys      # 운영체제 시스템 명령
#>>> import sys
#>>> sys.executable
#'C:\\Users\\Admin\\.pyenv\\pyenv-win\\versions\\3.11.9\\python.exe'

# 기본변수
pygame.init()
screen_surface = pygame.display.set_mode(size=(600,400))
# print(type(screen_surface),screen_surface.get_rect())  
pygame.display.set_icon(pygame.image.load('./day08/apink.png'))
FPSCLOCK= pygame.time.Clock()
pygame.display.set_caption('MyMy Pygame')

def main():
    while True:
        screen_surface.fill((255,186,202))  # FFFFFF =white , #00000000 /#00FFFFFF 제일앞00은 alpha값,투명도이다. 
        for event in pygame.event.get():    # 키보드 ,마우스 이벤트 체크
            if event.type == QUIT :
                pygame.quit()               # pygame 종료
                sys.exit()                  # 윈도우 앱 탈출
        pygame.display.update()             # 지금까지 작성 코드를 윈도우 창에 표시!
        FPSCLOCK.tick(30)                   #30FPS 지정

if __name__ == '__main__' :
    main()
