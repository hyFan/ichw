#!/usr/bin/env python3
"""planets.py: Simulation of the orbits of six planets in solar system.


__author__ = "Fan Hanyun"
__pkuid__ = "1700017838"
__email__ = "501180426@qq.com"
"""


import turtle
import math


wn = turtle.Screen()
wn.bgcolor("black")
sun = turtle.Turtle()
sun.dot(30， "yellow")
sun.hideturtle()
me = turtle.Turtle()
me.shape("circle")
me.turtlesize(0.5)
me.color("blue")
me.pencolor("blue")
me.penup()
me.goto(40, 0)
me.pendown()
ve = turtle.Turtle()
ve.shape("circle")
ve.turtlesize(0.5)
ve.color("green")
ve.pencolor("green")
ve.penup()
ve.goto(60, 0)
ve.pendown()
ea = turtle.Turtle()
ea.shape("circle")
ea.turtlesize(0.5)
ea.color("white")
ea.pencolor("white")
ea.penup()
ea.goto(80, 0)
ea.pendown()
ma = turtle.Turtle()
ma.shape("circle")
ma.turtlesize(0.5)
ma.color("red")
ma.pencolor("red")
ma.penup()
ma.goto(90, 0)
ma.pendown()
ju = turtle.Turtle()
ju.shape("circle")
ju.turtlesize(0.7)
ju.color("brown")
ju.pencolor("brown")
ju.penup()
ju.goto(170, 0)
ju.pendown()
sa = turtle.Turtle()
sa.shape("circle")
sa.turtlesize(0.7)
sa.color("lightblue")
sa.pencolor("lightblue")
sa.penup()
sa.goto(200, 0)
sa.pendown()


def planets():
        for t in range(2000):
                y = 40*math.sin(math.radians(4.5*t+5))
                x = 40*math.cos(math.radians(4.5*t+5))
                me.goto(x, y)
                y = 50*math.sin(math.radians(4*t))
                x = 55*math.cos(math.radians(4*t))+5
                ve.goto(x, y)
                y = 90*math.sin(math.radians(3*t+10))+5
                x = 80*math.cos(math.radians(3*t+10))
                ea.goto(x, y)
                y = 110*math.sin(math.radians(2.5*t))+10
                x = 90*math.cos(math.radians(2.5*t))
                ma.goto(x, y)
                y = 150*math.sin(math.radians(2*t+5))
                x = 160*math.cos(math.radians(2*t+5))+10
                ju.goto(x, y)
                y = 180*math.sin(math.radians(t))
                x = 195*math.cos(math.radians(t))+5
                sa.goto(x, y)

                
def main():
        planets()
        
if __name__ == '__main__':
        main()
