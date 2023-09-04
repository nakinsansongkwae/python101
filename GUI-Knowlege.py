from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

L1 =Label(GUI,text='โปรแกรมความรู้',front('Angsana New',30),fg='green')
L1.place(x=30,y=30)


def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)


FB1 = Frame(GUI)
FB1.place(x=100,y=300)


B2 = ttk.Button(FB1,text = 'เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)







GUI.mainloop()
