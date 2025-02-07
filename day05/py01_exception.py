# 예외처리
# 오류, 에러

# 1. 문법적 오류 - error 
#    코드 작성 시 빨간 밑줄 뜸, 콘솔창에 오류 뜨지 않음
#    오류표시가 안 나는 코딩을 잘못한 오류 포함 >mul(7,6) -> 42 예상 , 그러나 결과가 13인 경우 
# 2. 실행 중 발생 예외  -exception / 콘솔창에 오류 뜸
#   Exception 클래스는 다른 모든 예외 클래스의 조상
#   try:
#       예외가 발생할 수 있는 로직
#   except 예외클래스 as e:
#       예외처리로직
#   finally :   
#       예외발생유무와 상관없이 항상 처리해야 할 로직


# 디버깅- 예외(오류)가 어디에서 발생하는지 확인하기 위해 사용
# F9 : 중단점(breakpoint) 표시 및 해제
# F5 : 디버깅 시작 , 중단점까지 실행
# F10 : 한줄 실행, 함수가 있어도 함수를 실행하고 넘어감
# F11 : 한줄 실행, 함수가 있으면 내부구조 안으로 진입
# Shift + F5 : 종료
# 변수 탭 : 현재 변수에 들어있는 값 표시
# 조사식 탭 : 내가 원하는 식을 실행하면 결과 표시

numbers = list(range(1,11))
for i in numbers:
   pass

def mul(a, b):
    return a*b
def div(a, b):
    return a/b

# 입력이 공백으로 분리되어 입력되지 않는 경우 - ValueError
# 0으로 나누는 경우 - ZeroDivisionError
print('계산시작')
while True:
    op = input('계산할 연산을 입력(*,/,q):')
    if op == 'q' :
        break
    elif op == '*' :
        try :
            x, y= input('곱할 수 입력: ').split()   
            x , y = int(x), int(y)

            print(f'{x} * {y} = {mul(x, y)}')
        except ValueError as e :
            print(f'입력실수 {e} ')
        
    elif op == '/' :
        try :
            x, y= input('나눌 수 입력: ').split()
            x , y = int(x), int(y)

            print(f'{x} / {y} = {div(x,y)}')
        # except ValueError as e :
        #     print(f'입력실수 {e} ')
        # except ZeroDivisionError as e :
        #     print(f'0으로 나눌 수 없어 {e} ')
        except Exception as e :
            print(e)
    else :
        print('정확한 입력 요망')





