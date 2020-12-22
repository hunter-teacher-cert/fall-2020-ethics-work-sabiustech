
def noAccount():
	print("Sorry, you may not make an account at this time because you do not meet the age requirement.")
	print("Goodbye!")
	print("**********************************************************************************************************************************************\n")
	print("END SESSION \n")

def exitNow():
	print("You have been securely logged out of your account. \n Thank you for visiting us.")
	print("Goodbye!")
	print("**********************************************************************************************************************************************\n")
	print("END SESSION \n")

def statusUpdate():
	print("status updates")

def makePost():
	print("make posts")

class User:

	numUsers = 0
	password_attempts = 0

	def __init__(self, first_name, last_name, age, email, userName, passwords):

		self.first = first_name
		self.last = last_name
		self.age = age
		self.email = email
		self.username = userName
		self.password = passwords



	def greetUser(self):
		# return '{} {}'.format("Welcome, " + self.first +  self.last)
		print("Welcome to 'SNAPFACE', " + self.first)




class Posts:

	def __init__(self, date, time, text):
		self.date = date
		self.time = time,
		self.text = []





def runProgram ():
	print(" ")
	print(" ")
	print("   SSSSSSSSSSSSSSS                                                      FFFFFFFFFFFFFFFFFFFFFF                                                         ")
	print("	SS:::::::::::::::S                                                     F::::::::::::::::::::F                                                         ")
	print("	S:::::SSSSSS::::::S                                                     F::::::::::::::::::::F                                                        ")
	print("	S:::::S     SSSSSSS                                                     FF::::::FFFFFFFFF::::F                                                        ")
	print("	S:::::S          nnnn  nnnnnnnn      aaaaaaaaaaaaa  ppppp   ppppppppp     F:::::F       FFFFFFaaaaaaaaaaaaa      cccccccccccccccc    eeeeeeeeeeee     ")
	print("	S:::::S          n:::nn::::::::nn    a::::::::::::a p::::ppp:::::::::p    F:::::F             a::::::::::::a   cc:::::::::::::::c  ee::::::::::::ee   ")
	print("	S::::SSSS       n::::::::::::::nn   aaaaaaaaa:::::ap:::::::::::::::::p   F::::::FFFFFFFFFF   aaaaaaaaa:::::a c:::::::::::::::::c e::::::eeeee:::::ee  ")
	print("		SS::::::SSSSS  nn:::::::::::::::n           a::::app::::::ppppp::::::p  F:::::::::::::::F            a::::ac:::::::cccccc:::::ce::::::e     e:::::e ")
	print("			SSS::::::::SS  n:::::nnnn:::::n    aaaaaaa:::::a p:::::p     p:::::p  F:::::::::::::::F     aaaaaaa:::::ac::::::c     ccccccce:::::::eeeee::::::e ")
	print("				SSSSSS::::S n::::n    n::::n  aa::::::::::::a p:::::p     p:::::p  F::::::FFFFFFFFFF   aa::::::::::::ac:::::c             e:::::::::::::::::e   ")
	print("							S:::::Sn::::n    n::::n a::::aaaa::::::a p:::::p     p:::::p  F:::::F            a::::aaaa::::::ac:::::c             e::::::eeeeeeeeeee   ")
	print("							S:::::Sn::::n    n::::na::::a    a:::::a p:::::p    p::::::p  F:::::F           a::::a    a:::::ac::::::c     ccccccce:::::::e            ")
	print("	SSSSSSS     S:::::Sn::::n    n::::na::::a    a:::::a p:::::ppppp:::::::pFF:::::::FF         a::::a    a:::::ac:::::::cccccc:::::ce::::::::e           ")
	print("	S::::::SSSSSS:::::Sn::::n    n::::na:::::aaaa::::::a p::::::::::::::::p F::::::::FF         a:::::aaaa::::::a c:::::::::::::::::c e::::::::eeeeeeee   ")
	print("	S:::::::::::::::SS n::::n    n::::n a::::::::::aa:::ap::::::::::::::pp  F::::::::FF          a::::::::::aa:::a cc:::::::::::::::c  ee:::::::::::::e   ")
	print("	SSSSSSSSSSSSSSS   nnnnnn    nnnnnn  aaaaaaaaaa  aaaap::::::pppppppp    FFFFFFFFFFF           aaaaaaaaaa  aaaa   cccccccccccccccc    eeeeeeeeeeeeee    ")
	print("																											p:::::p                                                                                           ")
	print("																											p:::::p                                                                                           ")
	print("																											p:::::::p                                                                                         ")
	print("																											p:::::::p                                                                                         ")
	print("																											p:::::::p                                                                                         ")
	print("																											ppppppppp                                                                                         ")

	print(" ")
	welcome1 = "Welcome to 'SnapFace'! "
	welcome2 = "The newest way to connect with your friends in the modern era!"
	print(welcome1.center(180).upper())
	print(welcome2.center(180).upper())
	print(" ")

	print("Select 1 to create an account or 2 to log in to your account:  " )
	try:
		pathwayDecision = int(input( ))

	except ValueError:
		print("You did not enter a number. \nProgram will automatically restart \n")
		runProgram()

	else:
		if pathwayDecision == 1:
			make_all()
		elif pathwayDecision == 2:
			logIn()
		else:
			print("Invalid entry. Program will restart")
			runProgram()


