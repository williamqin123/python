import math
def permuCalc(pick, *args):
	dividend = 0

	divisor = 1
	for arg in list(args):

		dividend += arg

		arg2 = int(arg) #WHY IS IT A TUPLE?!?!?!?!?!?!?
		newNewArg = 0

		if pick < arg2:
			newNewArg = arg2 - pick

		newArg = math.factorial(arg2)/math.factorial(newNewArg)
		
		divisor *= newArg

	divisor *= math.factorial(dividend - pick)

	return math.factorial(dividend) / divisor

print (input())