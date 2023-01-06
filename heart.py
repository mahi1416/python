import turtle
from turtle import *

win = Screen()
win = bgpic("magic.gif")
t = turtle.Turtle()
t.pencolor("black")


def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)


def heart():
    t.penup()
    t.bk(200)
    
    
    t.goto(40,-70)
    t.pendown()
    t.pensize(2)
    t.fillcolor("red")
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()


heart()
t.ht()


def write(message, pos):
    x, y = pos
    t.penup()
    t.goto(x, y)
    t.color("white")
    style = ("Stencil Std", 18, "italic")
    t.write(message, font=style)


write("H", (-50, 45))
write("A", (-40, 45))
write("P", (-30, 45))
write("P", (-20, 45))
write("Y", (-10, 45))
write("N", (10, 45))
write("E", (20, 45))
write("W", (30, 45))
write("Y", (50, 45))
write("E", (40, 45))
write("A", (50, 45))
write("R", (60, 45))




done()
