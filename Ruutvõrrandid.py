from tkinter import*
from math import*
import matplotlib.pyplot as plt #для рисования диаграммы (графика)
import numpy as пр #создание точек, запоминает их
global D,t
D=-1
t="Ruut juurt puudub"
def lahenda():
    global a,b,c
    if (a.get()!="" and b.get()!="" and c.get()!=""): #проверяем чтобы поля были заполнены и не были равны пустоте
        #if type!=  #тут надо проверить тип вводимх данных
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            graf=True
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
            graf=True
        else:
            t="Ruut juurt puudub"
            graf=False
            a.configure(bg="Lightblue")
            b.configure(bg="Lightblue")
            c.configure(bg="Lightblue")
        vastus.configure(text=f"D={D}\n{t}")     
    else:
        t="Ruut juurt puudub"
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return graf,D,t
def grafik():
    graf,D,t=lahenda()
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x=пр.arange(x0-10, x0+10, 0.5) #mix max step
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y, "b:o")
        plt.title("Ruutvõrrand")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"Parabooli tipp ({x0},{y0})"
    else:
        text=f"Ei ole võimalusi teha graafikut"
    vastus.configure(text=f"D={D}\n{t}\n{text}")

aken=Tk() #создаем окно
aken.title("Ruutvõrrand")
aken.geometry("650x200")
#кнопка решения
lbl=Label(aken,text="Ruutvõrrandi lahendus",font="Calibri 26",fg="green",bg="Lightblue", justify=CENTER)
lbl.pack()
vastus=Label(aken,text="Lahendus",height=2,width=60,bg="yellow")
vastus.pack(side=BOTTOM)
lah=Button(aken,text="Lahenda",font="Calibri 26",fg="black",bg="green",relief=GROOVE, command=lahenda)
lah.pack(side=RIGHT)
grafik=Button(aken,text="Graafik",font="Calibri 26",fg="black",bg="green",relief=GROOVE, command=grafik)
grafik.pack(side=RIGHT)
a=Entry(aken,font="Calibri 26",fg="green",bg="Lightblue",width=3)
a.pack(side=LEFT)
x2=Label(aken,text="x**2+",font="Calibri 26",fg="green",padx=10)
x2.pack(side=LEFT)
b=Entry(aken,font="Calibri 26", fg="green",bg="lightblue",width=3)
b.pack(side=LEFT)
x=Label(aken,text="x+",font="Calibri 26", fg="green")
x.pack(side=LEFT)
c=Entry(aken,font="Calibri 26", fg="green",bg="lightblue",width=3)
c.pack(side=LEFT)
y=Label(aken,text="=0",font="Calibri 26", fg="green")
y.pack(side=LEFT)
#кнопка график


aken.mainloop()