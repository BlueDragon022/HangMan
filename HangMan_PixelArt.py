#Each of the following functions are the hang man pixel art for the lives lost
def hang0():
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
def hang1():
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("================")

def hang2():
	print ("")
	print ("||")
	print ("||")
	print ("||")
	print ("||")
	print ("||")
	print ("||")
	print ("================")

def hang3():
	print ("")
	print ("||")
	print ("||")
	print ("||")
	print ("||")
	print ("||")
	print ("||\\")
	print ("================")

def hang4():
	print ("")
	print ("||/")
	print ("||")
	print ("||")
	print ("||")
	print ("||")
	print ("||\\")
	print ("================")

def hang5():
	print ("===============")
	print ("||/")
	print ("||")
	print ("||")
	print ("||")
	print ("||")
	print ("||\\")
	print ("================")

def hang6():
	print ("===============")
	print ("||/          |")
	print ("||           0")
	print ("||")
	print ("||")
	print ("||")
	print ("||\\")
	print ("================")

def hang7():
	print ("===============")
	print ("||/          |")
	print ("||           0")
	print ("||           |")
	print ("||           |")
	print ("||")
	print ("||\\")
	print ("================")

def hang8():
	print ("===============")
	print ("||/          |")
	print ("||           0")
	print ("||          /|")
	print ("||           |")
	print ("||")
	print ("||\\")
	print ("================")

def hang9():
	print ("===============")
	print ("||/          |")
	print ("||           0")
	print ("||          /|\\")
	print ("||           |")
	print ("||")
	print ("||\\")
	print ("================")

def hang10():
	print ("================")
	print ("||/           |")
	print ("||            0")
	print ("||           /|\\")
	print ("||            |")
	print ("||           /")
	print ("||")
	print ("||\\")
	print ("================")

def hang11():
	print ("===============")
	print ("||/          |")
	print ("||           0")
	print ("||          /|\\")
	print ("||           |")
	print ("||          / \\")
	print ("||\\")
	print ("================")

#Since making each pixel art in an array of arrays would be more difficult it was easier just to make each in its own function and have a function which would select the correct one to print.
def printHangArt(n):
	if n == 0:
		hang0()
	elif n == 1:
		hang1()
	elif n == 2:
		hang2()
	elif n == 3:
		hang3()
	elif n == 4:
		hang4()
	elif n == 5:
		hang5()
	elif n == 6:
		hang6()
	elif n == 7:
		hang7()
	elif n == 8:
		hang8()
	elif n == 9:
		hang9()
	elif n == 10:
		hang10()
	elif n == 11:
		hang11()

