from tkinter import *
import tkinter.font as fnt
from tkinter.messagebox import *

def ButtonClick():
    #showinfo, showerror, showwarning
    showinfo('위젯', '버튼을 클릭했습니다.')    # 메세지 박스
   
root = Tk()
root.geometry('800x900')
root.title('위젯 예제')

# 레이블에 이미지 표시
img = PhotoImage(file='./day06/baoFamily.png')
label=Label(root, image=img)
label.pack()

# 버튼 위젯
button = Button(root, text='클릭', command= ButtonClick)
button.pack()

# 엔트리 위젯 -사용자 입력
entry = Entry(root) 
entry.pack()

# 라디오버튼
Label(root, text='가장 선호하는 음식(1가지)').pack()
choice = IntVar()
Radiobutton(root,text='워토우', value=1, variable=choice).pack(anchor=W)
Radiobutton(root,text='사과', value=2 , variable=choice ).pack(anchor=W)
Radiobutton(root,text='당근', value=3, variable=choice ).pack(anchor=W)
Radiobutton(root,text='대나무', value=4 , variable=choice ).pack(anchor=W)

# 체크박스
Label(root, text='좋아하는 판다 모두 선택').pack()
ibao = IntVar()
Checkbutton(root, text='아이바오', variable=ibao).pack(anchor=W)
lubao = IntVar()
Checkbutton(root, text='러바오', variable=lubao ).pack(anchor=W)
fubao = IntVar()
Checkbutton(root, text='푸바오', variable=fubao).pack(anchor=W)

# 리스트박스 위젯
lstBx = Listbox(root, height=4)
lstBx.pack()
lstBx.insert(END, '강바오')
lstBx.insert(END,'송바오')
lstBx.insert(END,'오바오')
lstBx.insert(END,'편집바오')

# 컨테이너 위젯 중 프레임
frame = Frame(root, width=700, height=100, bg='gray')
frame.pack()

# 프레임에 들어갈 위젯
button2 = Button(frame, text='버튼2', width=30)
button2.pack(side=LEFT)
button3 = Button(frame, text='버튼3', width=30)
button3.pack(side=LEFT)
button4= Button(frame, text='버튼4', width=30)
button4.pack(side=LEFT)

root.mainloop()