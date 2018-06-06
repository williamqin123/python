import tkinter, math
canvas = tkinter.Canvas(width = 600, height = 400)

def parse(expression):
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
	expression = " %s " % expression
	for i in range(0, len(expression)):
		for m in numbers:
			if expression[i] == m:
				for g in alphabet:
					cut1 = expression[i + 1]
					cut2 = expression[i - 1]
					cut3 = expression[:i + 1]
					cut4 = expression[:i]
					cut5 = expression[i + 1:]
					cut6 = expression[i:]
					if cut1 == g:
						expression = cut3 + "*" + cut5
					if cut2 == g:
						expression = cut4 + "**" + cut6
	return "global x; global y; " + expression.strip()

def horizontal(equation, start, end, step):
	old = [-9999, -9999]
	global x, y
	x = start
	while x < end:
		parsed = parse(equation)
		exec(parsed)
		xValues = [old[0], (x * 50) + 300]
		yValues = [old[1], 200 - (y * 50)]
		canvas.create_line(xValues[0], yValues[0], xValues[1], yValues[1])
		old = [xValues[1], yValues[1]]
		x += step

def vertical(equation, start, end, step):
	old = [-9999, -9999]
	global x, y
	y = start
	while y < end:
		parsed = parse(equation)
		exec(parsed)
		xValues = [old[0], (x * 50) + 300]
		yValues = [old[1], 200 - (y * 50)]
		canvas.create_line(xValues[0], yValues[0], xValues[1], yValues[1])
		old = [xValues[1], yValues[1]]
		y += step
canvas.pack()

backgroundGrid = tkinter.PhotoImage(file = "grid.gif")
canvas.create_image(0, 0, image = backgroundGrid, anchor = "nw")

while True:
	formula = input("Quadratic Equation:")
	# horizontal("y = x2", -5, 5, 0.1)
	# vertical("x = y2", -5, 5, 0.1)
	# horizontal("y = x3", -5, 5, 0.1)
	# vertical("x = y3", -5, 5, 0.1)
	exec(formula)
	# horizontal("y = x3", -5, 5, 0.1)
	# vertical("x = y3", -5, 5, 0.1)
	# horizontal("y = -x3", -5, 5, 0.1)
	# vertical("x = -y3", -5, 5, 0.1)

	# horizontal("y = x2", -5, 5, 0.1)
	# vertical("x = y2", -5, 5, 0.1)
	# horizontal("y = -x2", -5, 5, 0.1)
	# vertical("x = -y2", -5, 5, 0.1)
