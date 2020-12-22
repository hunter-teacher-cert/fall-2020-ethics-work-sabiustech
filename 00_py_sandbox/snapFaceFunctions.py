
def noAccount():
	print("Sorry, you may not make an account at this time.")
	print("Goodbye!")
	print("**********************************************************************************************************************************************")
	print("END SESSION")


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

		User.numUsers += 1
		User.password_attempts += 1

	def ageCheck (self):
		if self.age >= 13:
			return True
		else:
			return False



	def greetUser (self):
		return '{} {}'.format("Welcome, " + self.first, self.last)

	def passCheck (self, password_attempts):
		if password_attempts == 3:
			print("You have been locked out of your account. Please call customer service for further assistnace. ")





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

	# pathwayDecision = int(input("Select 1 to create an account or 2 to log in to your account:  " ))

	# if pathwayDecision == 1:
	# 	userList.append(createUser("test"))
	# elif pathwayDecision == 2:
	# 	logIn()
	# else:
	# 	print("Invalid entry. Program will restart")
	# 	runProgram()


def createUser(userID):
		userID = User("first", "last", 0, "email", "username", "password")

		print("\nWhat is your first name? ")
		userID.first = input()
		print("\nWhat is your last name? ")
		userID.last = input()
		print("\nWhat is your age? ")
		userID.age = int(input())

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
			userID.append(userID)


def make_all ():

	numAccounts = int(input("How many accounts would you like to make?  \n"))

	for x in range(numAccounts):
		createUser(x)








def logIn(userName):
	print("\nPlease type your username: ")
	userNameLogIn = input()
	print (userNameLogIn)



#store each instance of User()
userList = []



import datetime
import getpass
