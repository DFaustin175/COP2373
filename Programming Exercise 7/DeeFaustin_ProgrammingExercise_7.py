#Dee Faustin Assignment 7
#A program that allows a user to input a paragraph and display each sentence and the count of sentences within it.
import re

def main():
    #Paragraph input from user
    para = str(input("Input your paragraph:\n"))

    #Pass paragraph into function to find and display sentences and sentence count
    analyzePara(para)


def analyzePara(para):
    #pattern established to find sentences regardless of if it begins with a letter or a number
    pat = r"\.\s(?=[A-Z0-9])"

    #Converts the data into a list to easily display each sentence separately and the amount of sentences found
    paraData = re.split(pat, para)

    #A for loop that displays each sentence and keeps track of the amount of sentences logged
    paraCount = 0
    for i in paraData:
        paraCount += 1
        print('->', i, "\n")

    #Display sentence count
    print("Paragraph sentence count:", paraCount)

main()