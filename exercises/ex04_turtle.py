"""Python Skills Can Make You Money."""

__author__ = "730319713"


from turtle import Turtle, colormode, done 


def main() -> None:
    """Money Maker."""
    # main function, drawing functions

    mturtle: Turtle = Turtle()
    circturtle: Turtle = Turtle()
    tinycirc: Turtle = Turtle()
    portrait: Turtle = Turtle()
    mturtle.speed(0)
    circturtle.speed(0)
    tinycirc.speed(10)
    drawrectangle(mturtle, -200, 200, 200, 400)
    cashamount(circturtle, -175, 155, 20)
    value(tinycirc, -190, 175, 3, 8)
    cashamount(circturtle, 175, 155, 20)
    value(tinycirc, 160, 175, 3, 8)
    cashamount(circturtle, -175, 15, 20)
    value(tinycirc, -190, 35, 3, 8)
    cashamount(circturtle, 175, 15, 20)
    value(tinycirc, 160, 35, 3, 8)
    value(tinycirc, 125, 120, 3, 12)
    # draw something twice^
    cashamount(circturtle, 0, 45, 60)
    circturtle.penup()
    face(portrait, 0, 75, "grey")
    # nested function within face^
    done()


def drawrectangle(iturtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws a green rectangle."""
    colormode(255)
    iturtle.penup()
    iturtle.goto(x, y) 
    iturtle.setheading(0.0)
    iturtle.pendown()
    iturtle.fillcolor(43, 134, 83)
    # fill color
    iturtle.begin_fill()
    i: int = 0
    while i < 2:
        iturtle.fd(height)
        iturtle.right(90)
        iturtle.fd(width)
        iturtle.right(90)
        i = i + 1
        # loop usage:
    iturtle.end_fill()


def cashamount(circturtle: Turtle, x: float, y: float, radius: int) -> None:
    """Draws a circle in corner of cash."""
    circturtle.penup()
    circturtle.goto(x, y)
    circturtle.pendown()
    circturtle.circle(radius)
    circturtle.penup()


def value(tinycirc: Turtle, x: float, y: float, digits: int, size: int) -> None:
    """Draws dots to represent amount of digits on bill."""
    tinycirc.penup()
    tinycirc.goto(x, y)
    tinycirc.pendown()
    N: int = 0
    while N < digits:
        N = N + 1
        tinycirc.dot(size, "black")
        tinycirc.penup()
        tinycirc.goto(x + (10 * N), y)
        tinycirc.pendown()
    tinycirc.penup()
    

def face(portrait: Turtle, x: int, y: int, haircolor: str) -> None:
    """Draws a presidential portrait."""
    colormode(255)
    portrait.penup()
    portrait.goto(x, y)
    portrait.pencolor(82, 82, 82)
    # marker color^
    portrait.pendown()
    portrait.circle(35, extent=None, steps=None)
    portrait.penup()
    portrait.goto(-15, 120)
    portrait.pendown()
    portrait.dot(12, (82, 82, 82))
    portrait.penup()
    portrait.goto(15, 120)
    portrait.pendown()
    portrait.dot(12, (82, 82, 82))
    portrait.penup()
    portrait.goto(0, 115)
    portrait.pendown()
    portrait.setheading(315)
    portrait.fd(15)
    portrait.setheading(225)
    portrait.fd(15)
    portrait.penup()
    portrait.goto(-10, 85)
    portrait.setheading(0)
    portrait.pendown()
    portrait.fd(20)
    portrait.penup()
    portrait.goto(-15, 79)
    portrait.setheading(270)
    portrait.pendown()
    portrait.fd(15)
    portrait.setheading(240)
    portrait.fd(20)
    portrait.penup()
    portrait.goto(15, 79)
    portrait.setheading(270)
    portrait.pendown()
    portrait.fd(15)
    portrait.setheading(300)
    portrait.fd(20)
    portrait.penup()
    folicle: Turtle = Turtle()
    hair(folicle, haircolor)


def hair(folicle: Turtle, hairs: str) -> None:
    """Add hair to the portrait, with color choice."""
    # tried something fun using the dot feature and a loop:
    # gave hair color as a parameter to be changed for fun:
    h: int = 0
    folicle.penup()
    while h < 6:
        folicle.goto(-20 + h * 8, 135)
        folicle.pendown()
        folicle.dot(15, hairs)
        h = h + 1
    h2: int = 0
    folicle.penup()
    while h2 < 7:
        folicle.goto(-20 + h2 * 6, 140)
        folicle.pendown()
        folicle.dot(10, hairs)
        folicle.penup()
        h2 = h2 + 1


if __name__ == "__main__":
    main()