import tkinter as tk
from random import randint
from math import sin,cos,radians

# -------- constanty ----------

niecodivne = 10

sirka = 600
vyska = 500
bg = "white"

vyskamuru = 200
velkostmedzery = 20
sirkamedzery = 20
vyskamedzery = 25
farbamuru = "brown"

odstupbrany = 10
vyskabrany = 75
sirkabrany = 150

texttlacidla1 = "TREEEEEEEES"
odstupstromov = sirkabrany
vyskastromov = 50
pocetkonarov = 5
dlzkakonarov = 10
uholkonarov = -35
farbastromu = "green"
hrubkastromu = 2

texttlacidla2 = "START"
maxrychlost = 5
velkosttick = 1
sancazakopnutia = 1000
zrychlenierytiera = 20
velkostpanaka = 20
farbarytiera = "green"
farbahraca = "red"
uholnoh = 5
uholruk = 25
tagrytiera = "ryt"
taghraca = "hrac"
krok = 1/100

farbaokna = "blue"
FPS = 100//3

# -------- preddefinovane premenne -------

rychlostrytiera = 100
rychlosthraca = 0
pozryt = (sirka-40,vyska-20)
pozhrac = (sirka-120,vyska-20)

# -------- funkcie -------

def panak(x,y,farba,tagl):
    v = velkostpanaka
    stvorec(x-v/2,y-v,v,v*1.5,farba,tagl)
    c.create_line(x-v/4,y+v/2,x-v/4+cos(radians(90+uholnoh))*v,y+v/2+sin(radians(90+uholnoh))*v,width=v/3,fill=farba,tags=tagl)
    c.create_line(x+v/4,y+v/2,x+v/4+cos(radians(90-uholnoh))*v,y+v/2+sin(radians(90-uholnoh))*v,width=v/3,fill=farba,tags=tagl)
    c.create_line(x-v/2,y-v,x-v/2+cos(radians(90+uholruk))*v,y-v+sin(radians(90+uholruk))*v,width=v/3,fill=farba,tag=tagl)
    c.create_line(x+v/2,y-v,x+v/2+cos(radians(90-uholruk))*v,y-v+sin(radians(90-uholruk))*v,width=v/3,fill=farba,tag=tagl)
    kruh(x,y-v-v/2,v/2,farba,tagl)
    

def but():
    x,y = randint(0,sirka-odstupstromov),randint(vyskamuru+vyskastromov,vyska)
    c.create_line(x,y,x,y-vyskastromov,fill=farbastromu,width=hrubkastromu)
    for i in range(pocetkonarov):
        y = y-(vyskastromov/pocetkonarov)
        c.create_line(x,y,x+cos(radians(0-uholkonarov))*dlzkakonarov,y+sin(radians(0-uholkonarov))*dlzkakonarov,fill=farbastromu,width=hrubkastromu)
        c.create_line(x,y,x+cos(radians(180+uholkonarov))*dlzkakonarov,y+sin(radians(180+uholkonarov))*dlzkakonarov,fill=farbastromu,width=hrubkastromu)


def kruh(x,y,r,farba,tag):
    c.create_oval(x-r, y-r, x+r, y+r,outline=farba,fill=farba,tag=tag)

def stvorec(x,y,sirka,vyska,farba,tag):
    c.create_rectangle(x,y,x+sirka,y+vyska,outline=farba,fill=farba,tag=tag)

def clic(sur):
    x,y = sur.x,sur.y
    velkost = entry.get()
    if velkost == "":
        print("Ty tupak najprv musis napisat ako velke chces to okno")
    
    else:
        velkost = int(velkost)
        if velkost/2+vyskamedzery < y < vyskamuru-velkost and x < sirka - sirkabrany - velkost:
            kruh(x,y,velkost/2,farbaokna,None)
            stvorec(x-velkost/2,y,velkost,velkost,farbaokna,None)


def rytierpohyb():
    rychlost = rychlostrytiera
    c.move(tagrytiera,0,-rychlost*krok)
    c.after(FPS,rytierpohyb)
    


def hracpohyb():
    global rychlosthraca
    zrychlenie = int(slider.get())
    rychlosthraca += zrychlenie
    if randint(0,100) < zrychlenie:
        rychlosthraca = 0
        print("do rici")
    c.move(taghraca,0,-rychlosthraca*krok)
    c.after(FPS,hracpohyb)


def start():
    rytierpohyb()
    hracpohyb()
    
# ------ definovanie vystupnych blbosti -------

c = tk.Canvas(width=sirka,height= vyska,background=bg)
c.pack()

button = tk.Button(text=texttlacidla1, command=but)
button.pack()

button = tk.Button(text=texttlacidla2, command=start)
button.pack()

entry = tk.Entry()
entry.pack()

a = tk.Canvas(width=sirka,height= vyska,background=bg)
a.pack()
slider = tk.Scale(a, from_=0,length=sirka,tickinterval=velkosttick, to=maxrychlost,orient="horizontal")
slider.pack()

# ------- vykreslenie pozadia ---------

stvorec(0,vyskamedzery,sirka+niecodivne,vyskamuru-vyskamedzery,farbamuru,None)
for i in range(sirka//(velkostmedzery+sirkamedzery)+1):
    stvorec(i*(velkostmedzery+sirkamedzery)-sirkamedzery/2,0,sirkamedzery,vyskamedzery,farbamuru,None)

stvorec(sirka-odstupbrany-sirkabrany,vyskamuru-vyskabrany,sirkabrany,vyskabrany,bg,None)
kruh(sirka-sirkabrany/2-odstupbrany,vyskamuru-vyskabrany,sirkabrany/2,bg,None)

panak(pozryt[0],pozryt[1],farbarytiera,tagrytiera)
panak(pozhrac[0],pozhrac[1],farbahraca,taghraca)

c.bind('<Button>', clic)
tk.mainloop()