import turtle
import random

dict1={"Shape1":"square","Shape2":"triangle","Shape3":"circle"}
colors=["orange","red","green","blue","yellow"]

user_input= input("Enter the shape you desire to draw:")

turtle.color(random.choice(colors))
turtle.begin_fill()

for i in range(4):
    turtle.forawrd(100)
    turtle.left(90)
dict1.get("Shape2")==user_input     
for i in range(3):
    turtle.forawrd(100)
    turtle.left(120)
dict1.get("Shape2")==user_input     

turtle.circle()
