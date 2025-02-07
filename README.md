# iot_python_2025

## github 데스크톱
- **fetch origin** : 리모트 최신변경사항 확인(중요!) 
- **pull**     : 리모트에 변경사항을 로컬로 내려받기
- **commit & push** : 로컬 변경사항을 확정 및 리모트로 올리기

### 1일차 : 2월 3일
- 1교시
    - 제어판-범주 큰아이콘-사용자계정-자격 증명관리-일반 자격증명 - github계정관련 개인정보 제거
    - 파이썬 기존꺼 제거

- 2교시
    - 글꼴 추가 
        - https://notepad-plus-plus.org/downloads/v8.7.6/         
        - x64 installer
        - 구성요소-사용자정의-korean
- 3교시
    - github,github desktop 설치
- 4교시
    - local - 개인pc  ->commit push  /pull
    - remote -github
    - 파일-기본설정-설정-vscode 테마, 한글, 글자크기 등 설정  
- 오후
    - 컴파일러(exe파일 생성하는 언어) c, c++, c#, java vs 인터프리터(소스코드를 바로 실행) 파이썬, 자바스크립트
    - 파이썬    
        - 1990년에 개발한 인터프리터 언어
        - 네덜란드 개발자 귀도 반 로섬
        - 객체지향 프로그래밍 언어

    - 파이썬 개발환경 Pyenv
        - 파이썬 버전을 손쉽게 변경할 수 있는 툴
        - 설치순서 및 참고자료 : https://pyenv-win.github.io/pyenv-win/
            - powershell 관리자로 실행
            - Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
            - y
            - Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
            - powershell 종료 후 , 재접속해서 pyenv --version해서 pyenv 3.1.1 확인
            - pyenv install --list : pyenv로 설치할 수 있는 파이썬 버전들이 나열됨
            - pyenv install 3.11.9
            - pyenv install 3.9.13
            - pyenv versions :설치된 파이썬 버전 확인
            - pyenv global 3.11.9 : 파이썬 버전 중 사용하고자 하는 버전 선택
            - exit() : 파이썬 빠져나오기

    - visual studio code
        - 확장에서 python 설치
        
