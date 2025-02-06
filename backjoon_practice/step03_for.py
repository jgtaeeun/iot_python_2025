import sys
# 구구단
# num=int(input('단 입력: '))

# for i in range(1,10):
#     print(f'{num} * {i} = {num * i}')

# 두 정수 a,b를 입력받아 합 출력
# rep = int (input('반복횟수: '))
# result = []
# sum = 0
# for i in range(rep) :
#     a,b = input().split(' ')
#     sum = int(a) + int(b)
#     result.append(sum)
# for i in result:
#     print(i)

# 1부터 n까지의 합
# num = int(input())
# sum = 0
# for i in range (1, num+1):
#     sum += i
# print(sum)

# 영수증
# total_fee = int(input('영수증에 적힌 총 금액: '))
# merchandise_count =int(input('구매한 물건의 총 개수: '))
# sum = 0
# for i in range(merchandise_count):
#     a, b = map(int ,input('해당 구매 물건의 종류 및 가격: ').split(' '))
#     sum = a * b
#     total_fee = total_fee - sum
# if total_fee == 0 :
#     print('yes')
# else :
#     print('no')

# 등비수열
# N = int(input())
# # 4바이트 long
# # 8바이트 long long
# long_count =0
# for i in range(1, N+1, 4):
#     long_count += 1
# print ('long '* long_count +'int')

# sys.stdin.readline
# T = int(input())
# for i in range(T):
#     a,b = map(int ,sys.stdin.readline().split(' '))
#     print(f'Case #{i+1} : {a} + {b} = {a+b}')

# 별찍기
# num = int(input())
# for i in range(1,num+1):
#     print('*' * i)

# 별찍기(우측정렬)
# num = int(input())
# for i in range(1,num+1):
#      print(' ' * (num-i) +'*' * i)


# while True :
#     a, b = map(int, input().split())
#     if a == 0 and b == 0 :
#         break
#     else :
#         print (a +b)

while True :
    try :
        a, b = map(int, input().split())
        print (a +b)
    except Exception as e:
        print(e)
        break