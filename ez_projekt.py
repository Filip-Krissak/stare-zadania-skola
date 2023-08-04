from tkinter import *
from tkinter import messagebox
from tkinter import sys
vlajka = Tk()



def bahamy():
    vlajka.title('bahamy')
    canvas=Canvas(vlajka, height=300, width=600)
    canvas.create_rectangle(0,0,600,100, fill='cyan', outline='cyan')
    canvas.create_rectangle(0,200,600,300, fill='cyan', outline='cyan')
    canvas.create_rectangle(0,100,600,200, fill='yellow', outline='yellow')
    canvas.create_polygon(0,0,250,150,0,300)
    canvas.pack()

def kuba():
    vlajka.title('kuba')
    canvas=Canvas(vlajka, height=250, width=500)
    canvas.create_rectangle(0,0,500,50, fill='mediumblue', outline='mediumblue')
    canvas.create_rectangle(0,50,500,100, fill='white', outline='white')
    canvas.create_rectangle(0,100,500,150, fill='mediumblue', outline='mediumblue')
    canvas.create_rectangle(0,150,500,200, fill='white', outline='white')
    canvas.create_rectangle(0,200,500,250, fill='mediumblue', outline='mediumblue')
    canvas.create_polygon(0,0,200,125,0,250, fill='red', outline='red')
    canvas.pack()
    
def kuwait():
    vlajka.title('kuwait')
    canvas=Canvas(vlajka, height=300, width=500)
    canvas.create_rectangle(0,0,500,100, fill='green', outline='green')
    canvas.create_rectangle(0,100,500,200, outline='white', fill='white')
    canvas.create_rectangle(0,200,500,300, outline='darkred', fill='darkred')
    canvas.create_polygon(0,0,100,100,100,200,0,300)
    canvas.pack()
    
    
    

vyber = input('Akú vlajku chcete vykresliť: bahamy/kuba/kuwait: ').lower()

if vyber == 'bahamy':
    bahamy()
elif vyber == 'kuba':
    kuba()
elif vyber == 'kuwait':
    kuwait()
else:
    
    if messagebox.showerror('ERROR', vyber + ' nie je jedna z možností'):
        sys.exit()
    else:
        sys.exit()




vlajka.mainloop()


