import time
import Letter
import fileLoader
import HangMan_Logic
import HangMan_PixelArt
import clearScreen

#This render function is used to call the pixel art rendering as well as printing the word/ spaces
def render(word, wrongAnswers):
	#Print pixel art first
	HangMan_PixelArt.printHangArt(wrongAnswers)
	
	#Now we generate the string to print but only we hide the not guessed letters
	printString = HangMan_Logic.hideNotGuessedLetters(word)	

	#To center the word in relation to the pixel art
	#Pixel art is 16 chars wide so (16-len(string))/2 gets spaces to prepend the string however -1 due to python automatically adding space later on
	printString = HangMan_Logic.prependSpaces(int((16 - len(printString))/2) - 1, printString)
	
	#At the end of the function we print the string of letters/ spaces
	print ("\n\n", printString)

#All code related to the game is in here and go off to other functions
def game():
	#Stores a letter array of the letters in a randomally choosen word from a file
	word = HangMan_Logic.toLetterArray(HangMan_Logic.chooseRanWord(fileLoader.loadFile("words-normal")))
	#Need a variable to hold how many wrong guesses for drawing pixel art and checking when game over for incorrectness
	wrongGuesses = 0
	#An array to store the letters already been tried by the user so they know what they've tried and so we don't count repeats as wrong guesses
	usedLetters = []
	#This is just so we can easily tell if the user has won the game by guessing the word correctly!!
	lettersGuessedRight = 0
	
	#Loop forever until the loop is broken out of as we do not know how long it would take them to guess correctly or loose...
	while True:
		#First of all we clear the screen each time so that it makes the program feel more polised instead of having text just printed one after the other in the terminal/console
		clearScreen.clearScreen()
	
		#Used to render the pixel art and the lines/letters guessed
		render(word, wrongGuesses)
		
		#Render letters that have already been guessed with newline to separate info out
		print ("\n\nYou have used these letters:")
		print (usedLetters)

		#Print two new line characters as space between guessed letters and input so easier to read
		print ("\n")

		#Ask the user for a letter and turn it to lower case for easy comparing as upper and lower have diff ascii vals
		letter = input ("Guess a letter! ").lower()

		#If the string inputed does not equal one char then we cant use that input
		if len(letter) != 1:
			#Tell them they can only guess a single letter
			print ("\n\nYou must type a single letter!")
			#Sleep for one second so they have time to read the message
			time.sleep(1)
			#Skip over rest of code and start at begining of loop as we do not want to use this input
			continue

		#We need to check if the character is an english character... we use the ascii values of letter typed
		if not ((ord(letter) >= 97 and ord(letter) <= 122) or (ord(letter) >= 65 and ord(letter) <= 90)):
			#If not english char then tell them
			print ("\n\nYou must type a letter from the english alphabet...")
			#Give them a second to read
			time.sleep(1)
			#Skip over rest of code and start at begining of loop as we do not want to use this input
			continue
		
		#We need a variable to hold if current guess was correct
		letterGuessedCorrectly = False

		#First check if they have already used the letter so that we can skip over code (efficiency)
		if letter not in usedLetters:
			#Loop through each letter in the word
			for l in word:
				#Check if the letter they guessed is the current letter in the word and it has not been guessed correctly already
				if letter == l.letter.lower() and l.guessed == False:
					#Set the letter to say that its been guessed therefore it will no longer be hiddened
					l.guessed = True
					#Inreament the letters guessed right by one
					lettersGuessedRight += 1
					#Set that this letter has been guessed correclty
					letterGuessedCorrectly = True
					#As we could have multiple of the same letter in one word we much check if we have already just added it to the used letters so that we do not have duplicates
					if letter not in usedLetters:
						#Append the letter to the used letters array
						usedLetters.append(letter)
			
			#Code for incorrect guessed
			if letterGuessedCorrectly == False:
				#Increment wrong guesses by one as this will change the pixel art and if they lost the game			
				wrongGuesses+=1
				#Also add the letter to the used letters
				usedLetters.append(letter)
		else:
			#Other wise we need to tell them that they have already used the letter
			print("\n\nYou have already used this letter!")
			#Give them a second to read
			time.sleep(1)

		#Check if they have guessed all letters correctly or had the max wrong guesses (10)
		if lettersGuessedRight == len(word) or wrongGuesses==11:
			#If so break out of the while loop
			break

	#First of all clear the screen to get rid of previous renderings
	clearScreen.clearScreen()
	
	#Code if won
	if lettersGuessedRight == len(word):
		#Render the hang man pixel art and the word
		render(word, wrongGuesses)
		#Give congratualtory msg
		print ("\n\nWell done you won!")
	#Code if lost
	elif wrongGuesses == 11:
		#Loop through each letter and set guessed to true so that it can be displayed
		for l in word:
			#Set so letter is displayed
			l.guessed = True
		#Render the hang man pixel art and the word (so they can see the answer)
		render(word, wrongGuesses)	
		#Tell the user they lost	
		print ("\n\nYou lost :(")

	#Input to stop it from going back to main menu streight away and so they can look at the answer
	input ("Press enter to continue!")

#This function contains all the code for the welcome screen
def welcomeScreen():
	#Loop for ever as we do not know when user wants to exit
	while True:
		#Clear the screen
		clearScreen.clearScreen()
		#Give a welcome message
		print("Welcome to hang man!")
		#String to store the option in
		option = ""		
		#Loop for ever as we do not know how many attempts it will take the user to type "play" or "quti"
		while True:
			#We will ask which option they want and convert it to lower case
			option = input("Type 'play' to play or 'quit' to quit: ").lower()
			#If they want to play
			if option == "play":
				#Start the game
				game()
				#Once the game ends it will return to here and we need to break out of the nested infinate loop to get back to the begining of welcome screen
				break
			#If the user wants to exit
			elif option == "quit":
				#Exit the program
				quit()
			else:
				#If not a valid option tell them and start from beginging of loop, asking for the option again.
				print ("That is not an option...\n")
#The program starts from the welcome screen function
welcomeScreen()
