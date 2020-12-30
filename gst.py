import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def select():
    selected =k.get()
    c1.config(state=tk.DISABLED if selected == 1 else tk.NORMAL)
    c2.config(state=tk.DISABLED if selected == 1 else tk.NORMAL)

def submit():
    a=s1.get()
    if k.get()==1:
        m=a+(18*a)/100
        s2.set(m)
        messagebox.showinfo("Total", "Total Amount = "+str(m))
        
    elif k.get()==2:
        p=0
        if v1.get()==1:
            m=a+(10*a)/100
            p+=m
            
        if v2.get()==1:
            q=a+(10*a)/100
            p+=q

        s2.set(p)
        messagebox.showinfo("Total", "Total Amount = "+str(p))
        
    s1.set(a)

def reset():
    s1.set(0)
    k.set(0)
    v1.set(0)
    v2.set(0)
    s2.set(0.0)

root=tk.Tk()
root.title("WINDOWS")
root.geometry("400x400")
#root.configure(bg="yellow")

k=tk.IntVar()
v1=tk.IntVar()
v2=tk.IntVar()
s1=tk.IntVar()
s2=tk.DoubleVar()

l1=ttk.Label(root, text="Enter Amount", font="Cambria 14 bold")
l1.place(x=50, y=50)
e1=ttk.Entry(root, textvariable=s1)
e1.place(x=200, y=55)

r1=ttk.Radiobutton(root, text="GST (18%)", variable=k, value=1, command=select)
r1.place(x=70, y=100)
r2=ttk.Radiobutton(root, text="NON-GST (20%)", variable=k, value=2, command=select)
r2.place(x=200, y=100)

c1=ttk.Checkbutton(root, text="IGST (10%)", variable=v1)
c1.place(x=250 , y=150)
c2=ttk.Checkbutton(root, text="SST (10%)", variable=v2)
c2.place(x=250 , y=200)

b1=ttk.Button(root, text="SUBMIT", command=submit)
b1.place(x=50, y= 270)
b2=ttk.Button(root, text="RESET", command=reset)
b2.place(x=150, y= 270)
b3=ttk.Button(root, text="EXIT", command=root.destroy)
b3.place(x=250, y= 270)

l2=ttk.Label(root, text="Total Amount", font="Cambria 14 bold")
l2.place(x=50, y=330)
e2=ttk.Entry(root, textvariable=s2)
e2.place(x=200, y=335)

root.mainloop()
