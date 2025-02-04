# 문자열 포맷팅

loginTemp = '안녕하세요, %s님!'
name = '윤'
print(loginTemp %(name))

name = input('로그인할 이름 입력: ')
print(loginTemp %(name))


# 구세대 문자열 포맷팅
intro = '나는 %s(이)고, %d살입니다. 몸무게는 %fkg입니다.'
print(intro % ('리사', 24, 48.5))

intro = '나는 %10s(이)고, %03d살입니다. 몸무게는 %3.2fkg입니다.'
print(intro % ('리사', 24, 48.5))

# 중간세대 문자열 포맷팅
intro = '나는 {0}이고, {1}살입니다. 몸무게는 {2}kg입니다.'
print(intro.format('하늘', 30, 50))

intro = '나는 {0:10s}이고, {1}살입니다. 몸무게는 {2}kg입니다.'
print(intro.format('하늘', 30, 50))

intro = '나는 {0:>10s}이고, {1}살입니다. 몸무게는 {2}kg입니다.'
print(intro.format('하늘', 30, 50))

# 신세대
name = '세라'
age = 45
weight = 52.8
print(f'나는 {name:>10}이고, {age}살입니다. 몸무게는 {weight}kg입니다.')
print(f'나는 {name:10}이고, {age}살입니다. 몸무게는 {weight}kg입니다.')