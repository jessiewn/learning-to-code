from tkinter import *
import tkinter



def add(*args):
    sum=0
    for n in args:
        sum+=n
    print(sum)

#add(1,2,3,4,5)
        
def calculate(n,**kwargs):
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

#calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kw) -> None:
        self.make=kw["make"]
        self.model=kw["model"]
my_car=Car(make="Nissan",model="GT")
#print(my_car.model)
window=tkinter.Tk()
window.minsize(width=500,height=300)
#label
my_label=Label(text="my text",font=("Arial",24,"bold"))
my_label.pack()
#button
def button_clicked():
    print("I got clicked")
    my_label.config(text=f"{input.get()}",font=("Arial",24,"bold"))


#Entry

input=Entry(width=10)
input.pack()
button=Button(text="click me",command=button_clicked)
button.pack()







window.mainloop()