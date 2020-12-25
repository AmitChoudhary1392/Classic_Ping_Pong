#!/usr/bin/env python
# coding: utf-8

# Classic Ping Pong Game using Python Turtle Library
# Task Breakdown for the Game
# Task 1- Build the game window and initialize the game's main loop
# Task 2 : Create the two paddles and the ball
# Task 3 : Move the paddles with the keyboard
# Task 4 : Move the ball and constrain its movement
# Task 5 : Bounce the ball back when it collides with the paddles
# Task 6 : add a scoring system to the game

"""************************************************************************"""

#import dependencies
import turtle

#initiate game window
window= turtle.Screen()
window.title("Classic Ping Pong")       #title of the window
window.bgcolor("black")                 #window background color
window.setup(width=800, height=600)
window.tracer(0)                        #accelerate the graphics without delays

# Build Paddles and Ball

## Left Paddle
Paddle_L = turtle.Turtle()        #initialise turtle object by accessing Turtle class
Paddle_L.speed(0)               #sets speed of animation based on argument, 0-max speed/zero delay

### Set paddle features
Paddle_L.shape("square")
Paddle_L.color("blue")
Paddle_L.shapesize(stretch_wid=5, stretch_len=1)        #default size of square shape is 20x20 px
Paddle_L.penup()                #move the turtle without a trace

### Set starting coordinates for the left paddle. Default (0,0) for turtle object
Paddle_L.goto(-350,0)

## Right Paddle
Paddle_R = turtle.Turtle()       #initialise turtle object by accessing Turtle class
Paddle_R.speed(0)               #sets speed of animation based on argument, 0-max speed/zero delay

### Set paddle features
Paddle_R.shape("square")
Paddle_R.color("red")
Paddle_R.shapesize(stretch_wid=5, stretch_len=1)        #default size of square shape is 20x20 px
Paddle_R.penup()                #move the turtle without a trace

### Set starting coordinates for the left paddle. Default (0,0) for turtle object
Paddle_R.goto(350,0)

## Ball
ball= turtle.Turtle()
ball.speed(0)

### Set ball features
ball.shape("circle")
ball.color("white")
ball.penup()
### no need to define starting point. Default is (0,0)

# Define ball movement by changes in coordinates
ball.dx = 0.25
ball.dy = 0.25      #dx/dy- change in coordinates or turtle will move diagonally in steps

## After defining the movement-- create a loop for continuous travel


#Functions for paddle movement

## Left Paddle
def Paddle_L_Up():
    
    y = Paddle_L.ycor()         # get Y coordinate for paddle
    y = y + 20                  # new position
    Paddle_L.sety(y)            # place the paddle at new coordinates

def Paddle_L_Down():
    
    y = Paddle_L.ycor()         # get Y coordinate for paddle
    y = y - 20                  # new position
    Paddle_L.sety(y)            # place the paddle at new coordinates

## Right Paddle 
def Paddle_R_Up():
    
    y = Paddle_R.ycor()         # get Y coordinate for paddle
    y = y + 10                  # new position
    Paddle_R.sety(y)            # place the paddle at new coordinates

def Paddle_R_Down():
    
    y = Paddle_R.ycor()         # get Y coordinate for paddle
    y = y - 10                  # new position
    Paddle_R.sety(y)            # place the paddle at new coordinates

# Keyboard Binding--- To interact with Keyboard

window.listen()
window.onkeypress(Paddle_L_Up, "w")         # key press interaction (function call, defined key)
window.onkeypress(Paddle_L_Down, "s")
window.onkeypress(Paddle_R_Up, "Up")        # using Arrow keys
window.onkeypress(Paddle_R_Down, "Down")


#initialize the main game loop
while True:
    window.update()

    ## new coordinates for ball movement 
    newX = ball.xcor() + ball.dx
    newY = ball.ycor() + ball.dy

    ball.setx(newX)
    ball.sety(newY)

    ## Check Borders and define constraints

    ### to bounce back when it hits the top of window
    if ball.ycor()>290:
        #set y coordinate to border limit and change direction
        ball.sety(290)
        ball.dy = ball.dy * -1
    
    ### to bounce back if it hits the bottom of window
    elif ball.ycor()<-290:
        #set y coordinate to border limit and change direction
        ball.sety(-290)
        ball.dy = ball.dy * -1

