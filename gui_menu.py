from tkinter import *
import random
import os
menulist = ['짜장면', '짬뽕', '탕수육','피자' ,'치킨','라면']

tk = Tk()
label = Label(tk,text='AI가 추천하는 메뉴') 
label.pack()

def event():
    menu = random.choice(menulist)
    button['text'] = f'{menu} 추천!'

button = Button(tk,text='추천메뉴',command=event)
# button2 = Button(tk,text='버튼2 입니다.')
button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
# button2.pack(side=LEFT, padx=10, pady= 10)
tk.mainloop()