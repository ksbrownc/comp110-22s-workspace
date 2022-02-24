
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# done()

leo.pen()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.color("blue")
colormode(225)
leo.color(225, 51, 228)

leo.begin_fill()
#code for shape to be filled
leo.end_fill()

leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()
bob.color("black")