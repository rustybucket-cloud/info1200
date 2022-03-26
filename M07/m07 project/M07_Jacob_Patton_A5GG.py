#!/usr/bin/env python3
#Name: Jacob Patton
#Class: (INFO 1200)
#Section: (X01)
#Professor: Say
#Date: 10/24/2021
#Project #: MO7_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.


import random #import random module

def display_title(): #displays title
    print("Guess the number!") #title
    print() #empty line

def get_limit(): #gets and returns the upper limit fot the range
    valid =  'n' #'n' if not valid, 'y' if valid
    while valid == 'n': #runs until upper limit is valid
        limit = int(input("Enter the upper limit for the range of numbers: ")) #sets limit from user input
        if limit <= 1: #if limit is less than or equal to 1
            print("Upper limit must be greater than 1") #displays string
        else: #if limit is greater than 1
            valid = 'y' #changes valid to 'y'
    return limit #returns upper limit

def play_game(limit): #plays guessing game, has upper limit as parameter
    number = random.randint(1, limit) #sets number at random int between 1 and upper limit
    print(f"I'm thinking of a number from 1 to {limit}\n") #prints string and upper limit
    count = 1 #number of guesses
    
    while True: #runs on loop until user guesses correctly  
        guess = int(input("Your guess: ")) #sets guess from user input
        if guess < number: #if guess is lower than the number
            print("Too low.") #display string too low
            count += 1 #adds 1 to number of guesses
        elif guess > number: #if guess is higher than number
            print("Too high.") #display string too high
            count += 1 #add one to guesses
        elif guess == number: #if guess equals number
            print(f"You guessed it in {count} tries.\n") #display string and number of guesses
            return #end loop

def main(): #main function
    display_title() #displays title
    
    again = "y" #declairs again function to start
    while again.lower() == "y": #while again is y
        limit = get_limit() #sets limit to get limit function
        play_game(limit) #runs play_game function, passes limit variable
        
        again = input("Play again? (y/n): ") #run again if user selects y, ends if user selects n
        print() #empty row
    print("Bye!") #displays bye

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

