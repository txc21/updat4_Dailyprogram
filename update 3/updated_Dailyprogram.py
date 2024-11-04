import tkinter as tk
import ttkbootstrap as ttk
from classe import *
from classes import *
# window
root = ttk.Window(themename='darkly')
root.title(today)
root.geometry('600x300')
# title
the_day= ttk.Label(master= root,text=today,font='cilibri 20 bold')
the_day.pack(pady=5)


# class1

frame = ttk.Frame(master=root)
spg = tk.StringVar()
supject1= ttk.Label(master=frame,text='class1',font='cilibri 15 bold' , textvariable=spg)
# class2 

supg2 = tk.StringVar()
supject2= ttk.Label(master=frame,text='class1',font='cilibri 15 bold' , textvariable=supg2)
# class3

supg3 = tk.StringVar()
supject3= ttk.Label(master=frame,text='class1',font='cilibri 15 bold' , textvariable=supg3)
# class 4

supg4 = tk.StringVar()
supject4= ttk.Label(master=frame,text='class1',font='cilibri 15 bold' , textvariable=supg4)
# class 5

supg5 = tk.StringVar()
supject5= ttk.Label(master=frame,text='class1',font='cilibri 15 bold' , textvariable=supg5)
# class 6

supg6 = tk.StringVar()
supject6= ttk.Label(master=frame,text='class1',font='cilibri 15 bold' , textvariable=supg6)
# class 7

supg7 = tk.StringVar()
supject7= ttk.Label(master=frame,text='class1',font='cilibri 15 bold' , textvariable=supg7)

def classes_system():
        spg.set(class1)
        supg2.set(class2)
        supg3.set(class3)
        supg4.set(class4)
        supg5.set(class5)
        supg6.set(class6)
        supg7.set(class7)

classes_system()



## made by : *****
MMe = ttk.Label(master  = root,text='Made By : *****',font = 'cilibri 15 bold')
# sssd
frame.pack()
supject1.pack(side='left')

supject2.pack(side='left')

supject3.pack(side='left')

supject4.pack(side='left')

supject5.pack(side='left')

supject6.pack(side='left')

supject7.pack(side='left')
MMe.pack(pady=10)
# end
root.mainloop()