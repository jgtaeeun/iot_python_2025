# 수학 모듈
import math
import random


# print(math.pi)

# print(2**10)            #int
# print(math.pow(2,10))   #float
# print(math.sqrt(4))
# print(math.log10(10))

# numbers = [i for i in range(1, 45+1)]
# result = []

# for i in range(6):  #여섯 번 반복
#     result.append(random.choice(numbers))
# print(result)

numbers = weight= list(range(1,45+1))
random.shuffle(weight)
result = random.choices(numbers, weights=weight, k=6)
print(result)





