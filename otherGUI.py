# Written by siembra1978
from tkinter import *
import graphCalc


class yvars:

    def __init__(self, master):
        self.master = master
        self.master.title('Graphing Input')

        self.master.configure(bg='gray1')

        self.Label1 = Label(self.master, text='Y=', font='Courier 11', bg='gray1', fg='white')
        self.Label1.grid(row=0, column=0)
        self.Entry1 = Entry(self.master, font='Courier 11', bg='gray9', fg='white')
        self.Entry1.grid(row=0, column=1)

        # self.Label2 = Label(self.master,text="Y2=")
        # self.Label2.grid(row=1,column=0)
        # self.Entry2 = Entry(self.master)
        # self.Entry2.grid(row=1,column=1)

        self.graph = Button(self.master, text='Graph', command=self.graphF, font='Courier 11', bg='gray1', fg='white')
        self.graph.grid(row=1, column=1)

    def graphF(self):
        string = self.Entry1.get()
        graphCalc.enter(string)


def startY():
    root = Tk()
    pGUI = yvars(root)
    root.mainloop()
