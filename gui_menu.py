
from tkinter import *
import random

menu = ["짜장", "짬뽕", "라면", "김밥", "돈까스"]

def pressed(): # 버튼 클릭 이벤트
    foodname = random.choice(menu)
    msg = "오늘의 메뉴는 {}".format(foodname)
    label.configure(text=msg)
    img = PhotoImage(file='{}.png'.format(foodname)) #이미지 읽고
    lbl = Label(image=img) #이미지 넣어
    lbl.image = img  # 레퍼런스 추가
    lbl.grid(column=0, row=2)
    # lbl.pack()

root = Tk()
root.title("오늘 머 먹지?")
root.geometry("540x380")

btn1 = Button(root, text="추천메뉴", command=pressed)
btn1.grid(column=0, row=0)
# btn1.pack()

label = Label(root, text="두구 두구", font=("돋음", 10))
label.grid(column=0, row=1)

root.mainloop()