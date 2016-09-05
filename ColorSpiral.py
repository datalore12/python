import turtle
t = turtle.Pen()
colors=["red","yellow","blue","green", "purple", "orange"]
turtle.bgcolor("black")
sides = 6
t.speed(0)
for x in range(500):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides + x)
    t.left(360/sides+1)
    t.width(x*sides/200)
