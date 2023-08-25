from tkinter import *
from tkinter import ttk # theme of ttk
from tkinter import messagebox

GUI = Tk()  # Main Screen
GUI.title('Recording Application') # App name
GUI.geometry('500x400') # windows size

L1 = Label(GUI, text = 'โปรแกรมทดสอบปุ่ม' ,font=('Angsana New', 30), fg='green')
L1.place(x=10, y=10)


B1 = ttk.Button(GUI,text=' เงินกี่บาท ')
B1.pack(ipadx=20 , ipady=20)

###################
def Button2():
    text = ' มีเงินอยู่ 300 บาท'
    messagebox.showinfo(' เงินในบัญชี Info ', text)
    messagebox.showwarning(' เงินในบัญชี Warning', text)

FB2 = LabelFrame(GUI)
FB2.place(x=200, y=100)
B2 = ttk.Button(FB2, text=' เงินกี่บาท ', command = Button2)
#B2.place(x=50 ,y=200)
B2.pack(ipadx=20 , ipady=20)

#B2 = Button(GUI,text=' เงินกี่บาท ')
#B2.pack()

GUI.mainloop()
