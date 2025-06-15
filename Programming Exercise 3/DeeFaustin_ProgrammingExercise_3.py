#Dee Faustin Assignment 3
#Program that asks a user for a list of their monthly expenses and displays the amount and provides the highest and lowest expense.
from functools import reduce

#This function asks the user to input the type of expense and the value of it and adds it to a dictionary of monthly expenses
def obtainExpenses(data):
    #Asks for user input to log expense type and value
    expenseType, expenseCost = input("Please input the expense type and value:\n").split()
    #Adds new expense and its value to a dictionary
    data[expenseType] = float(expenseCost)

#Using the data in the monthlyExpenses dictionary finds the total spent during the month and the least and greatest expense
def calculateData(data):
    #Uses lambda function to find the total expense
    totalExpenses = reduce(lambda x, y: x + y, data.values())

    #Goes into the dictionary to obtain the value with the highest value
    greatestExpense = max(data, key=data.get)
    #Returns the key that has the highest "cost" value in the dictionary
    greatestValue = data[greatestExpense]

    #Goes into the dictionary to obtain the value with the lowest value
    lowestExpense = min(data, key=data.get)
    #Returns the key that has the lowest "cost" value in the dictionary
    lowestValue = data[lowestExpense]

    #prints the total, highest, and lowest expense
    print("Your total expenses for this month is $" + str(round(totalExpenses, 2)))

    print("Your greatest expense was", greatestExpense, "at a value of $" + str(greatestValue))
    print("Your lowest expense was", lowestExpense, "at a value of $" + str(lowestValue))



def main():
    #creates an empty dictionary that will be populated using the obtainExpenses function
    monthlyExpenses = {}
    #Ask the user if they are ready to start logging expenses for the month
    ans = input("Begin logging monthly expenses?: Y/N   ")

    #Based on the users answer continue asking if the user has more expenses to input
    while ans.lower() == "y" or ans.lower() == "yes":
        obtainExpenses(monthlyExpenses)
        ans = input("Continue logging expenses?: Y/N   ")

    #Displays the different expenses in the monthlyExpenses dictionary in a clear format
    for x, y in monthlyExpenses.items():
        print(x)
        print("   $" + str(y), "\n")

    #Calculate the highest, lowest, and total
    calculateData(monthlyExpenses)




main()