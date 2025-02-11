from tkinter import *               # tkinter모듈에 있는 모든 클래스, 함수, 변수 등을 다 씀
from tkinter.messagebox import *    # 모듈 밑에 있는 모듈을 from tkinter import * 로 가져올 수 없음
from tkinter.scrolledtext import *    
from tkinter.font import *    

# 5. gemini 위한 모듈
import google.generativeai as genai

# 6.  gemini 연결 설정
genai.configure(api_key='')
model = genai.GenerativeModel( model_name="gemini-1.5-flash")



def responseMessage():
    inputText = textMessage.get('1.0', END).replace('\n' ,'').strip()
    # print(inputText)
    # '1.0'은 텍스트 위젯의 첫 번째 줄 첫 번째 문자(시작 위치)를 의미합니다.
    # END는 텍스트의 끝을 의미합니다. 그래서 이 코드는 텍스트 위젯의 처음부터 끝까지 모든 텍스트를 가져옵니다.
 
    textMessage.delete('1.0', END)  # 보낸 메시지 text 초기화

    if inputText :
        try:
            textResult.insert(END , '나: ', BOLD)
            textResult.insert(END , f'{inputText}\n\n' ,'user')
            
            ai_response = model.generate_content(inputText)
            response = ai_response.text
            textResult.insert(END , '챗봇: ', 'bold')
            textResult.insert(END, f'{response}\n\n', 'ai')   #'ai' 텍스트 태그

        except Exception as e :
            textResult.insert(END, f'Error:{str(e)}\n\n', 'error')
        finally :
            textResult.see(END)             # 결과 메시지를 스크롤 마지막내용을 보여줌

def keypress(event) :
    # print(repr(event.char)) #repr()을 안 쓰면 '\r', '', '\x08'등이 표시 안 됨/tkinter에서는 '\r'을 쓴다.
    # '\r' : 캐리지 리턴     '\n' : 뉴라인
    if event.char == '\r' :
        responseMessage()
    
def onClosing():
    if askyesno('종료확인','종료하시겠습니까?') :
        root.destroy()

root = Tk()
root.title('gemini 챗봇')
root.geometry('730x450')
# 12. 아이콘 변경
root.iconbitmap('./day07/chat-bot.ico')

# 7. 폰트 지정
myFont = Font(family='NanumGothic', size=10)
boldFont = Font(family='NanumGothic', size=10, weight='bold', slant=ITALIC)

# 2. UI 화면 구성
textFrame = Frame(root, width=730, height=30, bg='#EFEFEF')
textFrame.pack(side=BOTTOM,fill=BOTH)

# 3. textFrame에 들어갈 entry와 button 구성
textMessage = Text(textFrame, width=75 ,height=1,wrap=WORD , font=myFont )
# 8. 입력창에서 enter으루 치면 이벤트 keypress 발생
textMessage.bind('<KeyPress>', keypress)
textMessage.pack(side=LEFT,padx=15)

buttonSend = Button(textFrame, width=30, text='전송', fg='white',bg = 'green' , 
                    font=myFont, command=responseMessage)
buttonSend.pack(side=RIGHT,padx=20, pady=5)

# 4. API호출 결과메시지 출력될 스크롤기능 텍스트 위젯
textResult = ScrolledText(root, wrap=WORD , bg = '#000000' , fg= '#ffffff' , font=myFont)
textResult.pack(fill=BOTH, expand=True)

# 10 . 스크롤텍스트에 나올 메시지를 디자인
textResult.tag_config('user', font=boldFont, foreground='yellow')
textResult.tag_config('ai', font=myFont, foreground='limegreen')
textResult.tag_config('error', font=boldFont, foreground='red')
# 9. 실행 후 바로 입력창에 포커스가 가도록
textMessage.focus_set()

# 11. 종료버튼 (X)를 누르면 종료메시지 확인 후 종료
root.protocol('WM_DELETE_WINDOW', onClosing)
# 종료시까지 계속 실행
root.mainloop()