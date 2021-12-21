from tkinter import*
import tkinter

window=tkinter.Tk()
window.title("my first GUI program")
window.minsize(width=500,height=300)

#label
my_label=tkinter.Label(text="I am a label",font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)

#button
def button_clicked():
    print("I got clicked")
    my_label.config(text=f"{input.get()}",font=("Arial",24,"bold"))
button=Button(text="click me",command=button_clicked)
button.grid(column=1,row=1)
new_button=Button(text="click me",command=button_clicked)
new_button.grid(column=2,row=0)

#Entry

input=Entry(width=10)
input.grid(column=3,row=2)












window.mainloop()
