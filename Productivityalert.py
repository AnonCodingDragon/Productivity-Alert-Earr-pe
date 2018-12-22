import webbrowser
import time
from pyfiglet import Figlet

anstoboot = input("Welcome to this short program that will try to make you stay awake! Type start and press enter to start the program: ")

if(anstoboot == "start" or anstoboot == " start" or anstoboot == "Start" or anstoboot == " Start"):

	persontypedno = False
	
	while True:
		
		ryoutired = input("Type yes and press enter if you're about to fall asleep ")
			
		if(ryoutired == "yes" or ryoutired == "Yes"):
			print("Opening browser...")
			webbrowser.open ("https://www.youtube.com/watch?v=s20Pn-eS3VA", new=1, autoraise=True)


if(anstoboot == "Dragonboi"): #easteregg
	f = Figlet(font='larry3d')
	print(f.renderText('AnonCodingDragon'))
	time.sleep(5)
	anstobootee = input("Congrats, you found this random easter egg! Type start and press enter to start the program: ")
	
	if(anstobootee == "start" or anstobootee == " start" or anstobootee == "Start" or anstobootee == " Start"):	
		
		persontypedno = False
	
		while True:
		
			ryoutired = input("Type yes and press enter if you're about to fall asleep ")
				
			if(ryoutired == "yes" or ryoutired == "Yes"):
				print("Opening browser...")
				webbrowser.open ("https://www.youtube.com/watch?v=s20Pn-eS3VA", new=1, autoraise=True)