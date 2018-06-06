import random

shuffle = []
mylist = ["yo", "bro", "lol", "mo"]

fairTally = {"yo": 0, "bro": 0, "lol": 0, "mo": 0}
unfairTally = {"yo": 0, "bro": 0, "lol": 0, "mo": 0}

def fairRandomCycle():
	global shuffle, mylist
	if not shuffle:
		shuffle = list(mylist)
		random.shuffle(shuffle)
	returnValue = shuffle[0]
	shuffle = shuffle[1:]
	print(returnValue)
	fairTally[returnValue] += 1

def unfairRandomCycle():
	choice = random.choice(mylist)
	print(choice)
	unfairTally[choice] += 1

def fairRandom(times):
	for i in range(0, times):
		fairRandomCycle()

def unfairRandom(times):
	for i in range(0, times):
		unfairRandomCycle()

fairRandom(16)
print()
unfairRandom(16)

print(fairTally)
print(unfairTally)