import tkinter
vyska = 600
sirka = 800
canvas=tkinter.Canvas(bg='green', height = vyska, width = sirka)
canvas.pack()
from random import *

canvas.create_rectangle(sirka//4,vyska//4,sirka//4*3,vyska, fill='skyblue', outline='skyblue')

def mucha(x,y):
    r=randrange(4,8)
    canvas.create_line(x,y,x-r,y+r, width=3)
    canvas.create_line(x,y,x+r,y+r, width=3)

def ryba(x,y):
    farbaryba=choice(('blue','yellow','green'))
    s=randrange(8,15)
    canvas.create_oval(x,y-s,x+2*s,y+s, fill=farbaryba)
    canvas.create_line(x+2*s,y,x+3*s,y-s,x+3*s,y+s,x+2*s,y, width=2, fill=farbaryba)
    
def lekno(x,y):
    s=randrange(8,15)
    canvas.create_oval(x,y,x+2*s,y+2*s, fill='red')
    canvas.create_oval(x+0.5*s,y+0.5*s,x+1.5*s,y+1.5*s, fill='yellow')
    
def strom(x,y):
    t=randrange(8,14)
    canvas.create_rectangle(x,y,x+0.4*t,y+5*t,fill='brown')
    canvas.create_oval(x-2*t,y-4*t,x+2*t,y, fill='lightgreen')
    
def stromy(sur):
    x=sur.x
    y=sur.y 
    if 0<x<sirka//4 or sirka//4*3<x<sirka:
        strom(x,y)
    
    
    
def elko(sur):
    x=sur.x
    y=sur.y    
    if sirka//4<x<sirka//4*3 and vyska//4<y<vyska//2:
        lekno(x,y)

def lava(sur):
    x=sur.x
    y=sur.y
    if sirka//4<x<sirka//4*3 and vyska//2<y<vyska:
        ryba(x,y)
    else:
        mucha(x,y)
        

canvas.bind_all('l',elko)
canvas.bind('<Button-1>',lava)
canvas.bind('<Button-3>',stromy)

canvas.mainloop()
