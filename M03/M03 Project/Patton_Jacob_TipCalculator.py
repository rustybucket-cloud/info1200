#Name: Jacob Patton
#Class: INFO 1200
#Section: X01
#Professor: Say
#Date: 9/14/2021
#Project #:3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Jacob Patton Tip Calculator App") #display title
print() #empty line

costOfMeal = float(input("Cost of Meal: "))
tipPercentage = float(input("Tip Percentage: "))
print() #empty line

tipAmount = costOfMeal * (tipPercentage / 100)
print("Tip Amount: " + str(round(tipAmount, 2)))
print("Total Meal Cost: " + str(round(costOfMeal + tipAmount, 2)))
