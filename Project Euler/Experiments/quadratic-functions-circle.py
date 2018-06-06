import tkinter, math
canvas = tkinter.Canvas(width = 1000, height = 800)

def plot(x, y):
	canvas.create_oval(x, y, x + 5, y + 5)

for y in range(0, 10000):
	plot(math.sqrt(abs(10000 - y * y))+100, y+100)

canvas.pack()
input()