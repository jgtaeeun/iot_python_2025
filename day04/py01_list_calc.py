# 리스트 연산
# 리스트가 for, while 반복문에서 가장 많이 활용되는 구조

# iterable -> 반복할 수 있는 요소가 for, while문에 사용
# 자료구조 중 딕셔너리(키, 값으로 저장 용도),리스트(반복용도)가 가장 많이 나온다.

# sum = 0
# listSample = [1,2,3,4,5,6,7,8,9,10]
# for i in listSample:
#     sum = sum + i
# print(f'합산 결과 : {sum}')

# 리스트 연산
array = [1,2,3,4,5]
# print(array)
# print(array[0] + array[2])
# print(array[-2])
# print(array[2:])
# print(array[2:3])

array2 = [2,4,6,8,10]
# print(array2 + array)   #리스트 더하기(연결)
# print(array2 * 2 )      #리스트 곱하기(반복)

# print(len(array2))
# array2[2] = 7           #리스트의 데이터 할당(수정) 
# print(array2)

# #리스트의 요소 삭제
# del(array2[2])
# print(array2)
# print(len(array2))

# # 리스트의 요소 추가
# array2.append(12)
# print(array2)

# array2.insert(0, 100)
# print(array2)

# 리스트 합칠 때
# array2 + array
# print(array2.extend(array))

# 리스트 정렬
# 쇼핑몰 낮은, 높은 가격순/최신일자
array3 = [6,7,1,3,9,0,2,8]
array3.sort()
print(array3)
array3.sort(reverse=True)
print(array3)

#요소의 위치 파악
print(array3.index(1))

#요소 꺼내기-pop

print(array3.pop())
print(array3)

# 리스트 컴프리핸션
arr = [i for i in range(1,100+1)]
print(arr)

# 1부터 100까지의 합산
sum = 0
for i in arr:
    sum += i
print(f'1부터 {len(arr)}까지의 합산: {sum}')

# 1부터 100까지의 짝수의 합 
sum =0
arr_even = [i for i in range(1,100+1,2)]
for i in arr_even :
    sum = sum + i
print(f'1부터 100까지의 짝수의 합 : {sum}')


