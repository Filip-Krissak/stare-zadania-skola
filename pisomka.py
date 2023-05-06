#Filip Kriššák
import tkinter
from random import *
vyska = 600
sirka = 800

canvas = tkinter.Canvas(width = sirka, height = vyska, bg = "white")
canvas.pack()

medzera = 30
def hradba():
    x = 0
    y = 0
    for i in range(30):
        canvas.create_rectangle(x,y,x+10,y+medzera, fill='brown', outline='brown')
        x=x+medzera
hradba()
canvas.create_rectangle(0,30,800,260,fill='brown',outline='brown')

def strom():
    vyskastromu = 100
    x = randint(0,sirka//3*2)
    y = randint(270,vyska)
    canvas.create_line(x,y,x,y-vyskastromu,fill = 'green', width=3)
    for i in range(5):
        y= y - (vyskastromu/5)
        canvas.create_line(x,y,x+(vyskastromu/5),y+(vyskastromu/5),fill='green', width = 3)
        canvas.create_line(x,y,x-(vyskastromu/5),y+(vyskastromu/5),fill='green', width = 3)

def rytier(x,y,r):
    canvas.create_oval(x-r,y,x+r,y+2*r,outline='green',fill='white',tags='rytier')
    canvas.create_rectangle(x-r,y+2*r,x+r,y+5*r,outline='green',fill='white',tags='rytier')
    canvas.create_rectangle(x-0.5*r,y+5*r,x+0.5*r,y+8*r,outline='green',fill='white',tags='rytier')


def start():
    global rytier1, rytier2
    canvas.delete('rytier')
    rytier1 = rytier1 - randrange(10)
    rytier2 = rytier2 - randrange(10)
    rytier(640,rytier1,10)
    rytier(690,rytier2,10)
    if rytier1 < 200 or rytier2 < 200:
        if rytier1<rytier2:
            canvas.create_text(680, 400,text = 'vyhral 1 ')
        else:
            canvas.create_text(680, 400,text = 'vyhral 2 ')
    else:
        canvas.after(50,start)


canvas.create_oval(600,60,750,210, fill='white', outline='white')
canvas.create_rectangle(600,135,750,260, fill='white', outline='white')

button2 = tkinter.Button(text='start',command = start)
button2.pack()
rytier1 = 450
rytier2 = 450
button1 = tkinter.Button(text='strom',command = strom)
button1.pack()
canvas.mainloop()
        