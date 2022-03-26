import math # import math module
import tkinter as tk # import tkinter
from tkinter import ttk, messagebox

# calculate hypotenuse
def calculateHypotenuse(a, b): # define function
    c = math.sqrt(a ** 2 + b ** 2) # calculate hypotenuse, c = square root of a squared plus b squared
    return c #return hypotenuse

# create gui
def main(): # define function
    root = tk.Tk() # create window
    root.title("Hypotenuse Calculator") # give window title
    root.geometry("250x150") # define window size

    a = tk.StringVar() # define a variable
    b = tk.StringVar() # define b  variable
    c = tk.StringVar() # define c variable, hypotenuse

    def calculate(): # calculates hypotenuse
        aInput = a.get() # gets a side input
        bInput = b.get() # gets b side input
        if not a.get().isnumeric() or not b.get().isnumeric(): # if a or b inputs are not whole positive numbers
            messagebox.showwarning("Error", "a and b must be whole positive integers") # show error message
        else: # if inputs are valid
            sideA = int(aInput) # converts value to int
            sideB = int(bInput) # converts value to int
            sideC = calculateHypotenuse(sideA, sideB) # calculates hypotenuse
            c.set(round(sideC, 2)) # sets hypotenuse value to hypotenuse

    def clear(): # clears entries
        a.set("") # clears a entry
        b.set("") # clears b entry
        c.set("") # clears c entry

    ttk.Label(root, text="Side a").grid(column=0, row=0) # creates side a label
    ttk.Entry(root, textvariable=a).grid(column=1, row=0) # creates side a entry

    ttk.Label(root, text="Side b").grid(column=0, row=1) # create side b label
    ttk.Entry(root, textvariable=b).grid(column=1, row=1) # create side b entry

    ttk.Label(root, text="Side c").grid(column=0, row=2) # create side c label
    ttk.Entry(root, textvariable=c, state="readonly").grid(column=1, row=2) #create side c entry

    tk.Button(root, text="clear", width=10, command=clear).grid(column=1, row=3, sticky=tk.W) # creates clear button
    tk.Button(root, text="calculate", width=10, command=calculate).grid(column=1, row=3, sticky=tk.E) # create calculate button


    root.mainloop() # shows window

if __name__ == "__main__":
    main()