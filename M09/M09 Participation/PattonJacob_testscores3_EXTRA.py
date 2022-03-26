#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox
import re

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

    class Data: # creates class of data that will be returned as object
        def __init__(self, total, num, median, mean, max, min):
            self.total = total
            self.num = num
            self.median = median
            self.mean = mean
            self.max = max
            self.min = min

    return Data(total, len(scores), median, average, maxValue, minValue) # data to be returned to create GUI
                
    # format and display the result
    print() # empty line
    print("Score total:       ", total) # displays score total
    print("Number of Scores:  ", len(scores)) # displays number of scores
    print("Average Score:     ", average) # displays average score
    print("Median:            ", median) # displays median score
    print("Max Score:         ", maxValue) # displays highest score
    print("Min Score:         ", minValue) # displays lowest score


def main(): # main function
    root = tk.Tk()
    root.title("Test Score Calculator")
    root.geometry("280x300")

    scoresList = []

    scores = tk.StringVar()
    newScore = tk.StringVar()
    total = tk.StringVar()
    numEntries = tk.StringVar()
    average = tk.StringVar()
    median = tk.StringVar()
    maxScore = tk.StringVar()
    minScore = tk.StringVar()

    def handleClick(): # handles click of 'add score' button
        if re.search("[0-9]", newScore.get()): # if new score is all numbers
            input = float(newScore.get())
            if input >= 0 and input <= 100:
                scoresList.append(input)
                newScore.set("")
                scores.set(scoresList)
                data = process_scores(scoresList)
                total.set(data.total)
                numEntries.set(data.num)
                median.set(round(data.median, 2))
                average.set(round(data.mean, 2))
                maxScore.set(data.max)
                minScore.set(data.min)
            else:
                messagebox.showerror("Error", "Grade entries must be between 0 and 100.")
        else:
            newScore.set("")
            messagebox.showerror("Error", "Grade entries must be a number.")  

    scoresLabel = ttk.Label(root, text="Scores", width=10)
    scoresEntry = ttk.Entry(root, textvariable=scores, state="readonly")

    newScoresLabel = ttk.Label(root, text="New Score", width=10)
    newScoresEntry = ttk.Entry(root, textvariable=newScore)

    submit = ttk.Button(root, text="Add Score", command=handleClick)

    infoHeader = ttk.Label(root, text="Test Score Info")
    totalLabel = ttk.Label(root, text="Total", width=10).grid(column=0, row=5)
    totalEntry = ttk.Entry(root, textvariable=total, state="readonly").grid(column=1, row=5)
    numLabel = ttk.Label(root, text="# of Entries", width=10).grid(column=0, row=6)
    numEntry = ttk.Entry(root, textvariable=numEntries, state="readonly").grid(column=1, row=6)
    averageLabel = ttk.Label(root, text="Average", width=10).grid(column=0, row=7)
    averageEntry = ttk.Entry(root, textvariable=average, state="readonly").grid(column=1, row=7)
    medianLabel = ttk.Label(root, text="Median", width=10).grid(column=0, row=8)
    medianEntry = ttk.Entry(root, textvariable=median, state="readonly").grid(column=1, row=8)
    maxLabel = ttk.Label(root, text="Max", width=10).grid(column=0, row=9)
    maxEntry = ttk.Entry(root, textvariable=maxScore, state="readonly").grid(column=1, row=9)
    minlLabel = ttk.Label(root, text="Min", width=10).grid(column=0, row=10)
    minEntry = ttk.Entry(root, textvariable=minScore, state="readonly").grid(column=1, row=10)

    scoresLabel.grid(column=0, row=4, padx=5, pady=5, sticky=tk.E)
    scoresEntry.grid(column=1, row=4, padx=5, pady=5, sticky=tk.E)
    newScoresLabel.grid(column=0, row=1, padx=5, sticky=tk.E)
    newScoresEntry.grid(column=1, row=1, padx=5, sticky=tk.E)
    submit.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
    infoHeader.grid(column=1, row=3, sticky=tk.W)

    #scores = get_scores() # gets scores from user inputs
    #process_scores(scores) # calculates mean, median, min, and max of scores
   
    root.mainloop()

# if started as the main module, call the main function
if __name__ == "__main__":
    main()