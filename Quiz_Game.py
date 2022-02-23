

print("Welcome to Quiz Game.")

#Line Break
print("")

#Ask the user if they would like to play Quiz Game.

start = input("Would you like to play Quiz game? (yes/ no) ").lower()

#If the user types no the game will quit. if they type yes the game will continue.
if start != "yes":
    quit()

#Line Break
print("")

print("Let's get started!!")

#Set a variable to keep score.
score = 0

#Line Break
print("")

#Ask the a series of questions, the users answer will turn to all lower case by using .lower at the end of the question.
#If the user gets the question correct they will receive 1 point, if the answer is wrong they will receive 0 points.
question1 = input("What is the name of the first Star Wars movie? ").lower()

if question1 == "new hope":
    print("Correct!!")
    score += 1

else:
    print("Incorrect.")

#Line Break
print("")

question2 = input("What is the jedi's weapon called? ").lower()

if question2 == "light saber":
    print("Correct!!")
    score += 1

else:
    print("Incorrect.")

#Line Break
print("")

question3 = input("What is the name of Star Wars Episode 1 movie? ").lower()

if question3 == "phantom menace":
    print("Correct!!")
    score += 1

else:
    print("Incorrect.")
    
#Line Break
print("")

question4 = input("What is the name of the goofy character the jedi met in Star Wars Episode 1? ").lower()

if question4 == "jar jar" or "jar jar binks": 
    print("Correct!!")
    score += 1

else:
    print("Incorrect.")
    
#Line Break
print("")

question5 = input("Who is princess Leia married to? ").lower()

if question5 == "han solo":
    print("Correct!!")
    score += 1

else:
    print("Incorrect.")

#Line Break    
print("")

question6 = input("Who is the famous green jedi? ").lower()

if question6 == "yoda":
    print("Correct!!")
    score += 1

else:
    print("Incorrect.")
   
#Line Break
print("")

question7 = input("What is the name of Darth Vader's grandson? ").lower()

if question7 == "kylo ren":
    print("Correct!!")
    score += 1

else:
    print("Incorrect.")
   
#Line Break
print("")

question8 = input("What is the name Anakin Skywalker's droid that he built? ").lower()

if question8 == "c3po":
    print("Correct!!")
    score += 1

else:
    print("Incorrect.")
   
#Line Break
print("")

question9 = input("What is the name of Anakin's droid when he is a jedi? ").lower()

if question9 == "r2d2":
    print("Correct!!")
    score += 1

else:
    print("Incorrect.")
   
#Line Break
print("")

question10 = input("What bounty hunter has his own show on Disney+? ").lower()

if question10 == "boba fett":
    print("Correct!!")
    score += 1

else:
    print("Incorrect.")
   
#Line Break
print("")

#Display the total number of question the user got correct.
print("You got " + str(score) + " questions correct!")