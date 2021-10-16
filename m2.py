try:
    for i in range(2 ** 31 - 1):
        you = int(input("请输入剪刀0，石头1，布2:"))
        import random
        import os
        import time

        cp = random.randint(0, 2)
        Website = random.randint(93000000, 95000000)
        WebsiteX = '"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://pixiv.moe/illust/' + str(
            Website)
        WebsiteS = '"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" http://passport2.chaoxing.com/'
        if (you > 2 or you < 0):
            print("没有这种出法哦")
        else:
            print("电脑出的是 %d\n " % cp)
            if (you == 0):
                if (cp == 0):
                    print("平局，请再出一次")
                elif (cp == 1):
                    print("你输了\n快去学习")
                    os.system(WebsiteS)
                else:
                    print("你赢了")
                    os.system(WebsiteX)
            if (you == 1):
                if (cp == 1):
                    print("平局，请再出一次")
                elif (cp == 2):
                    print("你输了\n快去学习")
                    os.system(WebsiteS)
                else:
                    print("你赢了")
                    os.system(WebsiteX)
            if (you == 2):
                if (cp == 2):
                    print("平局，请再出一次")
                elif (cp == 0):
                    print("你输了\n快去学习")
                    os.system(WebsiteS)
                else:
                    print("你赢了")
                    os.system(WebsiteX)
        time.sleep(1)
        Result = int(input('是否继续玩？(1继续/2不继续)'))
        if Result == 1:
            continue
        if Result == 2:
            break
        if Result != 1 or 2:
            print('输入有误，退出游戏')
            break

except:
    print('输入有误')
