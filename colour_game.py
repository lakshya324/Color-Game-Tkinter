#by Lakshya (Documantaion/Instructions completed)
    #Created on:     3/may/2023 5:34pm 
    #Last update on: 3/may/2023 7:46pm 

#TODO (Lack of Time)
    #Use Time
    #Include Reset after lossing
    #Winnig Song or message on winning
    #impove GUI apperances

from tkinter import *
from tkinter import messagebox as tm
import time
from random import choice


def check(notimp=0):
    #this Function will check weither colour you type is correct or not
    global cc , score
    
    colour_guess=True

    if colour_guess==True:#no previous mistake
        print(cc)
        if i.get()==cc:#input is correct or not
            i.set("")
            score=score+1
            score_out.set(f"Score is: {score}")
            cc=choice(colour)
            s1.config(fg=cc)
            cname.set(choice(colour).upper())
            root.update()
        else:#input is wrong
            colour_guess==False
            if score>maxscore:#user score is greater then max score or not
                if tm.askyesno("You Lose","Conglaturation!\nYou Make a new Max Score\nDo you want to Save?")==1:
                    with open(file,"w")as f:
                        f.write(str(score))
                root.mainloop()
            else:
                tm.showerror("Wrong Colour",f"You Lose\nColur is {cc}")
            


#MAIN PROGRAM

root=Tk()
root.geometry("480x480")
root.minsize(240,240)
root.maxsize(960,960)
root.config(bg="white")
root.title("Colour Game -By Lakshya")
root.wm_iconbitmap("Workshop Project\colour game\gamecontroller.ico")
colour=["black","blue","pink","red","green","yellow","purple"]


#score and max score declaration
score=0
file="Workshop Project\colour game\maxscore.txt"
try:
    with open(file,"r")as f:
        maxscore=int(f.read())
    # maxscore_file=open(file,"r")
    # maxscore_file.close()
except:
    tm.showerror('Max List Error', 'Error: Max list not found or contain not int value')


#output of max score and score
score_out=StringVar()
score_out.set(f"Score is: {score}")
maxscore_out=StringVar()
maxscore_out.set(f"Max Score is: {maxscore}")


i=StringVar()

#colour changing text 
cname=StringVar()
cname.set(choice(colour).upper())
cc=choice(colour)

Label(root,textvariable=StringVar(value="Which colour is this?"),font=("",20,"bold"),background="Black",foreground="white",relief=RAISED).pack(fill=X)
Label(root,textvariable=maxscore_out,font=("",15,"bold"),background="white").pack(pady=1)
Label(root,textvariable=score_out,font=("",15,"bold"),background="White").pack(pady=1)

Label(root,text="",font=("",5),background="white").pack(pady=15,fill=X)#spacing
s1=Label(root,textvariable=cname,font=("Helvetica",50,"bold"),foreground=cc,background="white")
s1.pack(pady=5)


Entry(root,textvariable=i,font=("",15,"bold"),background="white",bd=5,justify="center").pack(pady=15,padx=5)

Button(root,text="Click Here",relief=RAISED,command=check,font=("",20,"bold"),background="red",fg="yellow",bd=10).pack(side=BOTTOM,fill=X)

root.bind("<Return>",check)#enter button is bind with program

root.mainloop()