#askcolor(), askinteger() 함수 사용을 위해 사용
from tkinter import* 
from tkinter.colorchooser import*
from tkinter.simpledialog import*

#마우스 클릭을 하면 클릭된 위치의 좌표를 x1, y1에 저장
def mouseClick(event) :
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

#마우스 클릭 상태를 떨어뜨리면 떨어진 위치의 좌표가 x2, y2에 저장
#(x1,y1), (x2,y2) 두 점 사이에 원하는 색과 두께의 선을 그린다.
def mouseDrop(event) :
    global x1, y1, x2, y2, penWidth, penColor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2, width = penWidth, fill = penColor)

#원하는 선의 색 선택
def getColor() :
    global penColor
    color = askcolor()
    penColor = color[1]

#원하는 선의 두께 선택
def getWidth() :
    global penWidth
    penWidth = askinteger("선 두께", "선 두께(1~10)를 입력하세요", minvalue = 1, maxvalue = 10)

#전역변수 설정
window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None
penColor = 'black'
penWidth = 5

##2019038010 박준용##

if __name__ == "__main__" :
    #윈도우 창 설정
    window = Tk()
    window.title("그림판과 비슷한 프로그램")
    canvas = Canvas(window, height = 300, width = 300)
    #마우스 클릭과 드롭에 대한 키값을 넣는다
    canvas.bind("<Button-1>", mouseClick)
    canvas.bind("<ButtonRelease-1>", mouseDrop)
    #그림판 세팅
    canvas.pack()

    #배너 설정(설정 안에 색상과 두께 배너가 있고 사용자가 원하는 색이나 두께 설정 가능)
    mainMenu = Menu(window)
    window.config(menu = mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "설정", menu = fileMenu)
    fileMenu.add_command(label = "선 색상 선택", command = getColor)
    fileMenu.add_separator()
    fileMenu.add_command(label = "선 두께 설정", command = getWidth)

    window.mainloop()
