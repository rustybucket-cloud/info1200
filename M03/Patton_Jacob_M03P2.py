#!/usr/bin/env python3
print("Jacob Patton's Test Score App") #display full name and app title

# display a welcome message
print("The Test Scores program") #display App Title
print() #display blank line
print("Enter 3 test scores") #display directions
print("======================") #display horizontal line

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
score1 = int(input("Enter test score: ")) #declare and set user score variable as user input
score2 = int(input("Enter test score: ")) #declare and set user score variable as user input
score3 = int(input("Enter test score: ")) #declare and set user score variable as user input
total_score = score1 + score2 + score3 #set total_score to the sum of the 3 user inputs

# calculate average score
average_score = round(total_score / 3) #declare and set average_score to total_score divided by 3
             
# format and display the result
print("======================") #display a horizontal line
print("Your scores:   " + str(score1) + " " + str(score2) + " " + str(score3))
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score) #display total score and average score
print() #display blank line
print("Bye") #display string Bye
