# 변수와 자료형

# 변수
a = None            # 특수형,  None타입
print(a)
print(type(a))

a = 19              # 정수형, Integer
print(a)            # 함수는 늘 괄호를 같이 사용
print(type(a))

a = 12.34           # 실수형, Float
print(a)
print(type(a))

a = 0b11111110      # 2진수 , Binary
print(a)
print(type(a))

a = 0xFE            # 16진수(0~9 , A, B, C, D, E, F[15]) , Hex
print(a)
print(type(a))

a = 1_900_000_000   # 천단위마다 쉼표와 같이 표현 
print(a)
print(type(a))

a = "Life is short, You need Python"    # 문자열 , String
print(a)
print(type(a))

a = 'Life is short, You need Python'    # 문자열
print(a)
print(type(a))

a = (3 > 1)         # True | False, boolean 
print(a)
print(type(a))