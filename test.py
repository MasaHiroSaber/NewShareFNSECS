import tkinter as tk
windows=tk.Tk()
windows.title('测量学计算')
windows.geometry('200x100')
hcbmss=tk.Entry(windows,show=None)
def P():
    var=hcbmss.get()
    print(type(var))
    print(1)
tk.Button(windows,text='123',command=P).pack()
hcbmss.pack()

windows.mainloop()
