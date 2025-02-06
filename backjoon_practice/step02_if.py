#1.두수 비교
# a , b = input('두수 입력: ').split(' ')
# a= int(a)
# b = int(b)

# if a>b :
#     print('>')
# elif a<b :
#     print('<')
# elif a ==b :
#     print('==')

# 2. 성적
# score = int(input('성적입력:'))
# if score >=90 :
#     print('A')
# elif score >=80 :
#     print('B')
# elif score >=70 :
#     print('C')
# elif score >=60 :
#     print('D')
# else :
#     print('F')


#3. 윤년  4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# year = int(input('년도를 입력하세요: '))
# if (year%4 ==0 and year%100!=0 ) or (year%400 ==0):
#     print(1)
# else :
#     print(0)

#4. 사분면 고르기
# a = int(input())
# b = int(input())


# if a>0 and b >0 :
#     print('제1사분면')
# elif a >0 and b<0 :
#     print('제4사분면')
# elif a<0 and b>0 :
#     print('제2사분면')
# elif a<0 and b< 0 :
#     print('제3사분면')

# 5 . 45분 일찍 알람 설정하기
#24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다.
# H, M = input('시간입력:').split(' ')
# #고려해야 할 것 
# # 45분미만일 경우, 시간이 -1
# # 0시의 경우, -1되면 23시가 되어야함
# # 0분~60분
# H = int(H)
# M =int (M)

# # 시간>=1, 분>=45
# # 시간=0 , 분>=45
# #시간 >=1 , 분<45
# # 시간=0 ,분<45

# if M >=45 :
#         M = M - 45
# else :
#     M = M - 45 +60
#     if H ==0:
#         H = 23
#     else :
#         H = H -1
# print(H , M)

# 오븐 타이머 설정
# 분의 합이 60이상이면, 시간 +1 그리고 분합 -60
# 분의 합이 60미만이면, 분합
#24시가 될 때, -23
# H, M = input('현재시각 입력:').split(' ')
# plus_time = input('조리시간: ')

# H, M, plus_time =int(H), int(M), int(plus_time)

# if (M+plus_time) >=60 :
#     H = H + ((M+plus_time)//60)
#     M = M+plus_time - 60

#     if (H==24):
#         H=0
#     if (M ==60):
#         M =0
# else :
#      M = M+plus_time
# print(H,M)


# 주사위 세개
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

# a, b, c = input('주사위 세 개의 값: ').split(' ')
# a, b, c = int(a) , int(b), int(c)

# sum = 0
# if a == b and b == c and c == a :
#     sum = 10000 + a * 1000
# elif a == b :
#     sum = 1000 + a *100
# elif  b == c :
#     sum = 1000 + b *100
# elif c == a:
#     sum = 1000 + c* 100
# else :
#     sum = max(a,b,c) *100
# print(sum)

