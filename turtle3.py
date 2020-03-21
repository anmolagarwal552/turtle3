import turtle

t = turtle.Pen()
win = turtle.Screen()
win.bgcolor('black')
t.speed(-100)

colors = ['red','blue','green','yellow','orange','purple']

for i in range(360):
	t.pencolor(colors[i%6])
	t.width(i/100+1)
	t.forward(i)
	t.left(56)

turtle.listen()
turtle.mainloop()

