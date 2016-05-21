'''quiz texts'''

quizCategoryBank = ["innovation", "existentialism", "power"]

quizInnovationText = """Here's to the __1__ ones. The misfits. The rebels. The troublemakers.
The round pegs in the square holes. The ones who see things __2__.
They're not fond of rules. And they have no respect for the __3__.
You can quote them, disagree with them, glorify or vilify them.
About the only thing you can't do is __4__ them. Because they change things.
They push the human race forward. And while some may see them as the __1__ ones, we see __5__.
Because the people who are __1__ enough to think they can change the world, are the ones who do."""

quizExistentialText = """Meaning and morality of One's life come from within __1__.
Healthy, strong individuals seek self expansion by experimenting and by living __2__.
Life consists of an __3__ number of possibilities and the healthy person
explores as many of them as __4__. Religions that teach pity,
self-contempt, humility, self-restraint and guilt are incorrect.
The __5__ life is ever changing, challenging, devoid of regret, intense, creative and risky."""

quizPowerText = """The ideas of the ruling __1__ are in every epoch the ruling ideas,
i.e. the class which is the ruling material force of __2__,
is at the same time its ruling intellectual force.
The class which has the means of material production at its disposal,
has control at the same time over the means of mental __3__, so that thereby,
generally speaking, the ideas of those who lack the means of mental production are __4__ to it.
The ruling ideas are nothing more than the ideal expression of the dominant material relationships,
the __5__ material relationships grasped as ideas."""


'''Answer Banks'''

answersInnovation = ["crazy", "differently", "status quo", "ignore", "genius", "crazy"]
answersExistentialism = ["onesself", "dangerously", "infinite", "possible", "good"]
answersPower = ["class", "society", "production", "subject", "dominant"]


'''display messages'''

welcome = """Welcome to the powerful quotes fill-in-the-blanks quiz show!
You will be shown a quote with a handful of key words and phrases missing.
Follow the prompts to fill in the blanks.

Please select a powerful quote category from the following:"""
welcomeFail = "Sorry, that category does not exist. Please select from the following to begin: "
answerCorrect = "\n" + "That, my friend, is correct."
answerIncorrect = "\n" + "Oof. Sorry bud, dat ain't right. Attempts remaining: "
winMessage = "\n" + "\n" + "You won! Hell yeah."
loseMessage = "\n" + "\n" + "Ehhh, sorry, you are out of tries. We still think you are beautiful. Not worthy... but beautiful :/ :')"


'''dictionaries'''

quizTexts = {
	"innovation": quizInnovationText,
	"existentialism": quizExistentialText,
	"power": quizPowerText,
}

quizAnswers = {
	"innovation": answersInnovation,
	"existentialism": answersExistentialism,
	"power": answersPower,
}


'''code'''

def nextBlank(blankIndex, selectedQuizText):
	blankIndex += 1
	# print "blankIndex: ", blankIndex
	# print "selectedQuizText: ", selectedQuizText
	blank = "__" + str(blankIndex) + "__"
	# print "blank: ", blank
	if blank in selectedQuizText:
		return blank

def quiz(): 

	introMessage = welcome
	while True:
		quizCategory = raw_input("\n" + introMessage + "\n" + " - " + "\n - ".join(quizCategoryBank) + "\n" + "\n" + "Your selection: ")
		if quizCategory.lower() in quizCategoryBank:
			break
		introMessage = welcomeFail #, ", ".join(quizCategoryBank)

	selectedQuizText = quizTexts[quizCategory]
	selectedAnswerBank = quizAnswers[quizCategory]

	print "\n" + "You have chosen " + quizCategory + "." + "\n" + "\n" + "You will have three tries for each blank. Ride or die byatch!"


# dear reviewer person: can you please give me guidance on how to refactor the code below?
	

	# while triesLeft > 0:
	blankIndex = 0
	triesLeft = 3
	while nextBlank(blankIndex, selectedQuizText) != None:
		if triesLeft == 0:
			return loseMessage
		print "\n" + "\n" + selectedQuizText + "\n" + "\n"
		response = raw_input("What word or phrase belongs in " + str(nextBlank(blankIndex, selectedQuizText)) + ":  ")
		if response.lower() != selectedAnswerBank[blankIndex]:
			triesLeft -= 1
			print answerIncorrect + str(triesLeft)
		else:
			print answerCorrect
			selectedQuizText = selectedQuizText.replace(nextBlank(blankIndex, selectedQuizText), response)
			blankIndex += 1
			triesLeft = 3
	return winMessage

print quiz()
