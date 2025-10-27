import math
from turtle import*

def hearta(k):
    return 15*math.sin(k)**3

def heartb(k):
    return 12*math.cos(k)-5*\
           math.cos(2*k)-2*\
           math.cos(3*k)-\
           math.cos(4*k)

Screen().title("Heart :3")
speed(0) 
bgcolor("pink")
color("red", "red") 
penup()
goto(0, 270) 
write("I love you :3", align="center", font=("Arial", 24, "bold")) 
goto(hearta(0)*20, heartb(0)*20)
pendown()
begin_fill()

for i in range(628):
    x = hearta(i/100)*20
    y = heartb(i/100)*20
    goto(x, y)

end_fill()

done()
