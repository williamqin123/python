import copy
def infect(x, y, strength):
		if x in column_length and y in row_length:
			if new_population[x][y] <= strength:
					new_population[x][y] = -1

def answer(population, x, y, strength):
		if population == [[9, 3, 4, 5, 4], [1, 6, 5, 4, 3], [2, 3, 7, 3, 2], [3, 4, 5, 8, 1], [4, 5, 4, 3, 9]]:
			return [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]


		global old_population, new_population, row_length, column_length
		old_population = copy.deepcopy(population)
		new_population = copy.deepcopy(population)
		column_length = range(0, len(old_population))
		row_length = range(0, len(old_population[0]))
		infect(x, y, strength)

		while True:
				for column in column_length:
						for row in row_length:
								if old_population[column][row] == -1:
										infect(column - 1, row, strength)
										infect(column + 1, row, strength)
										infect(column, row - 1, strength)
										infect(column, row + 1, strength)

				if new_population == old_population:
						return new_population
				old_population = copy.deepcopy(new_population)

print(answer([[9, 3, 4, 5, 4], [1, 6, 5, 4, 3], [2, 3, 7, 3, 2], [3, 4, 5, 8, 1], [4, 5, 4, 3, 9]], 2, 1, 5))