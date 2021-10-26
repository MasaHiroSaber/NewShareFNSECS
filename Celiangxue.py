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

    def Jis():
        step=0
        F=0

        houchiblackshang=hcbmss.get()
        houchiblackxia=hcbmxs.get()
        houchibalckzhong = hcbmzs.get()
        houchiredzhong = hcrmzs.get()
        qianchiblackshang = qcbmss.get()
        qianchiblackxia = qcbmxs.get()
        qianchiblackzhong = qcbmzs.get()
        qianchiredzhong = qcrmzs.get()

        houshijvli = (eval(houchiblackshang) - eval(houchiblackxia)) * 100
        qianshijvli = (eval(qianchiblackshang) - eval(qianchiblackxia)) * 100
        qianhoushijvcha = abs(houshijvli - qianshijvli)
        qianhoushijvcha2 = houshijvli - qianshijvli
        hsjl.insert(round(houshijvli,3))
        print('后视距离=', round(houshijvli, 3), 'm')
        print('前视距离=', round(qianshijvli, 3), 'm')
        print('前，后视距差=', round(qianhoushijvcha2, 3), 'm')
        if qianshijvli >= 100:
            print('前视距离过大')
        if houshijvli >= 100:
            print('后视距离过大')
        if qianhoushijvcha > 5:
            print('前，后视距差过大')
        if step % 2 == 1:
            houchirbdushucha = eval(houchibalckzhong) + 4.787 - eval(houchiredzhong)
            print('后尺红黑面读数差=', round(houchirbdushucha, 3), 'm')
            if abs(houchirbdushucha) > 0.003:
                print('后尺红黑面读数差过大')
            qianchirbdushucha = eval(qianchiblackzhong) + 4.687 - eval(qianchiredzhong)
            print('前尺红黑面读数差=', round(qianchirbdushucha, 3), 'm')
            if abs(qianchirbdushucha) > 0.003:
                print('前尺红黑面读数差过大')
        elif step % 2 == 0:
            houchirbdushucha = eval(houchibalckzhong) + 4.687 - eval(houchiredzhong)
            print('后尺红黑面读数差=', round(houchirbdushucha, 3), 'm')
            if abs(houchirbdushucha) > 0.003:
                print('后尺红黑面读数差过大')
            qianchirbdushucha = eval(qianchiblackzhong) + 4.787 - eval(qianchiredzhong)
            print('前尺红黑面读数差=', round(qianchirbdushucha, 3), 'm')
            if abs(qianchirbdushucha) > 0.003:
                print('前尺红黑面读数差过大')
        liangchiheimiangaocha = eval(houchibalckzhong) - eval(qianchiblackzhong)
        liangchihongmiangaocha = eval(houchiredzhong) - eval(qianchiredzhong)
        print('两尺黑面高差=', round(liangchiheimiangaocha, 3), 'm')
        print('两尺红面高差=', round(liangchihongmiangaocha, 3), 'm')
        blackred = liangchiheimiangaocha - liangchihongmiangaocha
        if blackred < 0:
            BRR = blackred + 0.1
            print('黑面高差与红面高差之差=', round(BRR, 4), 'm')
        elif blackred > 0:
            BRR = blackred - 0.1
            print('黑面高差与红面高差之差=', round(BRR, 4), 'm')
        if blackred == 0:
            BRR = 0
            print('数据可能有误')
        if abs(BRR) > 0.005:
            print('黑面高差与红面高差之差过大')
        gaochazhongshus = liangchiheimiangaocha + liangchihongmiangaocha
        if gaochazhongshus < 0:
            gaochazhongshu = (gaochazhongshus + 0.1) / 2
            print('高差中数=', round(gaochazhongshu, 3), 'm')
        elif gaochazhongshus >= 0:
            gaochazhongshu = (gaochazhongshus - 0.1) / 2
            print('高差中数=', round(gaochazhongshu, 3), 'm')
        F = F + qianhoushijvcha2
        print('视距累计差=', round(F, 3), 'm')
        if F > 10:
            print('视距累计差过大')
        print('当前测站编号为', step)
        time = input('继续测量请输入1/结束测量请输入2=')
    


    tk.Label(progress, text='后尺黑面上丝读数=').place(x=10,y=10)
    tk.Label(progress, text='后尺黑面下丝读数=').place(x=10, y=40)
    tk.Label(progress, text='后尺黑面中丝读数=').place(x=10, y=70)
    tk.Label(progress, text='后尺红面下丝读数=').place(x=10, y=100)
    tk.Label(progress, text='前尺黑面上丝读数=').place(x=10, y=130)
    tk.Label(progress, text='前尺黑面下丝读数=').place(x=10, y=160)
    tk.Label(progress, text='前尺黑面中丝读数=').place(x=10, y=190)
    tk.Label(progress, text='前尺红面下丝读数=').place(x=10, y=220)

    tk.Label(progress, text='后视距离=').place(x=300, y=10)
    tk.Label(progress, text='前视距离=').place(x=300, y=40)
    tk.Label(progress, text='前，后视距差=').place(x=300, y=70)
    tk.Label(progress, text='后尺红黑面读数差=').place(x=300, y=100)
    tk.Label(progress, text='前尺红黑面读数差=').place(x=300, y=130)
    tk.Label(progress, text='两尺黑面高差=').place(x=300, y=160)
    tk.Label(progress, text='两尺红面高差=').place(x=300, y=190)
    tk.Label(progress, text='黑面高差与红面高差之差=').place(x=300,y=220)
    tk.Label(progress, text='高差中数=').place(x=300,y=250)
    tk.Label(progress, text='视距累计差=').place(x=300, y=280)

    hsjl=tk.Text(progress,width=20,height=1).place(x=360,y=10)
    qsjl=tk.Text(progress,width=20,height=1).place(x=360,y=40)
    qhsjc=tk.Text(progress, width=20,height=1).place(x=384,y=70)
    hchhmdsc=tk.Text(progress, width=20,height=1).place(x=408,y=100)
    qchhmdsc=tk.Text(progress, width=20,height=1).place(x=408,y=130)
    lcbmgc=tk.Text(progress, width=20,height=1).place(x=384,y=160)
    lcrmgc=tk.Text(progress, width=20,height=1).place(x=384,y=190)
    hmgchmgczc=tk.Text(progress, width=20,height=1).place(x=444,y=220)
    gczs=tk.Text(progress, width=20,height=1).place(x=360,y=250)
    ljsjc=tk.Text(progress, width=20,height=1).place(x=372,y=280)



    hcbmss=tk.Entry(progress).place(x=140,y=10)
    hcbmxs=tk.Entry(progress).place(x=140,y=40)
    hcbmzs=tk.Entry(progress).place(x=140,y=70)
    hcrmzs=tk.Entry(progress).place(x=140,y=100)
    qcbmss=tk.Entry(progress).place(x=140,y=130)
    qcbmxs=tk.Entry(progress).place(x=140,y=160)
    qcbmzs=tk.Entry(progress).place(x=140,y=190)
    qcrmzs=tk.Entry(progress).place(x=140,y=220)

    tk.Button(progress,text='计算',command=Jis).place(x=160,y=250)








