#彩色蟒蛇
from turtle import *
#setup(650,350,200,200)
penup()
fd(-250)
pendown()
pensize(25)
seth(-40)
colors=["purple","red","yellow","pink"]
for i in range(4): 
    pencolor(colors[i])
    circle(40,80)
    circle(-40,80)
pencolor("blue")
circle(40,80/2)
fd(40)
pencolor("green")
circle(16,180)
fd(40*2/3)
done()