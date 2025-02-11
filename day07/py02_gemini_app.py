# tkinter를 클래스화

from tkinter import *               # tkinter모듈에 있는 모든 클래스, 함수, 변수 등을 다 씀
from tkinter.messagebox import *    # 모듈 밑에 있는 모듈을 from tkinter import * 로 가져올 수 없음
from tkinter.scrolledtext import *    
from tkinter.font import *   
import google.generativeai as genai

genai.configure(api_key='api 입력해야함')
model = genai.GenerativeModel( model_name="gemini-1.5-flash")



class window(Tk):
    def __init__(self):
        super().__init__()  # 부모객체도 같이 초기화
        self.title ('gemini 챗봇 v2.0')
        self.geometry('730x450')

       
        # self.iconbitmap('chat-bot.ico')  # pyinstaller 때는 실행파일폴더에 icon복사

        self.iconbitmap('./day07/chat-bot.ico')

        # 클래스 작업할 땐, self 키워드 유심히 잘 봐야함
        self.protocol('WM_DELETE_WINDOW', self.onClosing)

        self.initWindow() # 윈도우 화면 초기화 멤버함수 (메서드)

    def onClosing(self):
        if askyesno('종료확인','종료하시겠습니까?') :
            self.destroy()

    def initWindow(self):
        self.myFont = Font(family='NanumGothic', size=10)
        self.boldFont = Font(family='NanumGothic', size=10, weight='bold', slant=ITALIC)

        self.textFrame = Frame(self, width=730, height=30, bg='#EFEFEF')
        self.textFrame.pack(side=BOTTOM,fill=BOTH)

        self.textMessage = Text(self.textFrame, width=75 ,height=1,wrap=WORD , font= self.myFont)
        self.textMessage.bind('<KeyPress>', self.keypress)
        self.textMessage.pack(side=LEFT,padx=15)
    
        self.buttonSend = Button(self.textFrame, width=30, text='전송', fg='white',bg = 'green' , 
                    font=self.myFont, command=self.responseMessage)
        self.buttonSend.pack(side=RIGHT,padx=20, pady=5)

        self.textResult = ScrolledText(self, wrap=WORD , bg = '#000000' , fg= '#ffffff' , font= self.myFont)
        self.textResult.pack(fill=BOTH, expand=True)


        self.textResult.tag_config('user', font=self.boldFont, foreground='yellow')
        self.textResult.tag_config('ai', font=self.myFont, foreground='limegreen')
        self.textResult.tag_config('error', font=self.boldFont, foreground='red')

        self.textMessage.focus_set()

    def keypress(self, event):
        if event.char == '\r' :
            self.responseMessage()

    def responseMessage(self):
        inputText = self.textMessage.get('1.0', END).replace('\n' ,'').strip()
        self.textMessage.delete('1.0', END)  # 보낸 메시지 text 초기화
       
        if inputText :
                try:
                    self.textResult.insert(END , '나: ', BOLD)
                    self.textResult.insert(END , f'{inputText}\n\n' ,'user')
                    
                    ai_response = model.generate_content(inputText)
                    response = ai_response.text
                    self.textResult.insert(END , '챗봇: ', 'bold')
                    self.textResult.insert(END, f'{response}\n\n', 'ai')   #'ai' 텍스트 태그

                except Exception as e :
                    self.textResult.insert(END, f'Error:{str(e)}\n\n', 'error')
                finally :
                    self.textResult.see(END)             # 결과 메시지를 스크롤 마지막내용을 보여줌


if __name__ == '__main__' :
    print('tkinter클래스 시작')
    gemini_app = window()   # tkinter 객체 생성
    gemini_app.mainloop()


    
    


    
