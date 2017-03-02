#This function loads a file
def loadFile(file):
	#First open the file in read-only mode
	fileReader = open(file, "r")
	#Read the file's contents
	f = fileReader.read()
	#Close the file reader
	fileReader.close()
	#Return the contents of the file
	return f;
