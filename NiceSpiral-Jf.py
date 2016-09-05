import turtle
t = turtle.Pen()
t.speed(0)
colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange']
sides = 6
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%sides])
	t.width(x/100+1)
	t.forward(x)
	t.left(92)
