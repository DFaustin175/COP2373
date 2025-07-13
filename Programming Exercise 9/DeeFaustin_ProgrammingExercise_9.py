#Dee Faustin Assignment 9
#Program with a BankAccount class thats initialized with an account name, number, amount, and interest rate. Each of these variables also has a function dedicated to adjusting them.

class BankAccount:
    def __init__(self, name, acctNum, amount, interest):
        self.name = name
        self.acctNum = acctNum
        self.amount = int(amount)
        self.interest = interest

    def __str__(self):
        return (f"{self.name}:\n"
                f"Acct #{self.acctNum}\n"
                f"Current Funds: ${self.amount} \n"
                f"Interest Rate: %{self.interest}\n")

    def deposit(self):
        deposit = int(input("How many funds would you like to add to your account?:  "))
        self.amount = self.amount + deposit
        print("Funds successfully added.")
        print("New account balance: \n"
              f"${self.amount}\n")

    def withdraw(self):
        deposit = int(input("How many funds would you like to remove from your account?:  "))
        self.amount = self.amount - deposit
        print("Funds successfully withdrawn.")
        print("New account balance: \n"
              f"${self.amount}\n")

    def interestAdjust(self):
        self.interest = input("Please input the accounts new interest rate:  ")
        print("Interest rate successfully updated.")
        print("New account interest rate: \n"
              f"%{self.interest}\n")


def test():
    #Initialization of a new account
    acct = BankAccount("Ben Smith", 897, 1200, 12)

    #Print unedited version of account
    print(acct)

    #Test each method for adjusting different types of variables in the class
    acct.deposit()
    acct.withdraw()
    acct.interestAdjust()



