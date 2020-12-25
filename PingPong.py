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


#initialize the main game loop
while True:
    window.update()
