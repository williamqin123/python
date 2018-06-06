def intInput(string):
	return int(input(string))
def avg(numbers):
	total = 0
	for number in numbers:
		total += number
	average = total / len(numbers)
	return average
trophies = intInput("Trophies: ")
highestTrophies = intInput("Highest trophies: ")
wins = intInput("Wins: ")
trophyWinLoseAmount = 30
winsToGetCurrentTrophies = trophies / trophyWinLoseAmount
lossesToGetToZeroTrophies = trophies / trophyWinLoseAmount
trophyDifference = highestTrophies - trophies
lossesBecauseOfTrophyDifference = trophyDifference / trophyWinLoseAmount
losses = wins - lossesToGetToZeroTrophies + lossesBecauseOfTrophyDifference
totalBattles = wins + losses
print("Winning rate: %f" % (wins / totalBattles))
print("Losing rate: %f" % (losses / totalBattles))
print("Battles won: %f" % wins)
print("Battles lost: %f" % losses)
print("Total battles: %f" % totalBattles)