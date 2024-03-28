from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

## 함수 선언 부분 ##
def func_open() :#함수열기
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)

    width = photo.width() #이미지 크기
    height = photo.height() #이미지 크기

    for i in range(height) : #이중 for 문
        for k in range(width) :
            r, g, b = photo.get(k, i) #각각의 rgb값 가져옴
            grey = int((r+g+b)/3) #색상을 회색 값으로 함
            photo.put("#%02x%02x%02x" % (grey, grey, grey), (k, i))  #이미지 픽셀값을 변경

    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()


## 메인 코드  부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기(흑백)")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)





window.mainloop()