### 2일차 : 2월 4일
- 파이썬 기초
    - **주석 처리 : ctrl + /**
    - **한줄 삭제: shift + del**
    - **markdown 미리보기 : ctrl + shift + v**
    - **줄 위치 이동 : alt + 화살표**
    - 변수와 자료형
        - 변수명 규칙
        - 자료형 : none, int, float, str, bool, list, tuple(수정불가), dic, set(중복제거& 순서가 정해져 있지 않다.인덱스가 없다.)
    - 입출력
        - 화면입출력
            - `입력 , 출력 값은 모두 문자열이다.`
            - number = int(input('숫자를 입력하세요: '))   print(type(number)) 
        - 문자열포맷팅
            - %s , %d, %f 
            - '{0} {1}'.format()
            - f'{name} {age}'
    - 연산자
        - 사칙연산 : + ,-,*, //, /, %, **, ()
        - 연산자 우선순위
        - 리스트연산 : 인덱싱, 슬라이싱(`[start :end]  end-1 까지 출력`), 수정
        - 문자열연산 : + , * , 인덱싱, 슬라이싱, split, replace, rstrip, upper, find 
### 3일차 : 2월 5일
- print(값, sep=" " ,  end = "\n") 
    - print("가","나") : 가 나로 출력되는 이유는 sep = " " 때문이다.    
    - print(f'{i} x {j} = {i * j:>2} ', end=' ') 
    - {i * j:>2} {i * j:2d} 
- 흐름제어
    1) 조건문
        1) if 조건1 : 
              실행문1 
           elif 조건2 :
              실행문2
           else : 
    
    2) 반복문
    - `break(반복문 종료), continue(지나침)`
    -  `for문은 자동증가한 반면, while문은 i+=1과 같이 증가시켜줘야 함`
        1) for i in range():
        2)  while 조건: 

    - 조건에 변수가 들어갈 경우, 미리 선언해줘햐 함
    - 합을 구하는 반목문의 경우,  sum=0 미리 선언해줘햐 함
    - 반복문으로 합을 구하고 또 다른 반복문으로 합을 구할 경우, sum=0으로 할지, sum을 이어할지 선택해야 함        
       
- 파일입출력
    - mode : r, w(쓰기), a(추가)
        - 쓰기의 경우, \n이 기본적으로 없기에 연결해서 써짐 
        - 쓰기의 경우, 기존있던 txt에 다시 쓰기할 경우, 기존 내용 대신 새 내용으로 덮여써짐
        - 추가의 경우, 기존있던 내용에 더해짐
    - encoding : 한글만(euc-kr, cp949) , 국제어(utf-8)
    - 파일경로 
        - 절대 C:/Source/iot_python_2025       
        - 상대 .(현재위치)  ..(부모위치)
        - 윈도우 역슬래쉬  C:\\Source\\iot_python_2025 (* 파이썬에서는 \n과 같은 예약어이기에 )
    - open(경로, mode, encoding) ,close() 
    - write() , readline()

- 함수 (매개변수 유무, return값)
    - 함수의 return값이 있을 때, print()함수내에 함수호출
    ``` python 
    def 함수명 (매개변수) :
            로직
    ```

- 객체지향
    - 객체의 틀이 되는 클래스 선언
    - 클래스 : 명사와 동사의 집합
        - 명사 : 멤버변수(속성)
        - 동사 : 멤버함수(메서드)
    ``` python
    class 클래스명 :
        #멤버변수

        def 멤버함수 (self, 매개변수):
            #로직
    ```
### 4일차 : 2월 6일   
- 리스트 연산
    - for, while문에는 반복할 수 있는 요소가 필요(iterable)  (예)range(5) [1,2,3]
    - 자료구조에서는 딕셔너리(키, 값 저장 역할), 리스트(반복문에서 활용)를 주로 사용한다.

    - 연산 : + , * , del(lst),del(lst[0]),  lst.append(), lst.insert(index, value) , len(), sort(reverse=false) , reverse(인덱스를 뒤에꺼부터 시작하는, 값 반전) , index(value) , pop()하면 return은 value이다.
    - `리스트 컴프리핸션  arr = [i for i in range(1,101)]`
- 리스트와 문자열 연산 정리
    - 공통: 인덱싱, 슬라이싱 , + , *   
        - 리스트 :  `데이터수정가능`, append,del,insert,len, sort , pop, index 등                                    
        - 문자열 : replace,upper,lower, strip, find, count , split


- 객체지향
    - object는 모든 클래스의 부모 클래스이다.
    - 클래스 작성방법, 속성, 메서드, 캡슐화(멤버변수 폐쇄화, __멤버변수), **상속** , **추상화**, **인터페이스**, **다형성** ,**SOLID원칙**

    1. 멤버변수
        - ` 멤버변수 이름 앞에 __ 쓰면 외부접근 불가`
    2. 멤버함수
        - get, set 사용자 지정 함수 + 조건문 추가 (예)if type(plateNumber) is str:
        - __str__을 통해 객체의 멤버변수 내용 출력

- 모듈, 패키지 
    1. 모듈 : 함수나 클래스 등 자주 사용할 파이썬 파일로 만든것
        - import 모듈명 , from 모듈명 import 상세

    2. 패키지(라이브러리) : 모듈을 모아둔 폴더
        - `설치가이드 사이트: https://pypi.org/`
        - pip install

    - `if __name__ == '__main__' `
        - __main__ 은 프로그램이 시작하는 진입점(entry point) 지칭
        - c언어 등의 static void main()과 동일한 역할
        - `폴더 안에 py파일 중 실행되는 파이썬 파일이 __main__이 되고 나머지는 모듈이 됨`

### 5일차 : 2월 7일   
- 백준문제 문자열 연산
    - list_a =input().split() 일 때, type(list_a)는 list이다. 
    - list(map(int, input().split()))
    - [0]*10

- 리스트 연산 추가(append, extend)
    ``` python
        x= ['W' ,'Y' , 'Z']
        y= ['A' ,'C' , 'E']
        x.append(y)
        print(x)    #['W', 'Y', 'Z', ['A', 'C', 'E']]

        x= ['W' ,'Y' , 'Z']
        y= ['A' ,'C' , 'E']
        x.extend(y)
        print(x)    #['W', 'Y', 'Z', 'A', 'C', 'E']
    ```
- 스폐셜함수 조회 : print(dir(int))   

- `보기 - 자동줄바꿈 체크`
- `VERSION = 0.1   # 변수를 상수화 : 대문자`
- `for i, v in enumerate(items):`

``` python
# items변수는 list타입이라고 지정
def get_movie(items:list):
    for item in items :
        print(item) 
 ```
- 예외처리
    1) 문법적 오류 - error 
        - 코드 작성 시 빨간 밑줄 뜸, 콘솔창에 오류 뜨지 않음
        - 오류표시가 안 나는 코딩을 잘못한 오류 포함 (예)mul(7,6) -> 42 예상 , 그러나 결과가 13인 경우 
    
    2)  예외  - exception 
        - 실행 중 발생하여 프로그램을 비정상 종료시키는 것
        - 콘솔창에 오류 뜸
        - 예외처리 안에 또 예외처리 넣으면 속도 느려짐이 심해지니 지양
        
    ``` python
        try :
        except Exception as e:
        finally :
    ```
       

- 디버깅 : 왼쪽의 실행 및 디버그 탭
    -   시작 f5
    -   중단점 f9
    -   한줄실행 -f10
    -   함수 내부로 들어가면서 한줄 실행 f11
    -   종료 shift f5
    -   변수탭
    -   조사식탭

### 5일차 : 2월 7일   토이프로젝트 (콘솔앱 : 내 영화 앱)
- 예외처리
    -  메뉴 입력 sel_menu = int(input('메뉴 번호입력:'))
        - ㅂ일 경우, ValueError => try: except :sel_menu = 0 로 예외처리

    - 영화정보 입력  title, release, sponsor, rate = input('영화입력[영화제목|개봉일| 배급사|평점 순]: ').split('|')
        - input은 문자열이기에 개봉일, 평점을 int, float으로 행변환해야 나중에 연산할 수 있다.
        - 입력한 개수가 4개가 아닐경우, try except로 예외처리
        - 입력 순서가 title, release, sponsor, rate순서여야 정해둔 행변환 실행오류 없다.

- 보통 삭제할 때, id를 삭제한다. 지금은 id없으니 이름으로 삭제한다.

- 파일쓰기, 읽기
    - f.write(f'{}')
    - f.readline().replace().split()
    - `파일에서 읽을 때 숫자나 실수는 문자열이기에 int(), float()해줘야함`

### 6일차 : 2월 10일 
- 파이썬 응용
    - 토이프로젝트
        - 내 영화 앱 수정, 마무리
        - 챗gpt 윈도우앱(tkinter) 만들기

    - 주피터 노트북 학습

    - PyQt학습

    - 토이프로젝트
        - 윈도우앱(PyQt)