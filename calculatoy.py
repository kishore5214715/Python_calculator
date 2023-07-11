import tkinter
from tkinter import *

value_eqe = ""

def show(value):
    global value_eqe
    value_eqe+=value
    result.config(text=value_eqe)

def clear():
    global value_eqe
    value_eqe=""
    result.config(text=value_eqe)

def claculate():
    global value_eqe
    fin_res=""
    if value_eqe != "":
        try:
            fin_res=eval(value_eqe)
        except:
            fin_res="Error check you input \n Try again"
        
        result.config(text=fin_res)


def _onestep_():
    global value_eqe
    l=len(value_eqe)
    value_eqe=value_eqe[:l-1]
    result.config(text=value_eqe)


window=Tk()
window.title("Calculator")
window.geometry("565x600")

result=Label(window,width=25,height=2,text="",font=("arial",30))
result.pack()

Button(window,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: clear()).place(x=1,y=100)
Button(window,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("/")).place(x=150,y=100)
Button(window,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("%")).place(x=290,y=100)
Button(window,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("*")).place(x=430,y=100)

Button(window,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("1")).place(x=1,y=200)
Button(window,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("2")).place(x=150,y=200)
Button(window,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("3")).place(x=290,y=200)
Button(window,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("-")).place(x=430,y=200)

Button(window,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("4")).place(x=1,y=300)
Button(window,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("5")).place(x=150,y=300)
Button(window,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("6")).place(x=290,y=300)
Button(window,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("+")).place(x=430,y=300)

Button(window,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("7")).place(x=1,y=400)
Button(window,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("8")).place(x=150,y=400)
Button(window,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("9")).place(x=290,y=400)
Button(window,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show(".")).place(x=430,y=400)


Button(window,text="0",width=10,height=1,font=("arial",30,"bold"),bd=1,command=lambda: show("0")).place(x=1,y=500)
Button(window,text="=",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda: claculate()).place(x=430,y=500)
Button(window,text="OS",width=5,height=1,font=("arial",30,"bold"),bd=1,command=lambda:_onestep_()).place(x=290,y=500)


window.mainloop()