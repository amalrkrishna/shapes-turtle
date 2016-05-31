import turtle
import time
import random

squares = input("Enter the number of sides of the shape: ")
	
numshapes = input("Enter the number of shapes to draw: ")

angle = 180 - 180*(squares-2)/squares

turtle.up

x = 0 
y = 0
turtle.setpos(x,y)

for x in range(numshapes):
	turtle.color(random.random(),random.random(), random.random())
	#turtle.forward(x)
	turtle.left(y)
	for i in range(squares):
		turtle.begin_fill() # Begin the fill process.
		turtle.down() # "Pen" down?
		for i in range(squares):  # For each edge of the shape
   			turtle.forward(100) # Move forward 100 units
   			turtle.left(angle) # Turn ready for the next edge
		turtle.up() # Pen up
		turtle.end_fill() # End fill.
	y = 40
	
time.sleep(11)
turtle.bye()
