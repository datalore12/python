import turtle
t = turtle.Pen()
colors=["red","yellow","blue","green"]
turtle.bgcolor("black")
for x in range(100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
