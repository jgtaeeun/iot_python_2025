# 주피터노트북에서 만든 카운터 실습 예제를 py파일로 옮기기
from tkinter import *
import tkinter.font as fnt

root = Tk(className= "카운트 실습 예제")
root.geometry('320x200') # 세로 200은 제목표시줄 제외한 200이기에 제목포함하면 200 넘는다.

# 이벤트
count = 0

def countUp():
    global count # 전역변수 count를 countUp()함수 내에서 사용
    count += 1
    label['text'] = f'버튼클릭:{count}'

def countDown():
    global count # 전역변수 count를 countUp()함수 내에서 사용
    count -= 1
    label['text'] = f'버튼클릭:{count}'

def countInit():
    global count 
    count = 0
    label['text'] = f'버튼클릭:{count}'

myfont = fnt.Font(family='NanumGothic', size=20)

# 숫자카운트를 표시할 라벨
label = Label(root, text='버튼클릭:0' , fg= 'red', font=myfont)
# padx(왼쪽, 오른쪽) , pady(위, 아래 여백)
label.pack(side='left', padx =10)

# countUp이라는 함수가 마우스클릭때마다 실행
buttonUp = Button(root, text='카운트 증가' ,
                font=myfont, 
                command=countUp)
buttonUp.pack(side='top', padx =10 , pady =5)

buttonDown = Button(root, text='카운트 감소' ,
                    font=myfont, 
                    command=countDown)
buttonDown.pack(side='top', padx =10, pady =5)

buttonInit = Button(root, text='초기화' ,
                     font=myfont,
                     command=countInit)
buttonInit.pack(side='bottom', padx =10 ,pady =5)

root.mainloop()