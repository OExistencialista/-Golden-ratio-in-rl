import turtle 
t = turtle.Turtle()
import random
import time
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black']
f1= 0
f2=1
for i in range(int(input("ate qual valor a sequencia vai?:"))):
    f3 = f1 + f2
    f1 =f2
    f2 =f3 
    i = 1 + i
    
    t.pencolor(colors[5])
    for _ in range(2):
        t.forward(f1) 
        t.left(90)
        t.forward(f2)
        t.left(90)


time.sleep(100) 
turtle.done()       