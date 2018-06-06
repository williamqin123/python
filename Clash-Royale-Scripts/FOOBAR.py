def answer(numbers):
	loop = []
	indices = []
	looping = False
	number = 0
	while True:
		number = numbers[number]
		if number in indices:
			looping = True
		if number in loop:
			return len(loop)
		if looping:
			loop.append(number)
		indices.append(number)

print(answer([1, 4, 0, 1, 3]))