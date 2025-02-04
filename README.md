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
    - 흐름제어
    - 파일입출력
    - 함수
    - 객체지향
    - 모듈, 패키지
    - 예외처리
    - 디버깅