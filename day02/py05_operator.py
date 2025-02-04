# 연산자

# 사칙연산 : +, -, *, /, //(몫), %
a , b = 15, 14

# 연산자 우선순위
# 계산식이 복잡해서 연산자 우선순위를 잘 모르겠으면 () 사용
# 1순위: 튜플, 리스트, 딕셔너리, 집합
# 2순위: 리스트(튜플) 첨자, 슬라이싱
# 3순위: await 
# 4순위: 거듭제곱 **
# 5순위: 단항덧셈, 단항뺄셈, 비트not
# 6순위: 곱셈, 행렬곱셈, 나눗셈,몫 나눗셈, 나머지
# 7순위: 덧셈, 뺄셈
# 8순위: 비트 시프트
# 9순위: 비트 and
# 10순위: 비트 xor
# 11순위: 비트 or
# 12위: 포함 연산자. 비교 연산자
# 13위: 논리 not
# 14순위: 논리 and
# 15순위: 논리 or
# 16순위: if else
# 17순위: lambda

## 리스트 연산
listSample = [1,3,5,7,9]
print(listSample[0])
print(len(listSample))
print(listSample[len(listSample)-1])
# 리스트 요소 값 삭제 del(listSample[2])
# 리스트 요소 값 추가 listSample.append()

# 문자열 연산 : + , *
greeting = 'Hello'
target = 'World'
print(greeting, target)     #문자열연산 아님
print(greeting + target)    #문자열연산- concatenate

print(greeting + ' '+target)  
print(f'{greeting} {target}')               #string format
print('{0} {1}'.format(greeting, target))   #string format

print(greeting * 3)     #문자열을 *수 만큼 반복

# 문자열(문자 배열)는 List와 유사, 단 값 수정은 안됨!!!!
# 문자열은 + , * , 인덱스추출 가능
print(greeting[1])  #리스트연산


# 리스트 연산 -인덱싱 & 슬라이싱
listSample = ['2','0','2','5','-','0','2','-','0','4']
current = '2025-02-04'
for i in listSample:
    print(i, end='')
print()

print(current)

print(listSample[9])
print(current[9])
print(listSample[-1])
print(current[-1])

#[start :end]  end-1 까지 출력
print(listSample[0:3])  #['2', '0', '2']
print(current[0:3])     #202

print(current[-2:]) #04

# 문자열 연산 중 함수를 사용
full_name = "Hugo MG. Sung"
print(full_name.split())

names =  full_name.split()
print(type(names))
print(names)

names =  full_name.split('.')
print(type(names))
print(names)

# 바꾸기
print(full_name.replace('Hugo MG.','Ashley'))

#공백제거
origin='     Hello  ~     '
print(f'//{origin}//')
print(f'//{origin.lstrip()}//')
print(f'//{origin.rstrip()}//')
print(f'//{origin.strip()}//')

#단어찾기-인덱스를 반환
print(full_name.find('G'))
print(full_name.find('g'))

print(full_name.find('h'))  #-1은 단어 없음을 의미한다. full_name.find('h') 오류발생


print(full_name.count('g'))
print(full_name.index('g'))

print(full_name.upper())
print(full_name.lower())

# T로 자를 때
#'',"" == Empty(비어있다.)
#' ', " " == Space(공백존재)
origin2= 'TESTSTRING'
print(origin2.split('T'))   #['', 'ES', 'S', 'RING']

origin2= 'ESTSTRING'
print(origin2.split('T'))   #['ES', 'S', 'RING']