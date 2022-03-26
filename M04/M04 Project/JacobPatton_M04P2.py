#Name: Jacob Patton
#Class: INFO 1200
#Section: X01
#Professor: Say
#Date: 9/23/2021
#Project #: MO4_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Jacob Patton's Tip Calculator") #display title
print() #blank line

meal_cost = int(input("Cost of Meal: \t")) #set meal_cost to user input
print() #blank line

for i in range(3): #for loop that runs 3 times
    if i == 0: #if i is 0
        tip = 15 #tip set to 15
    elif i == 1: #if i is 1
        tip = 20 #tip set to 20
    elif i == 2: #if i is 2
        tip = 25 #tip set to 25
    
    tip_percent = tip / 100 #sets tip_percentage to tip divided by 100
    tip_amount = round(meal_cost * tip_percent, 2) #sets tip_amount to meal_cost times tip_percent, rounded to 2 decimals
    total = round(tip_amount + meal_cost, 2) #sets total to tip_amount plus meal_cost, rounded to 2 decimals

    print(tip, "%") #displays tip along with '%'
    print("Tip amount:\t", tip_amount) #displays tip_amount
    print("Total amount:\t", total) #displays total
    print() #empty line