def createUser(userID):

		userID = User("first", "last", 0, "email", "username", "password")

		print("\nWhat is your first name? ")
		userID.first = input()
		print("\nWhat is your last name? ")
		userID.last = input()
		print("\nWhat is your age? ")
		try:
			userID.age = int(input())
		except ValueError:
			print("You did not enter a number. \nProgram will automatically restart \n")
			make_all()
		else:
			if userID.age <= 12:
				noAccount()
			else:
				print("\nWhat is your email? ")
				userID.email = input()
				print("\nPlease select a username: ")
				userID.username = input()
				print("\nPlease create a password that is both secure and easy for you to recall: ")
				print("(You will not see it as you type it, but it is still being recorded)")
				print(" ")
				userID.password = getpass.getpass()
				print("\nYou have successfully created an account with SNAPFACE! \nYou may now log in to your account to post messages!")
				userList.append(userID)





def make_all():

	print("How many accounts would you like to make?  \n" )

	try:
		numAccounts = int(input())

	except ValueError:
			print("You did not enter a number. \nProgram will automatically restart \n")
			make_all()

	else:
		for x in range(numAccounts):
			createUser(x)





def logIn():
	global passCount

	if passCount < 3:
		if len(userList) == 0:
			emptyAccounts = input("There are no accounts to log into. Please create an account prior to logging in. Type 'setup' to create an account now. \n" )

			if emptyAccounts.lower() == "setup":
				make_all()
			else:
				print(" You have chosen to NOT set up an account at this time. Please visit us soon. Thanks! \n")
		else:

			for x in range(len(userList)):
				userList[x].greetUser()
				print(" ")
				print(" ")
				print(" ")

			print("\n *****************************************************************************************")
			print("\n USER LOGIN SCREEN")
			print("\n Please type your username: ")
			userCredCheck = input()
			print("\n Please enter your password")
			userPassCheck = getpass.getpass()

			for each_user in userList:

				if each_user.username == userCredCheck and each_user.password == userPassCheck:
					print("\n  Welcome back, " + each_user.first + "!")
					print("Enter (1) to make a post, (2) to update your mood status, or (3) to exit program: ")

					try:
						postStatusExit = int(input())
					except ValueError:
						print("\n You must make a selection by entering 1, 2, or 3 only. Please log in again to continue \n")
						logIn()
					else:
							if postStatusExit == 3:
								exitNow()
							elif postStatusExit == 2:
								statusUpdate()
							elif postStatusExit == 1:
								makePost()
							else:
								print("\n You must make a selection by entering 1, 2, or 3 only. Please log in again to continue \n")
								logIn()


				else:
					passCount += 1
					print("\n Sorry, that username  and password combination is not recognized. Please try again.")
					print("\n ATTEMPTS REMAINING: " + str((3 - passCount )))
					logIn()

	else:
		print("You have been locked out of your account for 15 seconds. Please call customer service for further assistnace if you continue to experience difficulties. ")
		time.sleep(15)
		runProgram()






		# userNameLogIn = input()
		# print (userNameLogIn)



#store each instance of User()
userList = []



import datetime
import time
import getpass #library to hide password as it is typed
passCount = 0


runProgram()
logIn()
