left = []
right = []
def append():
	list.append(string[previous_stop:index])

def parse(argument):
	index = 0
	previous_stop = index
	string = argument.replace(" ", "")
	list = left
	for character in string:
		if character == "-" or character == "+":
			append()
			previous_stop = index + ["-", "+"].index(character)
		index += 1
		if character == "=" or index == len(string):
			append()
			list = right

parse("2x + 3x + 8 - 10 = 20 + x")
print(left + right)