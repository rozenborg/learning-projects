# all quiz text, answer banks, display messages, and dictionaries are listed here

'''quiz texts'''

quizCategoryBank = ["easy", "medium", "hard"]

quizEasyText = """Here's to the __1__ ones. The misfits. The rebels. The troublemakers.
The round pegs in the square holes. The ones who see things __2__.
They're not fond of rules. And they have no respect for the __3__.
You can quote them, disagree with them, glorify or vilify them.
About the only thing you can't do is __4__ them. Because they change things.
They push the human race forward. And while some may see them as the __1__ ones, we see __5__.
Because the people who are __1__ enough to think they can change the world, are the ones who do."""

quizMediumText = """Meaning and morality of One's life come from within __1__.
Healthy, strong individuals seek self expansion by experimenting and by living __2__.
Life consists of an __3__ number of possibilities and the healthy person
explores as many of them as __4__. Religions that teach pity,
self-contempt, humility, self-restraint and guilt are incorrect.
The __5__ life is ever changing, challenging, devoid of regret, intense, creative and risky."""

quizHardText = """The ideas of the ruling __1__ are in every epoch the ruling ideas,
i.e. the class which is the ruling material force of __2__,
is at the same time its ruling intellectual force.
The class which has the means of material production at its disposal,
has control at the same time over the means of mental __3__, so that thereby,
generally speaking, the ideas of those who lack the means of mental production are __4__ to it.
The ruling ideas are nothing more than the ideal expression of the dominant material relationships,
the __5__ material relationships grasped as ideas."""


'''answer banks'''

answersEasy = ["crazy", "differently", "status quo", "ignore", "genius"]
answersMedium = ["onesself", "dangerously", "infinite", "possible", "good"]
answersHard = ["class", "society", "production", "subject", "dominant"]


'''display messages'''

welcomeMessage = """Welcome to the powerful quotes fill-in-the-blanks quiz show!
You will be shown a quote with a handful of key words and phrases missing.
Follow the prompts to fill in the blanks.

Please select a powerful quote category from the following:"""
welcomeFail = "Sorry, that category does not exist. Please select from the following to begin: "
categoryList = " - " + "\n - ".join(quizCategoryBank)
answerCorrect = "That, my friend, is correct."
answerIncorrect = "Oof. Sorry bud, dat ain't right. Attempts remaining: "
winMessage = "You won! Hell yeah."
loseMessage = "Ehhh, sorry, you are out of tries. We still think you are beautiful. Not worthy... but beautiful :/ :')"


'''dictionaries'''

quizTexts = {
	"easy": quizEasyText,
	"medium": quizMediumText,
	"hard": quizHardText,
}

quizAnswers = {
	"easy": answersEasy,
	"medium": answersMedium,
	"hard": answersHard,
}

totalTries = 3

'''code'''

# the nextBlank function finds and displays the next blank in a text, or returns None if the quiz is complete

def nextBlank(blankIndex, selectedQuizText):

	blank = "__" + str(blankIndex + 1) + "__"
	if blank in selectedQuizText:
		return blank

# the categorySelection function displays the intro message, prompts for a difficult level choice.

def categorySelection(introMessage):

	while True:
		print "\n" + introMessage + "\n" + categoryList
		quizCategory = raw_input("\n" + "Your selection: ")
		if quizCategory in quizCategoryBank:

		# if a difficulty is selected, the selction is displayed and the quiz continues

			print "\n" + "You have chosen " + quizCategory + "." + "\n" + "\n" + "You will have three tries for each blank. Ride or die byatch!" + "\n" + "\n"
			return quizCategory

		# if a nonavailable option is selected, the user is notified and prompted to choose again.

		introMessage = welcomeFail

# the displayQuiz function prints the quiz text and updates it with correct answers to each blank,
# and also returns win or loss message if if the game is completed or the user runs out of tries

def displayQuiz(selectedQuizText, selectedAnswerBank):

	blankIndex = 0
# game is complete when there are no "nextBlank"s (because that means the text is completely filled with correct answers)

	while nextBlank(blankIndex, selectedQuizText) != None:
		blank = nextBlank(blankIndex, selectedQuizText)
		print selectedQuizText + "\n"

		# this section updates the quiztext when a correct answer is input

		selectedQuizText = checkAnswer(blankIndex, blank, selectedQuizText, selectedAnswerBank, totalTries)
		
		# or instead triggers loss if checkanswer returns that the user has run out o tries

		if selectedQuizText == False:
			return loseMessage
		blankIndex += 1
	print selectedQuizText
	return winMessage

# the checkAnswer function checks the inputed answer, determines whether it is correct,
# displays number of tries left for incorrect answers, and returns loss if user runs out of tries

def checkAnswer(blankIndex, blank, selectedQuizText, selectedAnswerBank, totalTries):

	triesLeft = totalTries
	while triesLeft > 0:

		# this selection elicits an answer

		answer = raw_input("What word or phrase belongs in " + str(blank) + ":  ")
		
		# if answer is incorrect, a try is removed

		if answer.lower() != selectedAnswerBank[blankIndex]:
			triesLeft -= 1
			print answerIncorrect + str(triesLeft)

		# if answer is correct, the quiz text is updated with the answer and the user is notified
		else:
			print answerCorrect
			selectedQuizText = selectedQuizText.replace(blank, answer)
			return selectedQuizText
	return False

def quiz(): 

# this section displays the intro message and prompts the user to select a difficulty (or 'category')
	
	quizCategory = categorySelection(welcomeMessage)

# the selected difficult/category is used to assign the appropriate text and answer bank

	selectedQuizText = quizTexts[quizCategory]
	selectedAnswerBank = quizAnswers[quizCategory]

# the process of displaying the quiz, and imbeded process of eliciting answers and verifying or penalizing until win or loss is carried out below

	return displayQuiz(selectedQuizText, selectedAnswerBank)

print quiz()
