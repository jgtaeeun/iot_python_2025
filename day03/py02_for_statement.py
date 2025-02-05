# for문
# for 변수 in 반복할 값:

# for i in range(1,5):
#     print( '*' * i)

# num = int (input('반복횟수> '))
# for i in range(1, num+1):
#     print( '*' * i)

#구구단(2~9단)
# 1)  break 사용해서 2~7단
# for i in range(2, 10):
#     if i == 8 : break
#     print(f'{i}단 시작')
#     for j in range(1, 10):
#         print(f'{i} x {j} = {i * j:2d} ', end='  ')
#     print()

#2)  break 사용해서 i*7 까지
# for i in range(2, 10):
#     print(f'{i}단 시작')
#     for j in range(1, 10):
#         if j == 8 : break
#         print(f'{i} x {j} = {i * j:2d} ', end='  ')
#     print()


#3)  continue 사용해서 8단제외
# for i in range(2, 10):
#     if i == 8 : continue
#     print(f'{i}단 시작')
#     for j in range(1, 10):
#         print(f'{i} x {j} = {i * j:2d} ', end='  ')
#     print()
# print(값, sep=" " ,  end = "\n") print("가","나")  가 나로 출력되는 이유는 sep = " " 때문이다.

# 반복문 빠져나올 때 : break
# 반복문에서 특정 조건을 지나칠 때 : continue