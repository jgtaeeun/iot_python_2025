# while  - for
# while (조건이 참인 동안):
#       구문안에서 반복



# 1부터 10까지의 수 합산
sum = 0
i = 1

# while i <= 10 :
#     print(i)
#     i += 1  

while i <= 10 :
    sum += i
    i += 1
print(f'1부터 10까지의 수 합산은 {sum}입니다.')


sum = 0
for j in range(1, 10+1) :
    sum += j
print(f'1부터 10까지의 수 합산은 {sum}입니다.')

