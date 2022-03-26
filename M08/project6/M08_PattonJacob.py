import math # import math module
import tkinter as tk # import tkinter
from tkinter import ttk, messagebox
import re # import regular expressions

# calculate grade
def calculateGrade(grades):
    total = 0 # all grades combines
    numberOfGrades = 0 # total number of grades
    for grade in grades: # loops through each entry value
        if not re.search("[0-9]", grade) or float(grade) <= 0 or float(grade) > 100: # determines if input is not valid
            messagebox.showwarning("Error", "Grades must be between 1 and 100") # shows error
            return "error" # returns 'error' so total grade is not updated
        total += float(grade) # adds grade to total
        numberOfGrades += 1 # adds 1 grade
    avg = round(total / numberOfGrades, 2) # gets average of grades
    return avg # returns average


numGrades = 4 # number of grade entries
height = 180 # height of window
#display gui
def buildGui():
    global height # uses numGrades
    root = tk.Tk() # creates window
    root.title("Grade Calculator") # window title
    root.geometry(f"300x{height}") # window size

    totalGrade = tk.StringVar() # total grade string

    all_entries = [] # array that contains all grade values
    def grade(): # calcuates average grade
        grades = [] # array that contains values, send to calculateGrade function
        for entry in all_entries: # loops through each entry
            grades.append(entry.get()) # gets the value of each entry
        avg = calculateGrade(grades) # calculates average
        if avg != "error": # if avg did not return 'error'
            totalGrade.set(avg) # sets totalGrade entry to average grade

    def clear(): # clears entries
        for entry in all_entries: # loops through array with each entry
            entry.set("") # clears entry
        totalGrade.set("0") # clears total grade

    
    def addBox(): # adds a new grade entry, got help from https://stackoverflow.com/questions/24833655/creating-new-entry-boxes-with-button-tkinter
        global numGrades
        numGrades += 1 # adds to numGrades
        
        var = tk.StringVar() # creates string variable for entry
        lab = ttk.Label(root, text="Grade" + str(numGrades)).grid(column=0, row=numGrades-1) # creates label
        ent = ttk.Entry(root, textvariable=var).grid(column=1, row=numGrades-1) # creates entry
        
        all_entries.append(var) # adds entry to all_entries
        global height
        height += 26 # makes window higher
        loadLabels() #moves labels


    for i in range(numGrades): # creates initial entries and labels
        lab = ttk.Label(root, text=f"Grade{i+1}").grid(column=0, row=i) # creates label
        var = tk.StringVar() # creates StringVar
        ent = ttk.Entry(root, textvariable=var).grid(column=1, row=i) # creates entry
        all_entries.append(var) # adds entry to all_entry array

    totalLabel = ttk.Label(root, text="Total Grade") # creates side a label
    totalEntry = ttk.Entry(root, textvariable=totalGrade, state="readonly") # creates side a entry
    clearButton = tk.Button(root, text="clear", width=10, command=clear) # creates clear button
    calculate = tk.Button(root, text="calculate", width=10, command=grade) # create calculate button
    add = tk.Button(root, text="Add Grade", width=10, command=addBox) # creates add grade button

    totalLabel.grid(column=0, row=numGrades) # sets grid location
    totalEntry.grid(column=1, row=numGrades) # sets grid location
    clearButton.grid(column=1, row=numGrades+1, sticky=tk.W) # sets grid location
    calculate.grid(column=1, row=numGrades+1, sticky=tk.E) # sets grid location
    add.grid(column=0, row=numGrades+1, sticky=tk.E) # sets grid location

    def loadLabels(): # updates grid location
        totalLabel.grid(row=numGrades) # updates grid location
        totalEntry.grid(row=numGrades) # updates grid location
        clearButton.grid(row=numGrades+1) # updates grid location
        calculate.grid(row=numGrades+1) # updates grid location
        add.grid(row=numGrades+1) # updates grid location
        root.geometry(f"300x{height}") # updates grid location
    
    root.mainloop() # displays window


#main function
def main():
    buildGui() # creates gui

if __name__ == "__main__": # if main function
    main()