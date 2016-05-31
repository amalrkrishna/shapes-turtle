import turtle
import time
import random

numshapes = input("Enter the number of circles to draw: ")
radius = input("Enter the radius of the largest circle: ")

turtle.penup()
for i in range(radius, 0, -(radius/numshapes)):
	turtle.color(random.random(),random.random(), random.random())
	turtle.begin_fill() # Begin the fill process.
	turtle.down() # "Pen" down?
    	turtle.right(90)    # Face South
    	turtle.forward(i)   # Move one radius
    	turtle.right(270)   # Back to start heading
    	turtle.pendown()    # Put the pen back down
    	turtle.circle(i)    # Draw a circle
	turtle.up() # Pen up
	turtle.end_fill() # End fill.
   	turtle.penup()      # Pen up while we go home
   	turtle.home()       # Head back to the start pos
