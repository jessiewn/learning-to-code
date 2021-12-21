import math

import tkinter


timer=None
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_TIME = 5
SHORT_BREAK_TIME = 1
LONG_BREAK_TIME = 3
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    checkmark.config(text="")
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_TIME
    short_break_sec=SHORT_BREAK_TIME
    long_break_sec=LONG_BREAK_TIME
 
    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work")
       
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_seconds=round(count%60,2)
    
    if count_seconds<10:
        count_seconds=f"0{count_seconds}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_seconds}")

    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✓"
            checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW,highlightthickness=0)

canvas=tkinter.Canvas(width=200,height=224,bg=YELLOW)
tomato_img=tkinter.PhotoImage(file="100_day_course/day_28/pomodoro-start/tomato.png")
canvas.create_image(103,112,image=tomato_img)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


timer_label=tkinter.Label(text="Timer",font=(FONT_NAME,45,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)

start_button=tkinter.Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=tkinter.Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

checkmark=tkinter.Label(font=(FONT_NAME,20,"bold"),fg=GREEN,bg=YELLOW)
checkmark.grid(column=1,row=4)



window.mainloop()