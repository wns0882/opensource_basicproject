#동물을 누르면 label에 해당 동물 사진이 뜨는 프로그램

from tkinter import*

#선택한 라디오 버튼이 이미지를 바꾸도록 설정
def myFunc():
    if var.get() == 1 :
        labelImage.configure(image = photo1)
    elif var.get() == 2 :
        labelImage.configure(image = photo2)
    else :
        labelImage.configure(image = photo3)
        

var, labelImage = 0, None
photo1, photo2, photo3 = [None] *3
##2019038010 박준용##
if __name__ == "__main__" :
    #윈도창 화면 설정
    window = Tk()
    window.geometry("400x400")
    window.title("애완동물 선택하기")
    labelText = Label(window, text = "좋아하는 동물 투표 ", fg = "blue",
                       font = ("궁서체", 20))
    #라디오 버튼 값 변수
    var = IntVar()
    #강아지(1), 고양이(2), 토끼(3)을 선택 시 해당 라디오 버튼 값이 들어감
    rb1 = Radiobutton(window, text = "강아지", variable = var, value = 1)
    rb2 = Radiobutton(window, text = "고양이", variable = var, value = 2)
    rb3 = Radiobutton(window, text = "토끼", variable = var, value = 3)
    
    #해당 버튼 값에 따라 myFunc 함수 실행
    buttonOk = Button(window, text = "사진 보기", command = myFunc)

    photo1 = PhotoImage(file = "C:\Python\gif/dog.GIF")
    photo2 = PhotoImage(file = "C:\Python\gif/cat.GIF")
    photo3 = PhotoImage(file = "C:\Python\gif/rabbit.GIF")

    #사진이 출력되는 label 설정
    labelImage = Label(window, width = 400, height = 400, bg = "yellow",
                       image = None)

    #위젯 간격 설정
    labelText.pack(padx = 5, pady = 5)
    rb1.pack(padx = 5, pady = 5)
    rb2.pack(padx = 5, pady = 5)
    rb3.pack(padx = 5, pady = 5)
    buttonOk.pack(padx = 5, pady = 5)
    labelImage.pack(padx = 5, pady = 5)

    window.mainloop()
