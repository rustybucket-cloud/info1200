#Name: Jacob Patton
#Class: (INFO 1200)
#Section: (X01)
#Professor: Say
#Date: 11/11/21
#Project #: M10
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import csv
import tkinter as tk
from tkinter import ttk, messagebox
import re
MONTHLY_SALES = "monthly_sales.csv"

# prints application title
def display_title():
    print("Jacob Patton's Monthly Sales")
    print()

# displays menu options
def display_menu():
    print("COMMAND MENU")
    print()
    print("Monthly - Show monthly sales")
    print("Yearly - Show yearly sales")
    print("Edit - Edit the sales for a specified month")
    print("Exit - Exit program")
    print()

# reads data from csv file and adds to list
def read_sales():
    sales = []
    with open(MONTHLY_SALES, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            sales.append(row)
    return sales

# prints the monthly sales data
def view_monthly_sales(sales):
    for row in sales:
        print(f"{row[0]} - {row[1]}")

# prints the yearly sales data
def view_yearly_summary(sales):
    total = 0
    # add total sales
    for row in sales:
        amount = row[1]
        total += int(amount)

    # calculate the average monthly sales
    count = len(sales)
    average = round(total / count, 2)

    # format and display the result
    print("Yearly total:\t", total)
    print("Monthly average:\t", average)
    print()

    return {"total": total, "average": average}

# edit month sales data
def edit(sales, name, amount):
    # user selects month
    names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', "Aug", 'Sep', 'Oct', 'Nov', 'Dec']
    if name == "":
        name = input("Month:\t")
    name = name.title()

    # validate name entry
    if name not in names:
        messagebox.showerror("error", "Please enter a valid month.")
        return

    # if not valid entry
    if name not in names:
        print("Invalid three-letter month.")

    # user changes salaes data for selected month    
    index = names.index(name) # index of month in list of months
    month = []
    if amount == 0:
        amount = int(input("Sales Amount:\t"))
    
    # validate amount entry
    if not re.search("[0-9]", amount) or float(amount) < 0:
        messagebox.showerror("Error", "Amount must be a whole positive number")
        return
    month.append(name)
    month.append(str(amount))
    sales[index] = month # changes data in sales list
    write_sales(sales)
    print(f"Sales amount for {month[0]} was modified.")
    print()

# overwrites sales file with new info
def write_sales(sales):
    with open(MONTHLY_SALES, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sales)

# creates gui for user
def createGUI(sales):
    # set up gui
    root = tk.Tk()
    root.title("Monthly Sales")
    root.geometry("350x375")
    frame = ttk.Frame(root).grid(column=0, row=0, padx=10, pady=10)

    # set year total and year average
    yearTotal = tk.StringVar()
    yearAvg = tk.StringVar()
    def setYearSummary():    
        yearTotal.set(view_yearly_summary(sales)["total"])
        yearAvg.set(view_yearly_summary(sales)["average"])

    # create total and average entries
    yearTotalLabel = ttk.Label(frame, text="Year Total").grid(row=0, column=0, sticky=tk.W)
    yearTotalEntry = ttk.Entry(frame, textvariable=yearTotal, state="readonly", width=10).grid(row=1, column=0)
    yearAvgLabel = ttk.Label(frame, text="Year Average").grid(row=0, column=1, sticky=tk.W)
    yearAvgEntry = ttk.Entry(frame, textvariable=yearAvg, state="readonly", width=10).grid(row=1, column=1)

    # create month sales variables
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthVariables = []
    for month in months:
        monthVariables.append(tk.StringVar())
    
    # sets month variables
    def loadValues():
        for i in range(len(months)):
            monthVariables[i].set(sales[i][1])
        setYearSummary()
    loadValues()

    # creates monthly entries and labels
    row = 2
    for i in range(len(months)):
        # alternates column for label and entry 
        if i % 2 == 0:
            label = ttk.Label(frame, text=months[i]).grid(column=0, row=row, sticky=tk.W, padx=5)
            entry = ttk.Entry(frame, textvariable=monthVariables[i], width=10, state="readonly").grid(column=0, row=row+1, sticky=tk.W, padx=5)
        else:
            label = ttk.Label(frame, text=months[i]).grid(column=1, row=row, sticky=tk.W, padx=5)
            entry = ttk.Entry(frame, textvariable=monthVariables[i], width=10, state="readonly").grid(column=1, row=row+1, sticky=tk.W, padx=5)
            row += 2

    # update monthly sales variables
    updateMonth = tk.StringVar()
    updateAmount = tk.StringVar()
    # handles update button click
    def handleClick():
        month = updateMonth.get()
        amount = updateAmount.get()
        edit(sales, month, amount)
        write_sales(sales)
        loadValues()

    # create update labels, entries, and button
    updateMonthLabel = ttk.Label(frame, text="Month to Update").grid(row=0, column=3, sticky=tk.W)
    updateMonthEntry = ttk.Entry(frame, textvariable=updateMonth, width=10).grid(row=1, column=3, sticky=tk.W)
    updateAmountLabel = ttk.Label(frame, text="Update Amount").grid(row=2, column=3, sticky=tk.W)
    updateAmountEntry = ttk.Entry(frame, textvariable=updateAmount, width=10).grid(row=3, column=3, sticky=tk.W)
    updateButton = ttk.Button(frame, text="Update", width=7, command=handleClick).grid(row=4, column=3, sticky=tk.W)

    root.mainloop()

def main():
    display_title()
    display_menu()
    sales = read_sales()
    createGUI(sales)
    while True:
        command = input("Command:\t")
        if command == "monthly":
            view_monthly_sales(sales)
        elif command == "yearly":
            view_yearly_summary(sales)
        elif command == "edit":
            edit(sales, "")
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please Try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()