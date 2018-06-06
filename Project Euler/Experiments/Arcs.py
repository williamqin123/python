import tkinter, math, time
velocity = 1
canvas = tkinter.Canvas(width = 600, height = 400)
position = [0, 0]

def setPosition():
	global oldPosition, position
	oldPosition = list(position)

setPosition()

def draw(point1, point2):
	global velocity, position
	position = [point1[0], point1[1]]
	setPosition()
	length = math.floor(math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2))
	count = 0
	originalVelocity = velocity
	while True:
		velocityObject = [point2[0] - position[0], point2[1] - position[1]]
		actualVelocity = velocityObject[0] / velocityObject[1]
		velocity = (originalVelocity * (length - count) + actualVelocity * count) / length
		margin = 4 / 1 + velocity ** 2
		xOffset = velocity * margin
		yOffset = margin
		position[0] += xOffset * (abs(velocityObject[0]) / velocityObject[0])
		position[1] += yOffset * (abs(velocityObject[1]) / velocityObject[1])

		canvas.create_line(oldPosition[0], oldPosition[1], position[0], position[1])
		setPosition()

		print(velocityObject)

		if count < length:
			count += 1

		if count >= length:
			break

		if round(position[0] / 10, 0) * 10 == round(point2[0] / 10, 0) * 10 and round(position[1] / 10, 0) * 10 == round(point2[1] / 10, 0) * 10:
			break


points = [[0, 0], [300, 200], [100, 300]]

for i in range(0, len(points)-1):
	draw(points[i], points[i+1])

canvas.pack()
input()