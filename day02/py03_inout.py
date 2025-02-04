# 화면 입출력

print('출력입니다.')

# 입력
number = input('숫자를 입력하세요: ')
print(type(number))

# 입력 , 출력 값은 모두 문자열이다.
# <class 'int', 'str', 'float' >
number = int(input('숫자를 입력하세요: '))
print(type(number))
print('입력된 숫자는' , number + 1 , '입니다')  #여러 값을 같이 출력하려면, 쉼표로 구분

# 다중입력
x , y = input('합산할 두 수를 입력하세요: ').split()    #공백으로 자름
x = int(x)
y = int(y)
print(x + y)


