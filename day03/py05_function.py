# 함수 , 메서드, functionn, procedure ...
# 인자, 파라미터, 매개변수 , argument ...

# def 함수명(인자,...):
#   함수안으로 진입

def say_hi():
    print('안녕~')
    return None


def say_hello(name):
    print(f'{name}야, 안녕!!!')
    return None


def get_age (birthYear):
    age = 2025 - birthYear
    return age

def closing():
    return '바이바이'
    
# print('인사하기:' , end=' ')
# say_hi()

# name = input('이름입력 > ')
# print('이름으로 인사하기:' , end= ' ')
# say_hello(name)

# birthYear = int (input('생년을 입력하세요> '))
# print(f'나이는 {get_age(birthYear)}살입니다.')

#print('작별인사:' + closing())


# 매개변수 개수가 일정하지 않은 경우
# def adds(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
# print(adds(1,2,3,4))

# 계산기
# def calc (option='add' , *args):
#     result = 0
#     if option == 'sub':
#         result = args[0]
#         num = 0
        
#         for i in args:
#             num +=1
#             if num == 1 : continue
#             result -= i
       
#     elif option == 'div' :
#         result = args[0]
#         num = 0
#         for i in args:
#             num +=1
#             if num == 1 : continue
#             result /= i
    
#     return result
# print(calc('sub' , 10,3,2))
# print(calc('div', 13,5))

# 함수결과가 하나이상인 경우
def mul_and_div(x, y):
    return (x*y , x/y)
(mul_result, div_result) = mul_and_div(10,5)
print(mul_result)
print(div_result)

a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)

a = 1
def vartest2():
    global a 
    a += 1
vartest2()
print(a)