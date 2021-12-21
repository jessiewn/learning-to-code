from tkinter import*
import tkinter

window=tkinter.Tk()
window.title("Miles to kilometers Converter")
window.minsize(width=200,height=200)

#label
my_label=tkinter.Label(text="Miles")
my_label.grid(column=2,row=0)
my_label1=tkinter.Label(text="is equal to")
my_label1.grid(column=0,row=1)
my_label2=tkinter.Label(text="Km")
my_label2.grid(column=2,row=1)
my_label3=tkinter.Label()
my_label3.grid(column=1,row=1)


#button
def button_clicked():
    miles=int(input.get())
    km=miles*1.61
    print("I got clicked")
    my_label3.config(text=f"{km}")
button=Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)


#Entry

input=Entry(width=10)
input.grid(column=1,row=0)












window.mainloop()
