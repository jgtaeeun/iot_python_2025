# 복합자료형
# 자료구조 및 알고리즘

# 리스트 이전
a = 1
b = 2
c = 3
d = 4
e = 5

sum =  a + b + c + d + e
print(sum)

## 리스트(배열) 사용 []
#  다른언어에선 리스트와 배열은 다른 것
f = [1,2,3,4,5]
print(f)
print(type(f))

sum = 0
for i in f :
    sum += i 
print(sum)

f = ['Life', 'is', True, 0, None , [1,2,3]]
print(f)
print(f[0])

# 리스트의 한 요소에도 값을 집어넣을 수 있음
f[3] = 100
print(f)

## 튜플 ()
#  리스트와 거의 흡사, 값을 변경할 수 없음
t = (1,2,3,4)
print(t)
print(type(t))

## 딕셔너리 {}
spiderman = { 'name' : 'Peter Parker' , 'age' : 20 , 'weapon' : 'Web Shooter'}
print(spiderman)
print(type(spiderman))
print(spiderman['name'])
spiderman['age'] = 21
print(spiderman)

## 집합 -set 키워드, 
# set ((),{},[] 다 가능 )
# 중복 제거 , 순서가 정해져 있지 않다.(인덱스가 없다.)
s = set([1,2,3])
print(s)
s = set({1,2,3})
print(s)
s = set((1,2,3))
print(s)

s = set((1,3,5,7,9,5))
print(s)
print(type(s))

s = set('Hello Word!')  # 공백도 포함, 순서정해져있지 않다.
print(s)


## 변수명 지정 방식
# 의미있는 단어들의 조합으로 만들 것 (예)  phoneNumber ='010 0000 0000'

samsung=''
samsung1=''
# 1sumsung='' # 숫자로 시작할 수 없다.
_samsung ='' # 언더바로 시작할 수 있다.
samsung_ = ''
# samsung!='' # 언더바 외에 특수문자 불가능하다.
# samsung-apple ='' #파이썬 연산자는 사용불가