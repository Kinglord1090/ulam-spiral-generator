import colorsys
import random
import turtle


keshar = turtle.Turtle()
value = 1
color = 0.5
flag = False
shapes = ["circle", "square", "triangle", "turtle", "classic"]


turtle.delay(0)
turtle.bgcolor("black")
keshar.speed(0)
keshar.pensize(1)
keshar.turtlesize(1)
keshar.hideturtle()
keshar.fillcolor("white")
keshar.shape(shapes[random.randrange(len(shapes))])
#turtle.tracer(0, 0)


if random.randrange(2) == 0:
	keshar.penup()

for i in range(1, 51):
	for j in range(i):
		keshar.color("white")
		keshar.forward(10)
		value += 1
		for x in range(2, value):
			if x <= int(value / 2):
				if value % x == 0:
					flag = True
					break
				else:
					i += 1
			else:
				break
		if flag != True:
			keshar.color(colorsys.hsv_to_rgb(color, 1, 1))
			keshar.stamp()
			color += random.randrange(5, 21) / 1000
		flag = False
	keshar.left(90)

#turtle.update()
turtle.done()