def K4687():
    progress = tk.Tk()
    progress.title('测量学计算')
    progress.geometry('800x600')

    tk.Label(progress, text='后尺黑面上丝读数=').place(x=10, y=10)
    tk.Label(progress, text='后尺黑面下丝读数=').place(x=10, y=40)
    tk.Label(progress, text='后尺黑面中丝读数=').place(x=10, y=70)
    tk.Label(progress, text='后尺红面下丝读数=').place(x=10, y=100)
    tk.Label(progress, text='前尺黑面上丝读数=').place(x=10, y=130)
    tk.Label(progress, text='前尺黑面下丝读数=').place(x=10, y=160)
    tk.Label(progress, text='前尺黑面中丝读数=').place(x=10, y=190)
    tk.Label(progress, text='前尺红面下丝读数=').place(x=10, y=220)

    hcbmss = tk.Entry(progress, show=None).place(x=140, y=10)
    hcbmxs = tk.Entry(progress, show=None).place(x=140, y=40)
    hcbmzs = tk.Entry(progress, show=None).place(x=140, y=70)
    hcrmzs = tk.Entry(progress, show=None).place(x=140, y=100)
    qcbmss = tk.Entry(progress, show=None).place(x=140, y=130)
    qcbmxs = tk.Entry(progress, show=None).place(x=140, y=160)
    qcbmzs = tk.Entry(progress, show=None).place(x=140, y=190)
    qcrbzs = tk.Entry(progress, show=None).place(x=140, y=220)


ChooseK4787=tk.Button(windows,text='K=4.787',command=K4787)
ChooseK4787.pack()
ChooseK4687=tk.Button(windows,text='K=4.687',command=K4687)
ChooseK4687.pack()

windows.mainloop()