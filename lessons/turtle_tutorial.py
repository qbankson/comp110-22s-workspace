from turtle import Turtle, colormode, done
leo: Turtle = Turtle() 
i: int = 0
side_length: float = 300

colormode(255)
leo.pencolor(99, 204, 250)
leo.fillcolor(250, 250, 250)
leo.begin_fill()
while (i < 3):
    leo.backward(side_length)
    leo.rt(120)
    i += 1 
leo.end_fill()
N: int = 0
bob: Turtle = Turtle()
bob.pencolor(99 - 90, 204 - 190, 250 - 200)
while N < 5:
    i = 3
    while (i < 6):
        bob.backward(side_length)
        bob.rt(120)
        i += 1
    side_length = side_length * .95
    N += 1
done()