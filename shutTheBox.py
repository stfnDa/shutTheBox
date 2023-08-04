from tkinter import *
import random

darkBrown = "#723E03"
lightBrown = "#E6AB67"

def f1():
    i = 0
    fieldBtns(i)
def f2():
    i = 1
    fieldBtns(i)
def f3():
    i = 2
    fieldBtns(i)
def f4():
    i = 3
    fieldBtns(i)
def f5():
    i = 4
    fieldBtns(i)
def f6():
    i = 5
    fieldBtns(i)
def f7():
    i = 6
    fieldBtns(i)
def f8():
    i = 7
    fieldBtns(i)
def f9():
    i = 8
    fieldBtns(i)

def checkAnzahl():
    anzahl = 0
    for i in range(9):
        if (f[i].cget("bg") == "white"):
            anzahl = anzahl + 1
    return anzahl

def fieldBtns(i):
    anzahl = checkAnzahl()
    if (startButton.cget("text") == "Restart"):
        if(f[i].cget("fg") == darkBrown):
                if (anzahl <= 1):
                    f[i].config(bg = "white", fg = "black")
        elif(f[i].cget("bg") == "white"):
             f[i].config(bg = lightBrown, fg = darkBrown)      
def confirm():
    dices = int(d1.cget("text")) + int(d2.cget("text"))
    if(startButton.cget("text") == "Restart"):
        fields = 0
        for i in range(9):
            if(f[i].cget("bg") == "white"):
                fields = fields + i + 1
        if(fields == dices):
            for i in range(9):
                if(f[i].cget("bg") == "white"):
                    f[i].config(fg = lightBrown, bg=lightBrown)
            if(win() == False):       
                Roll()
            else:
                won.config(fg="red")    
def win():
    win = True
    for i in range(9):
        if(f[i].cget("fg") != lightBrown):
            win = False
    return win        

#würfeln
def Roll():
    dice = [1, 2, 3, 4, 5, 6]
    d1.config(text = random.choice(dice))
    d2.config(text = random.choice(dice))
    dices = int(d1.cget("text")) + int(d2.cget("text"))
    #possible:
    p = False
    for i in range(9):
        x = i + 1
        if(f[i].cget("fg") == darkBrown):
            if (x == dices):
                p = True
            else:
                for j in range(9):
                    y = j + 1
                    if(f[j].cget("fg") == darkBrown):
                        if (x != y):
                            if(x + y == dices):
                                p = True
    if(p == False):
        won.config(text="You \nlost!", fg="red")                         

def main():
    startButton.config(text="Restart")
    Roll()
    for i in range(9):
        f[i].config(bg=lightBrown, fg=darkBrown)
    won.config(fg="#8FD4B2") 

window = Tk()
window.geometry("800x600") #size lenght and height
window.title("Shut The Box") #text at the top

stbPhoto = PhotoImage(file="E:\\vsCodePython\\sTB\\shutTheBoxImage.png")
label = Label(window, 
              image=stbPhoto,)
label.place(relx=0.99, rely=0.01, anchor="ne")

#start and confirm button
startButton = Button(window,
                     text="Start",
                     font=("Arial", 20),
                     padx="50",
                     relief="ridge",
                     borderwidth=0.5,
                     command=main,
                     bg="#5ADA9B",
                     )
startButton.place(relx=0.1, rely=0.93, anchor="sw")

confirmButton = Button(window,
                       text="Confirm",
                       font=("Arial", 20),
                       padx="40",
                       relief="ridge",
                       borderwidth=0.5,
                       command=confirm,
                       bg="#5ADA9B")
confirmButton.place(relx=0.5, rely=0.75, anchor="center")

#board buttons
top = Frame(window)
top.place(relx = 0.5, rely = 0.55, anchor="center")
myFncs = [f1, f2, f3, f4, f5, f6, f7, f8, f9]
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = {}
for i in range(9):
    f[i] = Button(window,
            text=board[i],
            font=("Arial", 35),
            fg=darkBrown,
            bg=lightBrown,
            command= myFncs[i])
    f[i].pack(in_=top, side=LEFT)

#dices
canvas = Canvas(window,
                width=400,
                height=200,
                bg="white")
canvas.place(relx=0.06, rely=0.03, anchor="nw")
canvas.create_rectangle(25,25,175,175, fill=lightBrown, outline=darkBrown, width=2)
canvas.create_rectangle(225,25,375,175, fill=lightBrown, outline=darkBrown, width=2)

d1 = Label(window, text="", font=("Arial", 50), bg=lightBrown, fg=darkBrown)
d1.place(relx=0.187, rely=0.2, anchor="center")
d2 = Label(window, text="", font=("Arial", 50), bg=lightBrown, fg=darkBrown)
d2.place(relx=0.436, rely= 0.2, anchor="center")

won = Label(window,
            text="You \nwon!",
            font=("Arial", 59, "bold"),
            fg="#8FD4B2",
            bg="#8FD4B2")   
won.place(relx=0.95, rely=0.97, anchor="se")

window.config(bg="#8FD4B2")
window.mainloop() #show window, listen events