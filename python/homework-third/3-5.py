#Windows启动界面进度条
import time
width = 50
print()
for i in range(1,12):
    if i in (1,6,11):
        print("{0:^50}".format("-"*20))
    else:
        print("{0:>15}{1:^20}{2:<15}".format("|", "|","|"))
print("正在启动Windows...".center(width,"-"))
print()
for i in range(width+1):
    a = "|"*i
    b = "."*(width-i)    
    c = (i/width)*100
    print("\r[{}{}] {:^3.0f}%".format(a, b, c), end="")
    time.sleep(0.3)
print()
print("\n"+"Windows已启动成功！".center(width,"-"))