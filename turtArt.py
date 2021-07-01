from turtle import *
from random import randrange
colors = ['#ff0000','#ffff00','#00ff00','#00ffff','#0000ff','#ff00ff']
width = 1
h=0
n = 0
dist = 0.5
inc = 0.5
space = Screen()
space.bgcolor('#000000')            # create a turtle screen (space)
t = Turtle(visible=False)             # create a turtle named zari
t1 = Turtle(visible=False)             # create a turtle named zari
t2 = Turtle(visible=False)             # create a turtle named zari
t3 = Turtle(visible=False)             # create a turtle named zari
t.width(width)
t1.width(width)
t2.width(width)
t3.width(width)
t.speed('fastest')
t1.speed('fastest')
t2.speed('fastest')
t3.speed('fastest')
# ~ t.goto(-255,-255)
# ~ t1.goto(-255,-255)
while 1==1:
	h+=0.5
	t.width(width)
	t1.width(width)
	t2.width(width)
	t3.width(width)
	t.pencolor(colors[randrange(0,6)])
	t1.pencolor(colors[randrange(0,6)])
	t2.pencolor(colors[randrange(0,6)])
	t3.pencolor(colors[randrange(0,6)])
	t.setheading(90+h)         
	t1.setheading(90+h)        
	t2.setheading(-90+h)         # Point due north
	t3.setheading(-90+h)         # Point due north
	t.forward(dist)           # tell zari to move forward by 100 units
	t1.forward(dist)           # tell zari to move forward by 100 units
	t2.forward(dist)           # tell zari to move forward by 100 units
	t3.forward(dist)           # tell zari to move forward by 100 units
	t.left(90)              # turn right by 90 degrees
	t2.left(90)              # turn right by 90 degrees
	t1.right(90)              # turn right by 90 degrees
	t3.right(90)              # turn right by 90 degrees
	t.forward(dist)           # tell zari to move forward by 100 units
	t2.forward(dist)           # tell zari to move forward by 100 units
	t1.forward(dist)           # tell zari to move forward by 100 units
	t3.forward(dist)           # tell zari to move forward by 100 units
	t.left(90)              # turn right by 90 degrees
	t2.left(90)              # turn right by 90 degrees
	t1.right(90)              # turn right by 90 degrees
	t3.right(90)              # turn right by 90 degrees
	t.forward(dist)           # tell zari to move forward by 100 units
	t2.forward(dist)           # tell zari to move forward by 100 units
	t1.forward(dist)           # tell zari to move forward by 100 units
	t3.forward(dist)           # tell zari to move forward by 100 units
	t.left(90)              # turn right by 90 degrees
	t2.left(90)              # turn right by 90 degrees
	t1.right(90)              # turn right by 90 degrees
	t3.right(90)              # turn right by 90 degrees
	t.forward(dist)           # tell zari to move forward by 100 units
	t2.forward(dist)           # tell zari to move forward by 100 units
	t1.forward(dist)           # tell zari to move forward by 100 units
	t3.forward(dist)           # tell zari to move forward by 100 units
	t.left(90)              # turn right by 90 degrees
	t2.left(90)              # turn right by 90 degrees
	t1.right(90)              # turn right by 90 degrees
	t3.right(90)              # turn right by 90 degrees
	# ~ if n < 5:
		# ~ n += 1
	# ~ else:
		# ~ n = 0
	dist += inc
	inc += 0.0005
	
	width = 0.000003
