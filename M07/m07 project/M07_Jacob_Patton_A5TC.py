#!/usr/bin/env python3
#Name: Jacob Patton
#Class: (INFO 1200)
#Section: (X01)
#Professor: Say
#Date: 10/24/2021
#Project #: MO7_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.


TAX = 0.06 #sales tax percentage

def sales_tax(total): #receives total an parameter, returns total times Tax
    sales_tax = total * TAX #total sales tax
    return sales_tax #returns value

def main(): #main function
    print("Sales Tax Calculator\n") #displays app title
    valid = 'n' #used to determine if input is valid
    while valid == 'n': #runs until there is a valid input
        total = float(input("Enter total: ")) #sets total from user input
        if total <= 0: #if total is less than or equal to 0
            print("Total must be greater than 0") #print string
        else: #if total is greater than 0
            valid = 'y' #end loop
    total_after_tax = round(total + sales_tax(total), 2) #finds total after tax
    print("Total after tax: ", total_after_tax) #displays total after tax
    
if __name__ == "__main__": #runs main function
    main()
