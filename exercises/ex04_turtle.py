"""EX04- A SUNNY DAY AT THE BEACH."""

__author__ = "730327035"


from turtle import Turtle, colormode, done
import turtle
colormode(255)


beach = turtle.Screen()
beach.bgcolor(212, 230, 241)
beach.title("A beautiful Day at the beach <3")


def main() -> None:
    """Setting the variables for the scene of a sunny day at the beach."""
    beachball_fun: Turtle = Turtle()  
    draw_beachball(beachball_fun, -400, -88, 30)
    draw_beachball(beachball_fun, -300, -88, 40)
    tan_sand: Turtle = Turtle()
    draw_sand(tan_sand, -700, -99, 50)
    bright_sun: Turtle = Turtle()
    draw_sun(bright_sun, 340, 100, 80)
    blue_water: Turtle = Turtle()
    draw_water(blue_water, -199, -99, 800)
    done()


def draw_beachball(beachball_fun: Turtle, x: float, y: float, width: float) -> None:
    """Drawing beach balls that are high in the sun."""
    beachball_fun.pencolor("blue")
    beachball_fun.pensize(10)
    beachball_fun.penup()
    beachball_fun.goto(x, y)
    beachball_fun.pendown()
    beachball_fun.begin_fill()
    beachball_fun.fillcolor("red")
    beachball_fun.circle(width)
    beachball_fun.end_fill()


def draw_sand(tan_sand: Turtle, x: float, y: float, width: float) -> None:
    """Draw sand of the given width whose color is sand and is the land."""
    tan_sand.penup()
    tan_sand.pensize(10)
    tan_sand.goto(x, y)
    tan_sand.setheading(0.0)
    tan_sand.pendown()
    tan_sand.pencolor(226, 192, 112)
    tan_sand.begin_fill()
    tan_sand.fillcolor(226, 192, 112)
    i: int = 0
    while (i < 4):
        tan_sand.forward(500)
        tan_sand.forward(width)
        tan_sand.right(90)
        i = i + 1
    tan_sand.end_fill()


def draw_sun(bright_sun: Turtle, x: float, y: float, width: float) -> None:
    """Draw a bright yellow sun in front of the first red beach ball over the water."""
    bright_sun.penup()
    bright_sun.color("yellow")
    bright_sun.goto(x, y)
    bright_sun.pendown()
    bright_sun.begin_fill()
    bright_sun.fillcolor("yellow")
    bright_sun.circle(40)
    bright_sun.circle(width)
    bright_sun.end_fill()
    

def draw_water(blue_water: Turtle, x: float, y: float, width: float) -> None:
    """Next to the sand lies the blue water below the sun."""
    blue_water.penup()
    blue_water.pencolor("blue")
    blue_water.goto(x, y)
    blue_water.pendown()
    blue_water.begin_fill()
    blue_water.fillcolor("blue")
    i: int = 0
    while (i < 4):
        blue_water.forward(700)
        blue_water.right(90)
        i = i + 1
    blue_water.end_fill()


if __name__ == "__main__":
    main()
