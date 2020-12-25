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


#initialize the main game loop
while True:
    window.update()
