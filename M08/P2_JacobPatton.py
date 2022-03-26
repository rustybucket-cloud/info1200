import tkinter as tk #import statements
from tkinter import ttk, messagebox 
import locale

def calculateValue(temp, unit): #if temperature is fahrenheit, convert to celcuis, if celcius, convert to fahrenheit
    if unit == 'f': #if unit arg is 'f'
         conversion = (int(temp) - 32) * (5/9) #converts temperature to celcuis
         return conversion #returns value
    elif unit == 'c': #if unit arg is 'c'
        conversion = (int(temp) * 9/5) + 32 #converts temperautre to fahrenheit
        return conversion #returns valiue

if __name__ == "__main__": #main function
    root=tk.Tk() #creates window
    root.geometry("300x125") #sets window size

    frame = ttk.Frame(root, padding="10 10 10 10").grid(column=0, row=0) #create frame

    root.title("Temperature Converter") #window title
    f = tk.StringVar() #creates fahrenheit variable
    c = tk.StringVar() #creates celcius variable

    def values(): #gets the value in inputs, converts, changes the value in other input
        far = f.get() #gets input from fahrenheit input
        cel = c.get() #gets input from celcius input
        if far != '' and cel != '': #if user inputed in both boxes
            messagebox.showerror('Error', "Please only fill one box.") #error message
        elif far == '' and cel == '': #if user did not input in either box
            messagebox.showerror('Error', "Please enter a fahrenheit or celcius temperature.") #error message
        else: #user only inputed in one box
            if far != '': #if user inputed in fahrenheit
                unit = 'f' #set unit to 'f'
                conversion = calculateValue(far, unit) #set conversion to result of calculateValue function
                c.set(conversion) #set celcius input to conversion
            elif cel != '': #if user inputed in  celcius
                unit = 'c' #set unit to 'c'
                conversion = calculateValue(cel, unit) #sets converion to result calculateValue function
                f.set(conversion) #sets fahrenheit input to conversion

    def clear(): #clears inputs
        f.set('') #clears fahrenheit input
        c.set('') #clears celcius input

    ttk.Label(frame, text="Fahrenheit").grid(column=0, row=0, sticky=tk.E, padx=5, pady=5) #creates Fahrenheit label
    ttk.Entry(frame, textvariable=f).grid(column=1, row=0, padx=5, pady=5) #create Fahrenheit input

    ttk.Label(frame, text="Celcius").grid(column=0, row=1, sticky=tk.E, padx=5, pady=5) #create celcius input
    ttk.Entry(frame, textvariable=c).grid(column=1, row=1, padx=5, pady=5) #create celcius input

    tk.Button(frame, text="Clear", width=10, pady=5, command=clear).grid(row=2, column=1, stick=tk.W) #creates clear button, runs clear function on click
    tk.Button(frame, text="Convert", width=10, pady=5, command=values).grid(row=2, column=0, columnspan=2, sticky=tk.E) #creates calculate button, runs values function on click
   
    root.mainloop() #makes window visible