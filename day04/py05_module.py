# 외부 모듈
# 내 컴퓨터에 없는 모듈을 가져와서 사용하려면 
# pip - python이 제공하는 package installer of python

# pip --version
# pip list
# pip install requests
# C:\Users\Admin\.pyenv\pyenv-win\versions\3.11.9\Lib\site-packages에서 urllib3, idna, charset-normalizer, certifi, requests 설치 된 것 확인할 수 있다.

import requests
# print('외부 패키지 사용')

#웹 브라우저가 아닌 파이썬상에서 웹사이트 접속
# res = requests.get('https://www.google.com')
# print(res.status_code)
# print(res.content)

# f = open('./day04/index.html', mode = 'w' , encoding= 'utf-8')
# f.write(str(res.content, 'utf-8'))
# print('생성완료')
# f.close()


class Sample :
    pass


import py02_car as c
# __main__ 은 프로그램이 시작하는 진입점(entry point) 지칭
# c언어 등의 static void main()과 동일한 역할
# 폴더 안에 py파일 중 실행되는 파이썬 파일이 __main__이 되고 나머지는 모듈이 됨
if __name__ == '__main__':
    sam = Sample()
    print(sam)      # <__main__.Sample object at 0x00000185783975D0>
    
    
    car = c.Car()
    print(car)       # <py02_car.Car object at 0x000002A2740C7E10>
    