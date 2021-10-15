choose=input('二进制转十进制输入1/十进制转二进制输入2\n请输入:')
num=input('Number=')#输入数字
long=len(num)
Num=eval(num)
import time
stra=''
if choose=='2':
    s = time.perf_counter()
    while Num!=1 or 0:
        val10=Num%2#val10为数字的余数
        Num=(Num-val10)/2
        stra=stra+str(int(val10))
    r=stra+str(int(Num))
    R=r[::-1]
    t=time.perf_counter()-s
    print(R),print('计算用时=',t*1000,'ms')
elif choose=='1':
    s=time.perf_counter()
    Num=num[::-1]
    value=0
    for i in range(long):
        val=eval(Num[i])*(2**i)
        value=value+val
    t=time.perf_counter()-s
    print(value),print('计算用时=',t*1000,'ms')#233