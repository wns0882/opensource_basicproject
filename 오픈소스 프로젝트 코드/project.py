import tkinter as tk
from tkinter import*
from tkinter import messagebox
import openpyxl
import operator
from tkinter.simpledialog import *

wb=openpyxl.load_workbook('projectlist.xlsx')
sheet1=wb.active
sheet=wb['Sheet1']

from collections import deque
li = deque([])

def PrintMessage():
    keyStr = "C"+str(key)
    textstr = sheet[keyStr].value
    messagebox.showinfo("상세주소",textstr)

def EnterKey(temp):
    global key
    key = temp

def give_stars(index):
        coment=askstring("문자열 입력", "별점 입력(1~5 중 입력)")
        cell='I'+str(index)
        sheet1[cell]=coment
        wb.save('projectlist.xlsx')

class Samplewindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # 버튼 순서에 맞춰 들어갈 사진 경로 설정
        
        photoAry = [tk.PhotoImage(file="한식 (2).gif"), 
            tk.PhotoImage(file="일식.gif"),
            tk.PhotoImage(file="중식.gif"),
            tk.PhotoImage(file="양식.gif"),
            tk.PhotoImage(file="분식.gif"),
            tk.PhotoImage(file="고기.gif"),
            tk.PhotoImage(file="패스트푸드.gif"),
            tk.PhotoImage(file="별점입력.gif"),
            tk.PhotoImage(file="별점랭킹.gif"),
            tk.PhotoImage(file="맛집검색.gif"),
            tk.PhotoImage(file="최근에본식당.gif"),
            tk.PhotoImage(file="종료.gif")]

        commandAry = [lambda: master.switch_frame(Page1),
        lambda: master.switch_frame(Page2),
        lambda: master.switch_frame(Page3),
        lambda: master.switch_frame(Page4),
        lambda: master.switch_frame(Page5),
        lambda: master.switch_frame(Page6),
        lambda: master.switch_frame(Page7),
        lambda: master.switch_frame(Page8),
        lambda: master.switch_frame(Page9),
        lambda: master.switch_frame(Page10),
        lambda: master.switch_frame(Page11)]

        photo1=tk.PhotoImage(file="탑메뉴.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=1,columnspan=4)

        btn0 = tk.Button(self, image=photoAry[0], command=commandAry[0])
        btn0.image = photoAry[0]        
        btn0.grid(row=2,column=1)

        btn1 = tk.Button(self, image=photoAry[1], command=commandAry[1])
        btn1.image = photoAry[1]        
        btn1.grid(row=2,column=2)

        btn2 = tk.Button(self, image=photoAry[2], command=commandAry[2])
        btn2.image = photoAry[2]         
        btn2.grid(row=2,column=3)

        btn3 = tk.Button(self, image=photoAry[3], command=commandAry[3])
        btn3.image = photoAry[3]         
        btn3.grid(row=2,column=4)

        btn4 = tk.Button(self, image=photoAry[4], command=commandAry[4])
        btn4.image = photoAry[4]        
        btn4.grid(row=3,column=1) 

        btn5 = tk.Button(self, image=photoAry[5], command=commandAry[5])
        btn5.image = photoAry[5]      
        btn5.grid(row=3,column=2)

        btn6 = tk.Button(self, image=photoAry[6], command=commandAry[6])
        btn6.image = photoAry[6]         
        btn6.grid(row=3,column=3)

        btn7 = tk.Button(self, image=photoAry[7], command=commandAry[7])
        btn7.image = photoAry[7]         
        btn7.grid(row=4,column=1)

        btn8 = tk.Button(self, image=photoAry[8], command=commandAry[8])
        btn8.image = photoAry[8]         
        btn8.grid(row=4,column=2)

        btn9 = tk.Button(self, image=photoAry[9], command=commandAry[9])
        btn9.image = photoAry[9]         
        btn9.grid(row=4,column=3)

        #최근에 본 식당 
        btn10 = tk.Button(self, image=photoAry[10], command=commandAry[10])
        btn10.image = photoAry[10]         
        btn10.grid(row=3,column=4,columnspan=2)

        #종료
        btn11 = tk.Button(self, image=photoAry[11], command=exit)
        btn11.image = photoAry[11]         
        btn11.grid(row=4,column=4)

#한식
class Page1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정

        photoback=tk.PhotoImage(file="뒤로가기.gif")
        btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(StartPage))
        btnBack.image = photoback
        btnBack.grid(row=1,column=1)   
        
        photo1=tk.PhotoImage(file="한식탑.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=2,columnspan=4)

        photo=[]
        button=[]

        for i in range(0,15):
            temp = i+98
            tempStr = "B"+str(temp)
            photo.append(tk.PhotoImage(file=sheet[tempStr].value))
            button.append(tk.Button(self,image=photo[i])) 
            button[i].image = photo[i]

        a = 2; b = 1;

        for i in range (0,15):
            button[i].config(command=lambda x=i+98:[EnterKey(x),master.switch_frame(Page12)])
            button[i].grid(row = a,column = b)
            b += 1
            if b>5:
                b=1
                a +=1

#일식
class Page2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정

        photoback=tk.PhotoImage(file="뒤로가기.gif")
        btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(StartPage))
        btnBack.image = photoback
        btnBack.grid(row=1,column=1)   
        
        photo1=tk.PhotoImage(file="일식탑.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=2,columnspan=4)

        photo=[]
        button=[]

        for i in range(0,15):
            temp = i+50
            tempStr = "B"+str(temp)
            photo.append(tk.PhotoImage(file=sheet[tempStr].value))
            button.append(tk.Button(self,image=photo[i]))
            button[i].image = photo[i]

        a = 2; b = 1;

        for i in range (0,15):
            button[i].config(command=lambda x=i+50:[EnterKey(x),master.switch_frame(Page12)])
            button[i].grid(row = a,column = b)
            b += 1
            if b>5:
                b=1
                a +=1

#중식
class Page3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정

        photoback=tk.PhotoImage(file="뒤로가기.gif")
        btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(StartPage))
        btnBack.image = photoback
        btnBack.grid(row=1,column=1)   
        
        photo1=tk.PhotoImage(file="중식 탑.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=2,columnspan=4)

        photo=[]
        button=[] 

        for i in range(0,15):
            temp = i+66
            tempStr = "B"+str(temp)
            photo.append(tk.PhotoImage(file=sheet[tempStr].value))
            button.append(tk.Button(self,image=photo[i]))
            button[i].image = photo[i]

        a = 2; b = 1;

        for i in range (0,15):
            button[i].config(command=lambda x=i+66:[EnterKey(x),master.switch_frame(Page12)])
            button[i].grid(row = a,column = b)
            b += 1
            if b>5:
                b=1
                a +=1

#양식
class Page4(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정

        photoback=tk.PhotoImage(file="뒤로가기.gif")
        btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(StartPage))
        btnBack.image = photoback
        btnBack.grid(row=1,column=1)   
        
        photo1=tk.PhotoImage(file="양식탑.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=2,columnspan=4)

        photo=[]
        button=[]

        for i in range(0,15):
            temp = i+34
            tempStr = "B"+str(temp)
            photo.append(tk.PhotoImage(file=sheet[tempStr].value))
            button.append(tk.Button(self,image=photo[i]))
            button[i].image = photo[i]

        a = 2; b = 1;

        for i in range (0,15):
            button[i].config(command=lambda x=i+34:[EnterKey(x),master.switch_frame(Page12)])
            button[i].grid(row = a,column = b)
            b += 1
            if b>5:
                b=1
                a +=1

#분식
class Page5(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정

        photoback=tk.PhotoImage(file="뒤로가기.gif")
        btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(StartPage))
        btnBack.image = photoback
        btnBack.grid(row=1,column=1)   
        
        photo1=tk.PhotoImage(file="분식탑.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=2,columnspan=4)
        
        photo=[]
        button=[]

        for i in range(0,15):
            temp = i+18
            tempStr = "B"+str(temp)
            photo.append(tk.PhotoImage(file=sheet[tempStr].value))
            button.append(tk.Button(self,image=photo[i]))
            button[i].image = photo[i]

        a = 2; b = 1;
    
        for i in range (0,15):
            button[i].config(command=lambda x=i+18:[EnterKey(x),master.switch_frame(Page12)])
            button[i].grid(row = a,column = b)
            b += 1
            if b>5:
                b=1
                a +=1

#고기
class Page6(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정

        photoback=tk.PhotoImage(file="뒤로가기.gif")
        btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(StartPage))
        btnBack.image = photoback
        btnBack.grid(row=1,column=1)   
        
        photo1=tk.PhotoImage(file="고기탑.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=2,columnspan=4)
    
        photo=[]
        button=[]

        for i in range(0,15):
            temp = i+2
            tempStr = "B"+str(temp)
            photo.append(tk.PhotoImage(file=sheet[tempStr].value))
            button.append(tk.Button(self,image=photo[i]))
            button[i].image = photo[i]

        a = 2; b = 1;

        for i in range (0,15):
            button[i].config(command=lambda x=i+2:[EnterKey(x),master.switch_frame(Page12)])
            button[i].grid(row = a,column = b)
            b += 1
            if b>5:
                b=1
                a +=1

#패스트푸드
class Page7(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정

        photoback=tk.PhotoImage(file="뒤로가기.gif")
        btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(StartPage))
        btnBack.image = photoback
        btnBack.grid(row=1,column=1)   
        
        photo1=tk.PhotoImage(file="패스트푸드탑.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=2,columnspan=4)

        photo=[]
        button=[]

        for i in range(0,15):
            temp = i+82
            tempStr = "B"+str(temp)
            photo.append(tk.PhotoImage(file=sheet[tempStr].value))
            button.append(tk.Button(self,image=photo[i]))
            button[i].image = photo[i]

        a = 2; b = 1
            
        for i in range (0,15):
            button[i].config(command=lambda x=i+82:[EnterKey(x),master.switch_frame(Page12)])
            button[i].grid(row = a,column = b)
            b += 1
            if b>5:
                b=1
                a +=1

def give_stars(index):
        coment=askstring("문자열 입력", "별점 입력(1~5 중 입력)")
        cell='I'+str(index)
        sheet1[cell]=coment
        wb.save('projectlist.xlsx')

#별점 입력
class Page8(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정

        photoback=tk.PhotoImage(file="뒤로가기.gif")
        btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(StartPage))
        btnBack.image = photoback
        btnBack.grid(row=1,column=1)   
        
        photo1=tk.PhotoImage(file="별점입력탑.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=2,columnspan=3)

        def showInput(event):
            count = 2
            name1 = ent1.get()
            for i in sheet.rows:
                if i[0].value == name1:
                    photoSearch = tk.PhotoImage(file=i[1].value)
                    btnSearch = tk.Button(self,image = photoSearch)
                    btnSearch.config(command=lambda: [EnterKey(count-1),give_stars(count-1)])
                    btnSearch.image = photoSearch
                    btnSearch.grid(row=2,column=1)
                    break
                else:
                    count = count+1
                    continue

        #검색창 구현
        self.option_add('*Font','궁서 60')
        ent1 = Entry(self) # 입력창 선언
        ent1.bind("<Return>",showInput);
        ent1.grid(row=2,column=2)

#별점랭킹
class Page9(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정

        photoback=tk.PhotoImage(file="뒤로가기.gif")
        btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(StartPage))
        btnBack.image = photoback
        btnBack.grid(row=1,column=1)   
        
        photo1=tk.PhotoImage(file="별점랭킹탑.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=2,columnspan=4)

        ranking=[]
        star=5
        count=0
        while True:
            for i in sheet.rows:
                if(operator.eq(i[8].value,str(star))):
                    ranking.append(i)
                    count+=1
                if count==10:
                    break
            star=star-1
            if count==10 or star==-1:
                break
        a=1
        e=0
        for k in ranking:

            photoranking=tk.PhotoImage(file=k[1].value)
            button = tk.Button(self, image=photoranking, command=lambda x=k[8].value:messagebox.showinfo("별점",x))
            button.image = photoranking
            button.grid(row=2+e,column=a)
            a=a+1
            if a==6:
                a=1
                e+=1

#맛집검색
class Page10(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정

        photoback=tk.PhotoImage(file="뒤로가기.gif")
        btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(StartPage))
        btnBack.image = photoback
        btnBack.grid(row=1,column=1)   
        
        photo1=tk.PhotoImage(file="맛집검색탑.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=2,columnspan=4)
        
        def showInput(event):
            count = 2
            name1 = ent1.get()
            for i in sheet.rows:
                if i[0].value == name1:
                    photoSearch = tk.PhotoImage(file=i[1].value)
                    btnSearch = tk.Button(self,image = photoSearch)
                    btnSearch.config(command=lambda: [EnterKey(count-1),master.switch_frame(Page12)])
                    btnSearch.image = photoSearch
                    btnSearch.grid(row=2,column=1)
                    break
                else:
                    count = count+1
                    continue
                
        #검색창 구현
        self.option_add('*Font','궁서 60')
        ent1 = Entry(self) # 입력창 선언
        ent1.bind("<Return>",showInput);
        ent1.grid(row=2,column=2)

def makeLabel(f):
    if len(li) == 0: return
    label = []
    if len(li)>15:
        li.popleft()
    for i in range(len(li)):
        l = tk.PhotoImage(file=sheet[li[i]].value)
        photoLabel2 = tk.Label(f, image=l)
        photoLabel2.image = l
        label.append(photoLabel2)

    a = 2; b = 1

    for i in range (0,15):
        if i == len(label):
            break
        label[i].grid(row = a,column = b)
        b += 1
        if b>5:
            b=1
            a +=1
        
#최근에본식당
class Page11(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정

        photoback=tk.PhotoImage(file="뒤로가기.gif")
        btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(StartPage))
        btnBack.image = photoback
        btnBack.grid(row=1,column=1)   
        
        photo1=tk.PhotoImage(file="최근에본식당탑.gif")
        photoLabel = tk.Label(self, image=photo1)
        photoLabel.image = photo1
        photoLabel.grid(row=1,column=2,columnspan=4)

        makeLabel(self)

#가게 상세정보 페이지(label 3개 button 1개)
class Page12(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) # 고정
        
        if ((key>1)and(key<17)):
            photoback=tk.PhotoImage(file="뒤로가기.gif")
            btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(Page6))
            btnBack.image = photoback
            btnBack.grid(row=0,column=0)
            photo=tk.PhotoImage(file="고기탑.gif")
            photoLabel = tk.Label(self, image=photo)
            photoLabel.image = photo
            photoLabel.grid(row=0,column=1,columnspan=3)

        elif ((key>17)and(key<33)):
            photoback=tk.PhotoImage(file="뒤로가기.gif")
            btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(Page5))
            btnBack.image = photoback
            btnBack.grid(row=0,column=0)
            photo=tk.PhotoImage(file="분식탑.gif")
            photoLabel = tk.Label(self, image=photo)
            photoLabel.image = photo
            photoLabel.grid(row=0,column=1,columnspan=3)

        elif ((key>33)and(key<49)):
            photoback=tk.PhotoImage(file="뒤로가기.gif")
            btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(Page4))
            btnBack.image = photoback
            btnBack.grid(row=0,column=0)
            photo=tk.PhotoImage(file="양식탑.gif")
            photoLabel = tk.Label(self, image=photo)
            photoLabel.image = photo
            photoLabel.grid(row=0,column=1,columnspan=3)

        elif ((key>49)and(key<65)):
            photoback=tk.PhotoImage(file="뒤로가기.gif")
            btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(Page2))
            btnBack.image = photoback
            btnBack.grid(row=0,column=0)
            photo=tk.PhotoImage(file="일식탑.gif")
            photoLabel = tk.Label(self, image=photo)
            photoLabel.image = photo
            photoLabel.grid(row=0,column=1,columnspan=3)

        elif ((key>65)and(key<81)):
            photoback=tk.PhotoImage(file="뒤로가기.gif")
            btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(Page3))
            btnBack.image = photoback
            btnBack.grid(row=0,column=0)
            photo=tk.PhotoImage(file="중식 탑.gif")
            photoLabel = tk.Label(self, image=photo)
            photoLabel.image = photo
            photoLabel.grid(row=0,column=1,columnspan=3)

        elif ((key>81)and(key<97)):
            photoback=tk.PhotoImage(file="뒤로가기.gif")
            btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(Page7))
            btnBack.image = photoback
            btnBack.grid(row=0,column=0)
            photo=tk.PhotoImage(file="패스트푸드탑.gif")
            photoLabel = tk.Label(self, image=photo)
            photoLabel.image = photo
            photoLabel.grid(row=0,column=1,columnspan=3)

        elif ((key>97)and(key<113)):
            photoback=tk.PhotoImage(file="뒤로가기.gif")
            btnBack = tk.Button(self,image=photoback,command=lambda: master.switch_frame(Page1))
            btnBack.image = photoback
            btnBack.grid(row=0,column=0)
            photo=tk.PhotoImage(file="한식탑.gif")
            photoLabel = tk.Label(self, image=photo)
            photoLabel.image = photo
            photoLabel.grid(row=0,column=1,columnspan=3)
            
        #가게이름을 540x400 출력
        keyStr = "J"+str(key)
        photo1=tk.PhotoImage(file=sheet[keyStr].value)
        photoLabel1 = tk.Label(self, image=photo1)
        photoLabel1.image = photo1
        photoLabel1.grid(row=1,column=0,rowspan=2,columnspan=2,sticky=W)
        
        #음식사진
        keyStr = "F"+str(key)
        photo4=tk.PhotoImage(file=sheet[keyStr].value)
        photoLabel4 = tk.Label(self, image=photo4)
        photoLabel4.image = photo4
        photoLabel4.grid(row=1,column=2,rowspan=3,columnspan=3,sticky=W)

        #전화번호
        keyStr = "E"+str(key)
        photo3=tk.PhotoImage(file=sheet[keyStr].value)
        photoLabel3 = tk.Label(self, image=photo3)
        photoLabel3.image = photo3
        photoLabel3.grid(row=3,column=1)

        #맛집 라벨 정보
        keyStr = "B"+str(key)
        li.append(keyStr)

        #인근주소
        keyStr = "D"+str(key)
        
        if sheet[keyStr].value == "정문도보5분":
            keyStr = "정문도보5분.gif"
        elif sheet[keyStr].value == "정문도보3분":
            keyStr = "정문도보3분.gif"
        elif sheet[keyStr].value == "서문도보5분":
            keyStr = "서문도보5분.gif"
        elif sheet[keyStr].value == "서문도보3분":
            keyStr = "서문도보3분.gif"
        elif sheet[keyStr].value == "중문도보5분":
            keyStr = "중문도보5분.gif"
        elif sheet[keyStr].value == "중문도보3분":
            keyStr = "중문도보3분.gif"
        elif sheet[keyStr].value == "후문도보5분":
            keyStr = "후문도보5분.gif"
        elif sheet[keyStr].value == "후문도보3분":
            keyStr = "후문도보3분.gif"
        else :
            keyStr = "정문도보5분.gif"
 
        photo2=tk.PhotoImage(file=keyStr)
        photoLabel2 = tk.Button(self, image=photo2,command=PrintMessage)
        photoLabel2.image = photo2
        photoLabel2.grid(row=3,column=0)

if __name__ == "__main__":
    window = Samplewindow()
    window.geometry("1250x770")
    window.resizable(width=True, height=True)
    window.mainloop()
