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

print("Jacob Patton Pay Check Calculator App") #display app title
print() #empty line

#inputs
hoursWorked = float(input("Hours worked: ")) #input hours worked
payRate = float(input("Pay Rate: ")) #input pay rate
print() #empty line

#gross pay
grossPay = round(hoursWorked * payRate, 2) #calculate gross pay
print("Gross Pay: " + str(grossPay)) #display gross pay

#tax rate and amount
taxRate = 18 #set tax rate
print("Tax rate: " + str(taxRate) + "%") #display tax rate
taxAmount = round(grossPay * (taxRate / 100), 2) #calculate tax amount
print("Tax Amount: " + str(taxAmount)) #display tax amount

#take home pay
takeHomePay = round(grossPay - taxAmount, 2) #calculate take home pay
print("Take Home Pay: " + str(takeHomePay)) #display take home pay


