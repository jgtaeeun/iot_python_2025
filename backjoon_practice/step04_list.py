# 개수세기 : .count()
 
# N  = int(input())
# list_a =input().split()
# v = int(input())
# if len(list_a) != N:
#     print(f'정수입력 개수가 {N}이 아닙니다.')
# else :
#     count = 0
#     for i in range(len(list_a)):
#         if int(list_a[i]) == v :
#             count += 1
#     print(count)

# N = int(input())
# a = list(map(int, input().split()))
# v = int(input())
# if len(a)== N :
#     print(a.count(v))
# else :
#     print('입력개수 확인 요망')

# 2단계
# N, X = map (int, input().split())
# A = list(map(int,input().split()))
# if len(A) == N :
#     for i in range(N) :
#         if A[i] < X :
#             print(A[i] , end=' ')        
# else :
#     print('수열 요소 개수 확인 요망')

#3단계: 최대값, 최소값 max(),min()
# N = int(input())
# a = list(map(int, input().split()))
# if len(a) == N :
#     print(min(a),max(a))
# else :
#     print(f'정수 개수가 첫째줄의 정수개수{N}과 일치하지 않음')

# 4단계 : index(), max()
# 중복의 경우, 인덱스 작은 것이 우선시 되어 출력 된다.
# n = []
# limit_condition = True
# for i in range(9):
#     a = int(input())
#     if a < 100 :
#         n.append(a)
#     else :
#         limit_condition = False
#         break

# if limit_condition == True:
#     print(max(n))
#     print(n.index(max(n))+1)    #1번째 입력부터 시작이므로 인덱스+1로
# else :
#     print('자연수는 100보다 작아야 함')

# 바구니에 공 넣기
# box = [0] * n 

# N , M = map (int, input().split())
# box = [0 for _ in range(N)]
# for _ in range(M):
#     i, j, k =  map(int,input().split())
    
#     for o in range(i, j+1) :
#         box[o-1] = k 

# for i in range(N):
#     print (box[i], end=' ')


# 바구니에 있는 공 위치 바꾸기
# N , M = map(int, input().split())
# box = [i+1 for i in range(N)]

# for r in range(M) :
#     i, j = map(int, input().split())
#     tmp = box[i-1]
#     box[i-1] = box[j-1]
#     box[j-1]= tmp

# for k in range(N):
#     print (box[k], end=' ')

# 과제 안 낸 학생 번호 추출
# summit = []
# student =[i for i in range(1,31)]
# standard = True
# for _ in range(28):
#     number = int(input())   
#     if number >=1 and number <=30 :
#         summit.append(number)
#     else :
#         standard =False
#         break
# if standard :
#     for k in range(30):
#         if summit.count(student[k]) == 0 :  # 2개 나오면 바로 종료
#             print(student[k] )
# else :
#     print('출석번호가 올바르지 않음')

# 과제 안 낸 학생을 추출하는 방법
# student =[i for i in range(1,31)]
# for i in range(28) :
#     submit = int(input())
#     # del(student[(student.index(submit))])
#     student.remove(submit)
# print(min(student))
# print(max(student))

#나머지 개수 구하기
i = list( map (int, input().split()))
count = 0
for k in range(len(i)):
    i[k] = i[k] % 42
    print(i[k])
# if k not in i:
#     count +=1 




