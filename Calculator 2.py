from tkinter import *
import math
import tkinter.messagebox
root=Tk()
root.title("Scientific Calculator")
root.geometry("700x450")
switch=None
def btn_1():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'1')
def btn_2():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'2')
def btn_3():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'3')
def btn_4():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'4')
def btn_5():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'5')
def btn_6():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'6')
def btn_7():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'7')
def btn_8():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'8')
def btn_9():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'9')
def btn_0():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'0')
def btn_p():
    pos=len(disp.get())
    disp.insert(pos,'+')
def btn_m():
    pos=len(disp.get())
    disp.insert(pos,'-')
def btn_ml():
    pos=len(disp.get())
    disp.insert(pos,'*')
def btn_di():
    pos=len(disp.get())
    disp.insert(pos,'/')
def sin():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.sin(math.radians(ans))
        else:
            ans=math.sin(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def cos():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.cos(math.radians(ans))
        else:
            ans=math.cos(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def tan():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.tan(math.radians(ans))
        else:
            ans=math.tan(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def asin():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.asin(math.radians(ans))
        else:
            ans=math.asin(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def acos():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.acos(math.radians(ans))
        else:
            ans=math.acos(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def atan():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.atan(math.radians(ans))
        else:
            ans=math.atan(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def bl():
    pos=len(disp.get())
    disp.insert(pos,'(')
def log():
    try:
        ans=float(disp.get())
        ans=math.log10(ans)
        disp.delete(0,END)
        disp.insert(0,ans)
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def ln():
    try:
        ans=float(disp.get())
        ans=math.log(ans)
        disp.delete(0,END)
        disp.insert(0,ans)
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def round():
    try:
        ans=float(disp.get())
        ans=round(ans)
        disp.delete(0,END)
        disp.insert(0,ans)
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def sqrt():
    try:
        ans=float(disp.get())
        ans=math.sqrt(ans)
        disp.delete(0,END)
        disp.insert(0,ans)
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def fact():
    try:
        ans=float(disp.get())
        ans= math.factorial(ans)
        disp.delete(0,END)
        disp.insert(0,ans)
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def eq():
    try:
        ans=disp.get()
        ans=eval(ans)
        disp.delete(0,END)
        disp.insert(0,ans)
    except Exception:
        tkinter.messagebox.showerror("Value Error! Check your operator and operatand")
def bl():
    pos=len(disp.get())
    disp.insert(pos,'(')
def br():
    pos=len(disp.get())
    disp.insert(pos,')')
def cl():
    pos=len(disp.get())
    disp.delete(0,END)
    disp.insert(pos,'0')
def mod():
    pos=len(disp.get())
    disp.insert(pos,'%')
def pow():
    pos=len(disp.get())
    disp.insert(pos,'**')
def dot():
    pos=len(disp.get())
    disp.insert(pos,'.')
def btn_pi():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,str(math.e))
def btn_ex():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,str(math.e))
def back():
    pos=len(disp.get())
    display=str(disp.get())
    if display=='':
        disp.insert(0,'0')
    elif display==' ':
        disp.insert(0,'0')
    elif display=='0':
        pass
    else:
        disp.delete(0,END)
        disp.insert(0,display[0:pos-1])
def conv():
    global switch
    if switch is None:
        conv['text'] = 'DEG'
    else:
        conv['text'] = 'RAD'
disp=Entry(root, font="Elephant 18", fg="Black", bg="lightpink", bd=12, justify=RIGHT)
disp.insert(0,"0")
disp.pack(expand=True, fill=BOTH)
btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill=BOTH)
pibtn = Button(btnrow1, text="π", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_pi, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
sqrtbtn = Button(btnrow1, text="√x", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=sqrt, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
sinh_btn = Button(btnrow1, text="sin-1", font="Helvetica 16 bold", relief=GROOVE, bd=2, command=asin, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
cosh_btn = Button(btnrow1, text="cos-1", font="Helvetica 16 bold", relief=GROOVE, bd=2, command=acos, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
tanh_btn = Button(btnrow1, text="tan-1", font="Helvetica 16 bold", relief=GROOVE, bd=2, command=atan, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btn1 = Button(btnrow1, text="1", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_1, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btn2 = Button(btnrow1, text="2", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_2, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btn3 = Button(btnrow1, text="3", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_3, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btnp = Button(btnrow1, text="+", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_p, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btnrow2 = Frame(root, bg="#000000")
btnrow2.pack(expand=True, fill=BOTH)
e_btn = Button(btnrow2, text="e", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_ex, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
fact_btn = Button(btnrow2, text="x!", font="Helvetica 18 bold", relief=GROOVE, bd=2, command=fact, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
sin_btn = Button(btnrow2, text="sin", font="Helvetica 17 bold", relief=GROOVE, bd=2, command=sin, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
cos_btn = Button(btnrow2, text="cos", font="Helvetica 17 bold", relief=GROOVE, bd=2, command=cos, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
tan_btn = Button(btnrow2, text="tan", font="Helvetica 17 bold", relief=GROOVE, bd=2, command=tan, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btn4 = Button(btnrow2, text="4", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_4, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btn5 = Button(btnrow2, text="5", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_5, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btn6 = Button(btnrow2, text="6", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_6, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btnm = Button(btnrow2, text="-", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_m, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btnrow3 = Frame(root, bg="#000000")
btnrow3.pack(expand=True, fill=BOTH)
pow_btn = Button(btnrow3, text="x^y", font="Helvetica 18 bold", relief=GROOVE, bd=2, command=pow, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
log_btn = Button(btnrow3, text="log", font="Helvetica 18 bold", relief=GROOVE, bd=2, command=log, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
ln_btn = Button(btnrow3, text="ln", font="Helvetica 18 bold", relief=GROOVE, bd=2, command=ln, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
round_btn = Button(btnrow3, text="round", font="Helvetica 14 bold", relief=GROOVE, bd=2, command=round, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
conv_btn = Button(btnrow3, text="RAD", font="Helvetica 16 bold", relief=GROOVE, bd=2, command=conv, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btn7 = Button(btnrow3, text="7", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_7, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btn8 = Button(btnrow3, text="8", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_8, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btn9 = Button(btnrow3, text="9", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_9, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btnml = Button(btnrow3, text="*", font="Helvetica 22 bold", relief=GROOVE, bd=2, command=btn_ml, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btnrow4 = Frame(root, bg="#000000")
btnrow4.pack(expand=True, fill=BOTH)
mod_btn = Button(btnrow4, text="%", font="Helvetica 20 bold", relief=GROOVE, bd=2, command=mod, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
bl_btn = Button(btnrow4, text="(", font="Helvetica 20 bold", relief=GROOVE, bd=2, command=bl, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
br_btn = Button(btnrow4, text=")", font="Helvetica 20 bold", relief=GROOVE, bd=2, command=br, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
dot_btn = Button(btnrow4, text=".", font="Helvetica 20 bold", relief=GROOVE, bd=2, command=dot, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btn0 = Button(btnrow4, text="0", font="Helvetica 20 bold", relief=GROOVE, bd=2, command=btn_0, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btnc = Button(btnrow4, text="C", font="Helvetica 20 bold", relief=GROOVE, bd=2, command=cl, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btneq = Button(btnrow4, text="=", font="Helvetica 20 bold", relief=GROOVE, bd=2, command=eq, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
del_btn = Button(btnrow4, text="⌫", font="Helvetica 18 bold", relief=GROOVE, bd=2, command=back, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
btnd = Button(btnrow4, text="/", font="Helvetica 20 bold", relief=GROOVE, bd=2, command=btn_di, fg="Black", bg="#fefcaf").pack(side=LEFT, expand=True, fill=BOTH)
root.mainloop()