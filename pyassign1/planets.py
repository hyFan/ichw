import turtle
import math
wn = turtle.Screen()
sun = turtle.Turtle()
sun.dot(10,"yellow")
sun.hideturtle()
me = turtle.Turtle()
me.shape("circle")
me.color("blue")
me.pencolor("blue")
me.penup()
me.goto(40,0)
me.pendown()
ve = turtle.Turtle()
ve.shape("circle")
ve.color("green")
ve.pencolor("green")
ve.penup()
ve.goto(60,0)
ve.pendown()
ea = turtle.Turtle()
ea.shape("circle")
ea.color("black")
ea.pencolor("black")
ea.penup()
ea.goto(80,0)
ea.pendown()
ma = turtle.Turtle()
ma.shape("circle")
ma.color("red")
ma.pencolor("red")
ma.penup()
ma.goto(90,0)
ma.pendown()
ju = turtle.Turtle()
ju.shape("circle")
ju.color("brown")
ju.pencolor("brown")
ju.penup()
ju.goto(150,0)
ju.pendown()
sa = turtle.Turtle()
sa.shape("circle")
sa.color("lightblue")
sa.pencolor("lightblue")
sa.penup()
sa.goto(180,0)
sa.pendown()
for t in range(1000):
        y = 40*math.sin(math.radians(t))
        x = 40*math.cos(math.radians(t))
        me.goto(x,y)
        y = 50*math.sin(math.radians(t))
        x = 55*math.cos(math.radians(t))+5
        ve.goto(x,y)
        y = 90*math.sin(math.radians(t))+5
        x = 80*math.cos(math.radians(t))
        ea.goto(x,y)
        y = 120*math.sin(math.radians(t))+10
        x = 90*math.cos(math.radians(t))
        ma.goto(x,y)
        y = 140*math.sin(math.radians(t))
        x = 150*math.cos(math.radians(t))
        ju.goto(x,y)
        y = 160*math.sin(math.radians(t))
        x = 175*math.cos(math.radians(t))+5
        sa.goto(x,y)
