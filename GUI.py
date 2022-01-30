from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Fake Wordle")
        master.minsize(900,900)
        master.configure(background = "#808080")

        set = ttk.Treeview(master)
        set.pack()

        set['columns']= ("1","2","3","4","5")
        set.column("#0", width=0,  stretch=NO)
        set.column("1",anchor=CENTER, width=80)
        set.column("2",anchor=CENTER, width=80)
        set.column("3",anchor=CENTER, width=80)
        set.column("4",anchor=CENTER, width=80)
        set.column("5",anchor=CENTER, width=80)

        set.heading("#0",text="",anchor=CENTER)
        set.heading("1",text="1",anchor=CENTER)
        set.heading("2",text="2",anchor=CENTER)
        set.heading("3",text="3",anchor=CENTER)
        set.heading("4",text="4",anchor=CENTER)
        set.heading("5",text="5",anchor=CENTER)

        set.insert(parent='',index='end',iid=0,text='',
        values=('101','john','Gold'))
        set.insert(parent='',index='end',iid=1,text='',
        values=('102','jack',"Silver"))
        set.insert(parent='',index='end',iid=2,text='',
        values=('103','joy','Bronze'))

root = Tk()
gui = GUI(root)
root.mainloop()