from tkinter import *
from tkinter import messagebox 

window = Tk()

window.title("CARDIOVASCULAR SYMPTOMS")
window.geometry("400x400")
window.config(background="IndianRed1")

answer_1 = StringVar(value="0")
q1 = Label(window,text="Do you experience shortness of breath during routine activites")
q1.pack()
q1_r1 = Radiobutton(window,text="YES",variable=answer_1,value="YES")
q1_r1.pack()
q1_r2 = Radiobutton(window,text="NO",variable=answer_1,value="NO")
q1_r2.pack()


answer_2 = StringVar(value="0")
q2 = Label(window,text="Do you get a pain/shooting pain in the heart?")
q2.pack()
q2_r1 = Radiobutton(window,text="YES",variable=answer_2,value="YES")
q2_r1.pack()
q2_r2 = Radiobutton(window,text="NO",variable=answer_2,value="NO")
q2_r2.pack()


answer_3 = StringVar(value="0")
q3 = Label(window,text="Do you start sweating a lot?")
q3.pack()
q3_r1 = Radiobutton(window,text="YES",variable=answer_3,value="YES")
q3_r1.pack()
q3_r2 = Radiobutton(window,text="NO",variable=answer_3,value="NO")
q3_r2.pack()

answer_4 = StringVar(value="0")
q4 = Label(window,text="Are you uneasy while taking a breath")
q4.pack()
q4_r1 = Radiobutton(window,text="YES",variable=answer_4,value="YES")
q4_r1.pack()
q4_r2 = Radiobutton(window,text="NO",variable=answer_4,value="NO")
q4_r2.pack()

answer_5 = StringVar(value="0")
q5 = Label(window,text="Do you experience shortness of breath while sitting/laying down?")
q5.pack()
q5_r1 = Radiobutton(window,text="YES",variable=answer_5,value="YES")
q5_r1.pack()
q5_r2 = Radiobutton(window,text="NO",variable=answer_5,value="NO")
q5_r2.pack()

def heart():
    score = 0
    if(answer_1.get()=="YES"):
        score = score+10

    if(answer_2.get()=="YES"):
        score = score+10

    if(answer_3.get()=="YES"):
        score = score+10
    if score == 50:
        messagebox.showinfo("Report","You should strongly visit a doctor")
    elif score == 40:
        messagebox.showinfo("Report","You should strongly visit a doctor")  
    elif score == 30:
        messagebox.showinfo("Report","You perhaps need to visit a doctor")
    elif score == 20:
        messagebox.showinfo("Report","You perhaps need to visit a doctor")  
    else:
        messagebox.showinfo("Report","You don't need to visit a doctor")  





btn_click = Button(window,text="Click Me!",command=heart)
btn_click.pack()


window.mainloop()