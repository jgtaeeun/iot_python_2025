# 파일 입출력
# 파일 오픈, 읽고, 쓰고 , 닫음
# 파일경로-절대, 상대경로
# 경로 구분자 \ / 다 사용가능
# mode : r, w, a(추가)
# encoding : 한글만 (euc-kr, cp949) , 국제어(utf-8)



# f = open('./test.txt' , mode = 'w' , encoding='utf-8')                           # 상대경로 (경로를 특수문자로 생략하는 법) :  . (현재위치) ..(부모폴더 위치)
# f.write('저는 한국사람입니다.')
# print('파일쓰기 완료')
# f.close()


# f = open('./day03/test.txt' , mode = 'w' , encoding='utf-8')                           # 상대경로 (경로를 특수문자로 생략하는 법) :  . (현재위치) ..(부모폴더 위치)
# f.write('저는 한국사람입니다.')
# print('파일쓰기 완료')
# f.close()


# f = open('C:/Source/iot_python_2025/day03/test2.txt' , mode = 'w' , encoding='utf-8')   # 절대경로 (드라이브부터 모든 경로를 다 작성) C:\Source\iot_python_2025
# f.write('저는 한국사람입니다.')
# print('파일쓰기 완료')

# f = open('C:/Source/iot_python_2025/day03/test2.txt' , mode = 'w' , encoding='utf-8')   
# f.write('1번째 줄 작성합니다.\n')
# f.write('2번째 줄 작성합니다.')

r = open('C:/Source/iot_python_2025/day03/test2.txt' , mode = 'r' , encoding='utf-8')   
while True:
    line = r.readline() #한줄씩 읽음 
    if not line :       #한줄 읽은 값이 None이면
        break
    #print(line, end='')
    print(line.replace('\n',''))
    #print(line)
r.close()

