successes = {}

def decision(question):
	return successes[question][len(successes[question]) - 1]

def trial():
	question = input()
	if not question in successes:
		successes[question] = ["I dunno"]
	attempt = decision(question)
	print(attempt)
	feedback = input()
	if feedback == "success":
		successes[question].append(attempt)
	else:
		successes[question].append(feedback)
	trial()

trial()