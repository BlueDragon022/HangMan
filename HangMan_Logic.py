import random
import Letter

#This function takes in a dictionary file and pics a random word
def chooseRanWord(dic):
	#First fine num of words in dictionary by splitting at the newline
	numWords = len(dic.split())
	#Return a random word from the dictionary
	return dic.split()[random.randrange(0,numWords)]

#This function returns an array of letter objects of a word
def toLetterArray(word):
	#Create a variable for the result to be added to
	result = []
	#Create an array of the chars in the word
	chars = list(word)
	#Loop thourgh each letter in the word
	for l in chars:
		#Append a letter object to the results array with the current letter in the loop
		result.append(Letter.letter(l))
	return result

#This function returns a string which is the word but with any non-guessed letters replaced with a "_"
def hideNotGuessedLetters(word):
	#This variable is where we will create the string
	result = ""
	#Loop through each letter
	for l in word:
		#Check if it has not been guessed
		if l.guessed == False:
			#If it has not been guessed append a "_" to the result
			result = result + "_"
		else:
			#Other wise the letter has been guessed so just add the letter to the resultant string
			result = result + l.letter
	#Finally return the formatted string
	return result

#This function adds n number of spaces to the begining of a string
def prependSpaces(n, string):
	#If we have a negative set to 0
	if n < 0:
		n = 0

	# Now we add each space individually
	for i in range(0,n,1):
		#Prepend the space
		string = " " + string
	return string
