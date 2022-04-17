#gif 선택 후 해당 gif 파일을 화살표 위 또는 아래 키를 눌러 확대 또는 축소하는 프로그램

from tkinter import *
#askopenfilename()을 쓰기 위해 사용
from tkinter.filedialog import *

#파일을 오픈하는 함수
def func_open():
    #해당 파일을 축소나 확대 때 다시 쓰이므로 global
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"),
                ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    #해당 사진 세팅
    pLabel.configure(image = photo)
    pLabel.image = photo

#종료 함수
def func_exit():
    window.quit()
    window.destroy() 

#파일 확대 함수
def func_zoom(event):
    photo = PhotoImage(file = filename)
    #2배 확대
    photo = photo.zoom(2,2)
    pLabel.configure(image = photo)
    pLabel.image = photo

#파일 축소 함수
def func_subsample(event):
    photo = PhotoImage(file = filename)
    #1/2배 축소
    photo = photo.subsample(2,2)
    pLabel.configure(image = photo)
    pLabel.image = photo

##2019038010 박준용##

#윈도우 창 화면 설정
window = Tk()
window.geometry("400x400")
window.title("연습문제")

#사진 설정
photo = PhotoImage()
pLabel = Label(window,image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

#배너 설정
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일',menu = fileMenu)
fileMenu.add_command(label = '파일 열기', command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = '프로그램 종료', command = func_exit)

#파일 확대 축소
#화살표 위나 아래키를 누르면 해당 함수가 실행
window.bind("<Up>", func_zoom)
window.bind("<Down>", func_subsample)

window.mainloop()
