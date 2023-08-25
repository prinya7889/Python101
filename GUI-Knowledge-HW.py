from tkinter import *
from tkinter import ttk, messagebox


GUI = Tk()
GUI.title('HW-GUI')
GUI.geometry('600x500')

L1 = Label(GUI, text='Your profile', font=('Tahoma',20), fg='blue')
L1.place(x=200, y=10)

L2 = Label(GUI, text=' Name : ', font=('Tahoma', 15), fg='green')
L2.place(x=50, y=50)

L3 = Label(GUI, text=' Height : ', font=('Tahoma', 15), fg='green')
L3.place(x=50, y=150)

def BtnName():
    text = 'MaTaLaDa'
    messagebox.showinfo(' My name is  ',text)
def BtnHeight():
    text = '170 cm. '
    messagebox.showinfo(' I am Height  ',text)

    
FBName = LabelFrame(GUI)
FBName.place(x=180, y=50)
BName = ttk.Button(FBName, text=' Name Message ', command = BtnName)
BName.pack(ipadx=30, ipady=20)

FBHeight = LabelFrame(GUI)
FBHeight.place(x=180, y=150)
BHeight = ttk.Button(FBHeight, text=' Name Message ', command = BtnHeight)
BHeight.pack(ipadx=30, ipady=20)

GUI.mainloop()
