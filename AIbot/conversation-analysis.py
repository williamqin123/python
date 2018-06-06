memory = {}

dictionary = {
	"is" : {
		"part-of-speech": "verb"
	},
	"Bob" : {
		"part-of-speech": "proper-noun"
	}
}

def findWordsPartOfSpeech(text, partOfSpeech):
	found = []
	words = text.split(" ")
	for word in words:
		if word in dictionary:
			if dictionary[word]["part-of-speech"] == partOfSpeech:
				found.append(word)

	return found

def partsOfSpeechText(text):
	words = text.split(" ")
	parsed = {}
	for word in words:
		if word in dictionary:
			parsed[word] = dictionary[word]["part-of-speech"]
		else:
			parsed[word] = "unknown"
	return parsed





def findPattern(data, desiredResult):
	stuff = []
	wordOccurances = {}
	for pair in data:
		input = pair[0]
		output = pair[1]
		if output == desiredResult:
			for word in input:
				stuff.append(word)
				if not word in wordOccurances:
					wordOccurances[word] = 0
				else:
					wordOccurances[word] += 1

	print(stuff)
	print(wordOccurances)

def findPatternInSentences(sentences):
	deconstructedSentences = []
	totalWords = []
	for sentence in sentences:
		words = sentence.split()
		deconstructedSentences.append(words)

	commonWords = deconstructedSentences[0]
	for sentence in deconstructedSentences:
		commonWords = set(commonWords).intersection(sentence)

	return commonWords

sampleSentences = [
	"Why are you cussing so much?",
	"Why are you pooping so much?",
	"Why are you stooping so much?"
]

def sentenceAnalysis(sentences):
	deconstructedSentences = []
	totalWords = []
	for sentence in sentences:
		words = sentence.split()
		deconstructedSentences.append(words)
		totalWords.extend(words)

	allWords = set(totalWords)
	results = []
	for word in allWords:
		clips = []
		for sentence in deconstructedSentences:
			if word in sentence:
				clips.append(sentence[sentence.index(word):])
		offset = 0
		exit = False
		while True:
			if exit == True:
				break
			for clip in clips:
				if offset >= len(clip):
					exit = True
					break
				if not clip[offset] == word:
					clip[offset] = "___"
			offset += 1
		results.extend(clips)
		print(clips)
	print(results)


sentenceAnalysis(sampleSentences)