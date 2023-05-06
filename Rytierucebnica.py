import tkinter
from random import *
canvas = tkinter.Canvas(width=610,height=400,bg='white')
canvas.pack()

def hradby():
    canvas.create_rectangle(10,10,610,200,fill='brown',outline='')
    for i in range(1,31):
        canvas.create_rectangle(i*20,10,i*20+10,20,fill='white',outline='white')
    canvas.create_rectangle(500,100,600,200,fill='white',outline='')
    canvas.create_oval(500,50,600,150,fill='white',outline='')
    
def okno(suradnice):
    x = suradnice.x
    y = suradnice.y
    vyska = int(entry1.get())
    if x>10 and x<480 and y+vyska<200 and y>30:
        canvas.create_rectangle(x,y,x+20,y+vyska,fill='blue',outline='')
    canvas.create_oval(x,y-10,x+20,y+41,fill='blue',outline='')

def strom():
    x=randrange(480)
    y=randint(210,330)
    canvas.create_line(x,y,x,y+70,fill='green')
    for i in range(1,8):
        canvas.create_line(x-10,y+i*10,x,y+i*10-10,x+10,y+i*10,fill='green')


def rytier(x,y):
    canvas.create_oval(x-5,y-10,x+5,y,tags='rytier')
    canvas.create_rectangle(x-5,y,x+5,y+20,tags='rytier')
    canvas.create_rectangle(x-3,y+20,x+3,y+40,tags='rytier')

def spracuj_tipovanie(vyhral,tip):
    if tip==vyhral:
        canvas.create_text(550,350,text='dobrý tip')
    else:
        canvas.create_text(550,350,text='zlý tip')
def animuj():
    global rytier1, rytier2
    canvas.delete('rytier')
    rytier1 = rytier1 - randint(0,10)
    rytier2 = rytier2 - randint(0,10)
    rytier(520,rytier1)
    rytier(570,rytier2)
    if rytier1<200 or rytier2<200:
        if rytier1<rytier2:
            canvas.create_text(550,300,text='1')
            vyhral=1
        else:
            canvas.create_text(550,300,text='2')
            vyhral=2
        spracuj_tipovanie(vyhral,tip)
    else:
        canvas.after(100,animuj)
        
def tip1():
    global tip
    if tip==0:
        tip=1
        animuj()
        
def tip2():
    global tip
    if tip==0:
        tip=2
        animuj()
        
rytier1=350
rytier2=350
tip=0
hradby()
canvas.bind('<Button-1>',okno)
entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='strom',command=strom)
button1.pack()
button2 = tkinter.Button(text='Tipujem 1',command=tip1)
button2.pack()
button3 = tkinter.Button(text='Tipujem 2',command=tip2)
button3.pack()

canvas.mainloop()