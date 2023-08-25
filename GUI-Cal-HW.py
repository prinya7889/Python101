from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title(' Calculate App ')
GUI.geometry ('600x500')

L1 = Label(GUI, text=' How many Kg. ? ', font=('Tahoma', 15), fg='Blue')
L1.pack()

v_kilo = StringVar()

E1 = ttk.Entry(GUI, textvariable=v_kilo, width=10, font=('Tahoma', 18), justify='right')
E1.pack(pady=20)

def Calc(event=None) :
    print (' Processing ........  ')
    kilo = float (v_kilo.get())
    print ( kilo * 10)
    calc_result = kilo * 299
    messagebox.showinfo(' Total : ', ' Pay : {:,.2f} baht (299 Baht per Kilogram) '. format(calc_result))

B1 = ttk.Button(GUI, text=' Calculate ', command = Calc)
B1.pack (ipadx=40, ipady=30)

E1.bind('<Return>', Calc)

GUI.mainloop()
                
    
