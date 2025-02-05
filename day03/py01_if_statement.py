# if

# age = int(input('나이 입력> '))
# if age > 10 or age == 10 :
#     print(age , '입니다')

# 파이썬은 대문자, 소문자 구분
grade = input('학점입력 (A|B|C|D|F)> ').upper()
if grade == 'A' or grade == 'B' :
    print('공부열심히했네')
    print('축하')
    if grade == 'A' :
        print('장학금 대상자네')
elif grade == 'C' :
    print('그럭저럭 했네')
else :
    print('공부 해라')
