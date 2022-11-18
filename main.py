"""
ITS 1801 F22 Exam 03
Solution
"""

import turtle

casper = turtle.Turtle()
piper = turtle.Turtle()
hazel = turtle.Turtle()

casper.shape("turtle")
piper.shape("triangle")
hazel.shape("classic")

piper.penup()
piper.goto(-150,0)
hazel.penup()
hazel.goto(150,0)
piper.pendown()
hazel.pendown()

def square(turtleName,lineColor):
  turtleName.color(lineColor)
  for i in range(4):
    turtleName.forward(50)
    turtleName.left(90)

def triangle(turtleName,lineColor):
  turtleName.color(lineColor)
  for i in range(3):
    turtleName.forward(50)
    turtleName.left(120)

def circle(turtleName,lineColor):
  turtleName.color(lineColor)
  turtleName.circle(50)


print("This program has three turtles: Piper (left), Casper (middle) and Hazel (right)")
print("Piper draws squares, Casper triangles and Hazel circles.")
choiceTurtleStr = input("Select a turtle (0) Piper (1) Casper (2) Hazel: ")
choiceColorStr = input("Select a color (0) yellow, (1) blue, (2) red: ")

colorList = ["yellow", "blue", "red"]

choiceColorInt = int(choiceColorStr)

if choiceTurtleStr == '0':
  square(piper, colorList[choiceColorInt])
elif choiceTurtleStr == '1':
  triangle(casper, colorList[choiceColorInt])
elif choiceTurtleStr == '2':
  circle(hazel, colorList[choiceColorInt])
else:
  print("Invalid choice, turtle should be between 0 and 2")