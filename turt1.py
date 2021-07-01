#MODULE 7 - Pythin Turtle graphics
#https://docs.python.org/3/library/turtle.html (Links to an external site.)
#Before using turtle install turtle graphics.
#sudp apt install python3-tk python-tk
#
#Try this code:

import turtle

w = turtle.Screen()
w.clear()
w.bgcolor("#ffffff")
t = turtle.Turtle()
#turtle.tracer(0, 0)
# - - - - -
t.speed(1)
t.goto(0,0)
t.seth(0)
t.forward(100)
t.pencolor('#FF0000')
t.goto(0,0)
t.seth(90)
t.forward(100)
t.pencolor('#00FF00')
t.goto(0,0)
t.seth(180)
t.forward(100)
t.pencolor('#0000FF')
t.goto(0,0)
t.seth(270)
t.forward(100)
t.pencolor('#FFFF00')
#turtle.update()
w.exitonclick()
