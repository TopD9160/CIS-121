"""



"""



def main():
	
	DecodeWord()





#Your code goes here.
def DecodeWord():
	
	neww = ""
	#encodedWord = "WBLARF8TTS" #WATERFALLS
	encodedWord = "L8KAOUL" #TAKEOUT
	#encodedWord = "E8N8N8"
	#encodedWord = "8TRA8DY T8LA"
	#encodedWord = "8TT LHA TILLTA LIMAS"	
	#encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	#encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	#encodedWord = "UUHO"  		#Used for Bonus
	#encodedWord = "EOUUUUOUU" 	#Used for Bonus
	
	# for letter in word-goes through each letter
	# if's check for each letter

	for letter in encodedWord:
		if letter == "L":
			neww += "T"
		elif letter == "T":
			neww += "L"
		elif letter == "8":
			neww += "A"
		elif letter == "B":
			neww += "A"
		elif letter == "A":
			neww += "E"
		elif letter == "E":
			neww += "B"
		else:
			neww += letter
	print(neww)
	

		



















#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()
