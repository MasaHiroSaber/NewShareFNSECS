

import tkinter as tk
windows=tk.Tk()
windows.title('测量学计算')
windows.geometry('200x100')

var=tk.StringVar()
l=tk.Label(windows,textvariable=var,bg='white',width=15,height=2)
l.pack()
on_hit=False
def Choose_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you choose me')
    else:
        on_hit=False
        var.set('')

b=tk.Button(windows,text='Chooes',width=15,height=2,command=Choose_me)
b.pack()

windows.mainloop()




