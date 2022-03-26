#!/usr/bin/env python3

def display_welcome(): # displays welcome message
    print("The Test Scores program") # displays title
    print("Enter 'x' to exit") # displays instructions to exit
    print("") # empty line

def get_scores(): # gets all the scores and returns a list
    scores = [] # creates scores list
    while True: # keeps running until user enter 'x'
        score = input("Enter test score: ") # creates variable from input to be appended to scores list
        if score == "x": # if user has no more scores to enter
            return  scores # returns scores list
        else: # if user has more scores to enter
            score = int(score) # converts score to integer
            if score >= 0 and score <= 100: # if score is between 0 and 100
               scores.append(score) # add score to scores list
            else: # if user error
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.") # displays error message

def process_scores(scores): # processes the score
    # calculate average score
    total = 0 # creates total variable
    for i in range(len(scores)): # runs for each item in scores
        total += scores[i] # adds each score to total
    average = total / len(scores) # calculates average score
    maxValue = max(scores) # finds highest score
    minValue = min(scores) # finds lowest score

    median = 0 # declares median variable
    scores.sort() # sorts scores in order
    index = len(scores) // 2 # finds index to be used to find median
    if len(scores) % 2 != 0: # if scores list has an odd number of scores
        median = scores[index] # defines median
    else: # if sccores list has an even number of scores
        median = sum(scores[index - 1: index + 1]) / 2 # calculates median


                
    # format and display the result
    print() # empty line
    print("Score total:       ", total) # displays score total
    print("Number of Scores:  ", len(scores)) # displays number of scores
    print("Average Score:     ", average) # displays average score
    print("Median:            ", median) # displays median score
    print("Max Score:         ", maxValue) # displays highest score
    print("Min Score:         ", minValue) # displays lowest score

def main(): # main function
    display_welcome() # displays welcome message
    scores = get_scores() # gets scores from user inputs
    process_scores(scores) # calculates mean, median, min, and max of scores
    print("") # displays empty line
    print("Bye!") # bye message

# if started as the main module, call the main function
if __name__ == "__main__":
    main()