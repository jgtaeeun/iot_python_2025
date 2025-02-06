# 예외처리
# 오류, 에러

# 1. 문법적 오류 - error 
#    코드 작성 시 빨간 밑줄 뜸, 콘솔창에 오류 뜨지 않음
#    오류표시가 안 나는 코딩을 잘못한 오류 포함 >mul(7,6) -> 42 예상 , 그러나 결과가 13인 경우 
# 2. 실행 중 발생 예외  -exception / 콘솔창에 오류 뜸

numbers = list(range(1,11))
for i in numbers:
   pass

def mul(a, b):
    return a*b
def div(a, b):
    return a/b


print('계산시작')
while True:
    op = input('계산할 연산을 입력(*,/,q):')
    if op == 'q' :
        break
    elif op == '*' :
        x, y= input('곱할 수 입력: ').split()
        x , y = int(x), int(y)
        print(f'{x} * {y} = {mul(x, y)}')
    elif op == '/' :
        x, y= input('나눌 수 입력: ').split()
        x , y = int(x), int(y)
        print(f'{x} / {y} = {div(x,y)}')
    else :
        print('정확한 입력 요망')
        




