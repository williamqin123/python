import random

sentences = ["hemophilia is a disease", "hemophilia could potentially be deadly", "hemophilia is not a common disease", "hemophilia is genetic"]

fillers = ["the previous fact clearly indicates this statement's credibility", "many people commonly believe the following sentence to be true"]

befores = ["Additionally, ", "Actually, ", "It is commonly said that "]

afters = [", which is true.", ", which is officially accepted."]

def extend():
	output = list(sentences)
	for sentence in sentences:
		output.insert(output.index(sentence) + 1, random.choice(fillers))

	for sentence in output:
		output[output.index(sentence)] = random.choice(befores) + sentence + random.choice(afters)

	print(output)

extend()