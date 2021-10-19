step=0
F=0
while True:
    houchiblackshang=input('后尺黑面上丝读数=')
    houchiblackxia=input('后尺黑面下丝读数=')
    houchibalckzhong=input('后尺黑面中丝读数=')
    houchiredzhong=input('后尺红面中丝读数=')
    qianchiblackshang=input('前尺黑面上丝读数=')
    qianchiblackxia=input('前尺黑面下丝读数=')
    qianchiblackzhong=input('前尺黑面中丝读数=')
    qianchiredzhong=input('前尺红面中丝读数=')
    K=input('K=')
    houshijvli=(eval(houchiblackshang)-eval(houchiblackxia))*100
    qianshijvli=(eval(qianchiblackshang)-eval(qianchiblackxia))*100
    qianhoushijvcha=abs(houshijvli-qianshijvli)
    qianhoushijvcha2=houshijvli-qianshijvli
    print('后视距离=',round(houshijvli,3),'m')
    print('前视距离=',round(qianshijvli,3),'m')
    print('前，后视距差=',round(qianhoushijvcha2,3),'m')
    if qianshijvli>=100:
        print('前视距离过大')
    if houshijvli>=100:
        print('后视距离过大')
    if qianhoushijvcha>5:
        print('前，后视距差过大')
    houchirbdushucha=abs(eval(houchibalckzhong)+eval(K)-eval(houchiredzhong))
    print('后尺红黑面读数差=',round(houchirbdushucha,3),'m')
    if houchirbdushucha>0.003:
        print('后尺红黑面读数差过大')
    qianchirbdushucha=abs(eval(qianchiblackzhong)+eval(K)-eval(qianchiredzhong))
    print('前尺红黑面读数差=',round(qianchirbdushucha,3),'m')
    if qianchirbdushucha>0.003:
        print('前尺红黑面读数差过大')
    liangchiheimiangaocha=eval(houchibalckzhong)-eval(qianchiblackzhong)
    liangchihongmiangaocha=eval(houchiredzhong)-eval(qianchiredzhong)
    print('两尺黑面高差=',round(liangchiheimiangaocha,3),'m')
    print('两尺红面高差=', round(liangchihongmiangaocha,3),'m')
    blackred=liangchiheimiangaocha-liangchihongmiangaocha
    if blackred<0:
        BRR=blackred+0.1
        print('黑面高差与红面高差之差=', round(BRR, 3), 'm')
    elif blackred>0:
        BRR=blackred-0.1
        print('黑面高差与红面高差之差=', round(BRR, 3), 'm')
    if blackred==0:
        BRR=0
        print('数据可能有误')
    if BRR>0.005 :
        print('黑面高差与红面高差之差过大')
    gaochazhongshus=liangchiheimiangaocha+liangchihongmiangaocha
    if gaochazhongshus<0:
        gaochazhongshu=(gaochazhongshus+0.1)/2
        print('高差中数=',round(gaochazhongshu,3),'m')
    elif gaochazhongshus>=0:
        gaochazhongshu=(gaochazhongshus-0.1)/2
        print('高差中数=',round(gaochazhongshu,3),'m')
    F=F+qianhoushijvcha2
    step+=1
    print('当前测站编号为',step)
    time=input('继续测量请输入1/结束测量请输入2=')
    if time=='1':
        print('视距累计差=',round(F,3),'m')
        if F>10:
            print('视距累计差过大')
        continue
    if time=='2':
        print('视距累计差=',round(F,3),'m')
        if F>10:
            print('视距累计差过大')
        break






