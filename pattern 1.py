from turtle import *

speed('fastest')
pencolor('red')
pensize(3)

for i in range(8):
    fd(120)
    lt(360/8)
    circle(40,90)
    for i in range(5):
        fd(50)
        lt(360/8)
    
hideturtle()
mainloop()