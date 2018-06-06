def patternMatch(sentences):
	deconstructedSentences = []
	totalWords = []
	for sentence in sentences:
		words = sentence.split()
		deconstructedSentences.append(words)
		totalWords.extend(words)
	allWords = set(totalWords)

	pattern = []
	patterns = []
	for word in allWords:
		offset = 0
		for x in range(0, 5):
			sentenceWords = []
			for sentence in deconstructedSentences:
				if word in sentence:
					wordPosition = sentence.index(word) + offset
					if wordPosition < len(sentence):
						sentenceWords.append(sentence[wordPosition])
			if len(set(sentenceWords)) == 1:
				pattern.append(sentenceWords[0])
			else:
				pattern.append("_")
			offset += 1
		patterns.append(list(pattern))
		pattern = []
	return patterns

print(patternMatch(["you suck so much bro", "you moron so much bro", "you slappo so much bro"]))