#测量学计算GUI Ver 1.0
#///////////////////////////////////////////

import tkinter as tk

windows=tk.Tk()
windows.title('测量学计算')
windows.geometry('200x100')

def K4787():
    progress=tk.Tk()
    progress.title('测量学计算')
    progress.geometry('800x600')

    tk.Label(progress, text='后尺黑面上丝读数=').place(x=10,y=10)
    tk.Label(progress, text='后尺黑面下丝读数=').place(x=10, y=40)
    tk.Label(progress, text='后尺黑面中丝读数=').place(x=10, y=70)
    tk.Label(progress, text='后尺红面下丝读数=').place(x=10, y=100)
    tk.Label(progress, text='前尺黑面上丝读数=').place(x=10, y=130)
    tk.Label(progress, text='前尺黑面下丝读数=').place(x=10, y=160)
    tk.Label(progress, text='前尺黑面中丝读数=').place(x=10, y=190)
    tk.Label(progress, text='前尺红面下丝读数=').place(x=10, y=220)

    hchmss=tk.Entry(progress,show=None).place(x=140,y=10)
    hchmxs=tk.Entry(progress,show=None).place(x=140,y=40)







def K4687():
    print(2)


ChooseK4787=tk.Button(windows,text='K=4.787',command=K4787)
ChooseK4787.pack()
ChooseK4687=tk.Button(windows,text='K=4.687',command=K4687)
ChooseK4687.pack()






windows.mainloop()