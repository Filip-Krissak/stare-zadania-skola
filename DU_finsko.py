import tkinter
from random import*
sirka=800
vyska=500
canvas=tkinter.Canvas(width=sirka,height=vyska,bg="gray")
canvas.pack()

def stvorec(suradnice):
    x=suradnice.x
    y=suradnice.y
    r=7
    def s(farba):
        canvas.create_rectangle(x,y,x+4*r,y+4*r,w=0,fill=farba)
    

    if 210<x<340 or 185<y<315:
        s('blue')

    else:
        s('white')

        
canvas.bind('<B1-Motion>',stvorec)
