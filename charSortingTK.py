from tkinter import *
from time import sleep


menu = Tk()
menu.title('CharSorting')
menu.geometry('500x500')
#menu.resizable(False, False)

label1 = Label(menu, text="profissa")
label2 = Label(menu, text="Profissional")
label3 = Label(menu, text="pack")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
menu.mainloop()



