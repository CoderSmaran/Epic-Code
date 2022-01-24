#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:32:33 2021

@author: smaran
"""


import turtle
from turtle import bgcolor
from turtle import exitonclick,pencolor

def ghost():
    
    
    
    bgcolor('black')
    
    #sets background color
    
    turtle.setheading(270)
    #Sets Direction
    turtle.fillcolor('white')
    #Sets fillcolor
    turtle.begin_fill()
    #Starts the fill process
    turtle.circle(100, -180)
    #draws a semicircle/head
    turtle.setheading(270)
    #Sets direction
    turtle.forward(150)
    #Make the turtle go forward
    turtle.right(180)
    #Makes the turtle look the oppisite way
    turtle.circle(50,180)
    turtle.right(180)
    turtle.circle(50,180)
                   
    
    
    
    turtle.end_fill()
    
    turtle.fillcolor('black')
    
    turtle.penup();
    turtle.goto(40,0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(100,0)

    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()
    
   
    exitonclick()
ghost()
    

    
    
    
        