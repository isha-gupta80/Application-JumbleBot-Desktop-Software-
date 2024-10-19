import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle
 
answer = ["America","India","Australia"]

questions = []

for i in answer:
    words = list(i)
    shuffle(words)
    questions.append(words)
    
num = random.randint(0,len(questions)-1)

def initial():
    global questions,num
    lb1.configure(text=questions[num])
    
def answercheck():
    global questions, num ,answer
    userinput = e1.get()
    if userinput == answer[num]:
        messagebox.showinfo('success','your answer was correct') 
    else:
        messagebox.showinfo('Error','your answer is wrong')
        e1.delete(0,END)

def resetswitch():
    global questions,answers, num 
    num = random.randint(0,len(questions)-1)
    lb1.configure(text=questions[num])
    e1.delete(0,END)


window = Tk()
window.geometry("300x300")
window.configure(background='#30336B')
window.title("JumbleBot")
window.iconbitmap('icon.ico')
 
lb1 = Label(window,font='times 20',bg='#586776',fg='#EA7773')
lb1.pack(pady=30, ipady=10, ipadx=10)

answers = StringVar  () 
e1 = Entry(window, textvariable=answer)
e1.pack(ipady=5, ipadx=5)

button1 = Button(window , text="check",bg='#586776', width=20,command=answercheck)
button1.pack(pady=40)

button2 = Button(window , text="Reset",bg='#586776', width=20,command=resetswitch)
button2.pack()

    
initial() 
window.mainloop()
