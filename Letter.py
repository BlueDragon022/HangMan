#Create a class to store each letter so can easily get if guessed correctly
class letter:
	guessed = False
	letter = ''
	
	#Constructor
	def __init__(self, l):
		self.letter = l
