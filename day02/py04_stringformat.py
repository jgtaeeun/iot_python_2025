# 문자열 포맷팅

loginTemp = '안녕하세요, %s님!'
name = '윤'
# print(loginTemp %(name))

name = input('로그인할 이름 입력: ')
print(loginTemp %(name))
