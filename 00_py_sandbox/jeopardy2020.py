def quickStart():

	print("     _____                                                          __            ")
	print("    |     \                                                        |  \           ")
	print("     \$$$$$  ______    ______    ______    ______    ______    ____| $$ __    __  ")
	print("       | $$ /      \  /      \  /      \  |      \  /      \  /      $$|  \  |  \ ")
	print("  __   | $$|  $$$$$$\|  $$$$$$\|  $$$$$$\  \$$$$$$\|  $$$$$$\|  $$$$$$$| $$  | $$ ")
	print(" |  \  | $$| $$    $$| $$  | $$| $$  | $$ /      $$| $$   \$$| $$  | $$| $$  | $$ ")
	print(" | $$__| $$| $$$$$$$$| $$__/ $$| $$__/ $$|  $$$$$$$| $$      | $$__| $$| $$__/ $$ ")
	print("  \$$    $$ \$$     \ \$$    $$| $$    $$ \$$    $$| $$       \$$    $$ \$$    $$ ")
	print("   \$$$$$$   \$$$$$$$  \$$$$$$ | $$$$$$$   \$$$$$$$ \$$        \$$$$$$$ _\$$$$$$$ ")
	print("                               | $$                                    |  \__| $$ ")
	print("                               | $$                                     \$$    $$ ")
	print("                                \$$                                      \$$$$$$  ")
	print(" ")
	print(" ")

	print(" ")
	print("  +-------------+--------------+-------------+-------------+-------------+-------------+  ")
	print("  |   World     |   Number     |   Double    |    Body     |  Fruits &  |             |  ")
	print("  |  Capitals   |   Please     |    Talk     |  Language   |  Vegetables |  Mythology  |  ")
	print("  |             |              |             |             |             |             |  ")
	print("  +-------------+--------------+-------------+-------------+-------------+-------------+  ")
	print("  |             |              |             |             |             |             |  ")
	print("  |    $200     |    $200      |    $200     |    $200     |    $200     |    $200     |  ")
	print("  |             |              |             |             |             |             |  ")
	print("  +-------------+--------------+-------------+-------------+-------------+-------------+  ")
	print("  |             |              |             |             |             |             |  ")
	print("  |    $400     |    $400      |    $400     |    $400     |    $400     |    $400     |  ")
	print("  |             |              |             |             |             |             |  ")
	print("  +-------------+--------------+-------------+-------------+-------------+-------------+  ")
	print("  |             |              |             |             |             |             |  ")
	print("  |    $600     |    $600      |    $600     |    $600     |    $600     |    $600     |  ")
	print("  |             |              |             |             |             |             |  ")
	print("  +-------------+--------------+-------------+-------------+-------------+-------------+  ")
	print("  |             |              |             |             |             |             |  ")
	print("  |    $800     |    $800      |    $800     |    $800     |    $800     |    $800     |  ")
	print("  |             |              |             |             |             |             |  ")
	print("  +-------------+--------------+-------------+-------------+-------------+-------------+  ")
	print("  |             |              |             |             |             |             |  ")
	print("  |   $1000     |   $1000      |   $1000     |   $1000     |   $1000     |   $1000     |  ")
	print("  |             |              |             |             |             |             |  ")
	print("  +-------------+--------------+-------------+-------------+-------------+-------------+  ")

	print(" ")
	print("Welcome to Jeopardy! Thanks for playing!")

	print("Your starting score total is $" + str(score) + ". Let's begin!")
	print(" ")

	quesCat()




def quesCat():
		quesCategory = input("Please enter the category you would like to try: ")
		if quesCategory.lower() == "world capitals":
			list_Of_Ques(world_capitals)
		elif quesCategory.lower() == "number please":
			list_Of_Ques(number_please)
		elif quesCategory.lower() == "double talk":
			list_Of_Ques(double_talk)
		elif quesCategory.lower() == "body language":
			list_Of_Ques(body_language)
		elif quesCategory.lower() == "fruits & vegetables":
			list_Of_Ques(fruits_n_veggies)
		elif quesCategory.lower() == "mythology":
			list_Of_Ques(mythology)
		else:
			print("Sorry, invalid entry! Let's start again.")
			time.sleep(2)
			quickStart()


def list_Of_Ques(listName):
	global score, quesNum, endGameCounter

	if endGameCounter == 29:
		print("You have selected all available categories and their respective values. Thank you for playing.")
		print("Your final score is: $" + str(score))

	else:

		quesValue = int(input("Now select a dollar amount, please: $  "))

		if quesValue == 200 or quesValue == 400 or quesValue == 600 or quesValue == 800 or quesValue == 1000:

			randomQuesNum = random.randrange(len(listName))
			userAns = input(listName[randomQuesNum]["question"] + ": " )

			if userAns.lower() == listName[randomQuesNum]["answer"].lower():
				endGameCounter += 1
				score += listName[randomQuesNum]["value"]
				print("You are correct! Great work! The question was worth $" + str(listName[randomQuesNum]["value"]))
				print("Your total score is $" + str(score))
				print()
				print(" ")
				quesCat()

			else:

				endGameCounter += 1
				score -= listName[randomQuesNum]["value"]
				print("Sorry, that's incorrect! The right answer is: " + listName[randomQuesNum]["answer"].lower())
				print("The question was worth $" + str(listName[randomQuesNum]["value"]))
				print("Your total score is $" + str(score))
				print(" ")
				quesCat()

		else:
			print("Sorry, you entered the wrong value. Please try again.")
			time.sleep(1)
			quesCat()









import requests
import random
import similar_text
import time

#global variables
score = 0
quesNum = 30
endGameCounter = 0

#imported lists & dictionaries 1
response = requests.get('http://jservice.io/api/clues?category=139').json()

first_ten = requests.get('http://jservice.io/api/categories?count=10').json()
first_fifty = requests.get('http://jservice.io/api/categories?count=50').json()

# print(response)
# print(" ")
# print(response[0]["question"])
# print(len(response))

#---------------------------------------------------------------------------------------------------------------------#

# #Level 1 -3

# print(" ")
# score = 0

# randomQuesNum = random.randrange(len(response))
# for x in range (len(response)):
# 	userAns = input(response[x]["question"] + ": " )
# 	if userAns.lower() == response[x]["answer"].lower():
# 		score += response[x]["value"]
# 		print("You are correct! Great work! The question was worth $" + str(response[x]["value"]))
# 		print("Your total score is $" + str(score))
# 		print()
# 		print(" ")
# 	else:
# 		score -= response[x]["value"]
# 		print("Sorry, that's incorrect! The right answer is: " + response[x]["answer"].lower())
# 		print("The question was worth $" + str(response[x]["value"]))
# 		print("Your total score is $" + str(score))
# 		print(" ")

# #similar text missing ADD LATER


#---------------------------------------------------------------------------------------------------------------------#



# #Level 4

#imported lists & dictionaries 2
world_capitals = requests.get('http://jservice.io/api/clues?category=78').json()
number_please = requests.get('http://jservice.io/api/clues?category=1195').json()
double_talk = requests.get('http://jservice.io/api/clues?category=89').json()
body_language = requests.get('http://jservice.io/api/clues?category=897').json()
fruits_n_veggies = requests.get('http://jservice.io/api/clues?category=777').json()
mythology = requests.get('http://jservice.io/api/clues?category=680').json()


# # #similar text missing ADD LATER
quickStart()
