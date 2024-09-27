from turtle import *


print("hello world")
print("მარიამ ფუხაშვილი")


#i want to paint a house 

#step one:draw a square
speed(3)

width(10)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing door

forward(70)
color("brown")
left(90)
forward(120)
right(90)
forward(70)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("black")
right(150)
forward(190)
left(120)
forward(200)

penup()
goto(20, 90)
pendown()

color("yellow")
left(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(20, 90)
pendown()

left(80)

penup()
goto(200, 100)
pendown()

left(190)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
#end of drawing a house