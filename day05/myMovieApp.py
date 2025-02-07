import os       #운영체제 모듈
from Movie import Movie

VERSION = 0.1   # 변수를 상수화 : 대문자

# 메인에서 제일처음 실행되는 함수

# 콘솔화면 클리어 함수
def clear_console():
    command = 'clear'               #리눅스, 유닉스 클리어 명령어
    if os.name in ('nt', 'dos'):    #운영체제가 윈도우라면
        command = 'cls'             #윈도우 클리어 명령어
    os.system(command)              #콘솔에 명령어 실행


def run():
    lst_movie=[]
    load_File(lst_movie)
    clear_console()

    while True :
        sel_menu = set_menu()
        
        if sel_menu==1 :
            # print('영화입력')
            movie = set_movie()
            if type(movie) != Movie:
                print('입력순서와 입력개수를 지켜주세요')
            else :
                lst_movie.append(movie)
                print()
            

        elif sel_menu== 2 :
            print('---전체 리스트---')
            get_movie( lst_movie)
            print()

        elif sel_menu == 3 :
            search_keyword = input('검색할 영화명: ')
            print('---필터링 결과---')
            search_movie( lst_movie, search_keyword)
            print()
            
        elif sel_menu== 4 :
            delete_movie_name = input('삭제할 영화명: ')
            print('---삭제 결과---')
            delete_movie( lst_movie,delete_movie_name )
            print()
            


        elif sel_menu == 5 :
            # print('앱종료')
            save_File(lst_movie)
            break
        else :
            pass

        input()             #입력대기
        clear_console()

def set_movie():
    try :
        # (title, release, sponsor, rate) = input('영화입력[영화제목|개봉일| 배급사|평점 순]: ').split('|')
        title, release, sponsor, rate = input('영화입력[영화제목|개봉일| 배급사|평점 순]: ').split('|') #입력 개수 오류
        movie = Movie(title=title,release= int(release), sponsor=sponsor, rate=float(rate))   #input은 다 문자열이기에 연산을 위한 행변환이 필요-데이터형 오류
        return movie
    
    except Exception as e:   #입력개수, 형변환을 위한 입력순서
        return e

    
    

# items변수는 list타입이라고 지정
def get_movie(items:list):
    for item in items :
        print(item)     #Movie클래스 객체
        print()

# 필터조회(검색기능)
def search_movie(items:list, search_keyword:str):
    status = False
    for i in items:
        if i.isNameContain(search_keyword) :
            print(i)
            status = True
    if status == False :
        print('검색된 결과가 없습니다.')
        
# 삭제
# 보통 삭제할 때, id를 삭제한다. 지금은 id없으니 이름으로 삭제한다.

def delete_movie(items:list, search_keyword:str):
    status = False
    for i, v in enumerate(items):
        if v.isNameSame(search_keyword) :
            del(items[i])
            status = True
            print(f'영화 [{v.getTitle()}]이(가) 삭제되었습니다.')
    if status == False :
        print('존재하지 않는 값은 삭제할 수 없습니다.')


def set_menu():
    str_menu = (f'내 영화 앱 v{VERSION}\n'
                  '1. 영화 입력 \n'
                  '2. 영화 출력 \n'
                  '3. 영화 검색 \n'
                  '4. 영화 삭제 \n'
                  '5. 앱 종료 \n'
                )
    print(str_menu)
    
    try :
        sel_menu = int(input('메뉴 번호입력:')) #ㅂ일 경우, ValueError
    except Exception as e:
        sel_menu = 0

    return sel_menu

# 파일 저장
def save_File (items :list):
    f = open('./day05/movieDB.txt' , mode='w' , encoding='utf-8')
    for i in items :
        f.write(f'{i.getTitle()}|')
        f.write(f'{i.getRelease()}|')
        f.write(f'{i.getSponsor()}|')
        f.write(f'{i.getRate()}\n')
    f.close()

# 파일 불러오기
def load_File(items:list):
    f = open('./day05/movieDB.txt' , mode='r' , encoding='utf-8')
    while True:
        line =  f.readline()
        if not line :
            break
        # \n으로 indexarray 오류발생. \n을 리스트 저장전에 삭제해야함
        lines = line.replace('\n','').split('|')     #lines는 4개의 문자열을 가지는 리스트
        movie = Movie(title = lines[0],release=  int(lines[1]), sponsor= lines[2], rate=float(lines[3]))
        items.append(movie)
    f.close()




if __name__ == '__main__' :
    # print('내 영화 앱 시작')
    run()

print('프로그램 종료')