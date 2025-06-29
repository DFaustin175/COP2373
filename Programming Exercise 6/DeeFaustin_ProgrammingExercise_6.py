#Dee Faustin Assignment 6
#Program has user input phone numbers, social security numbers, and zip codes and tests and displays if the users input is valid
import re


def main():
    #While loop used to allow information validation for as long as the user wishes
    answer = "y"
    while answer.lower() == "yes" or answer.lower() == "y":
        #Obtain user input for phone number, social security number, and zip code
        phoneNum = input("First, input a phone number: ")
        ssNum = input("Next, a social security number: ")
        zipCode = input("Finally, input a zip code: ")
        #Passes user input into a function that validates the information gained
        validateInput(phoneNum, ssNum, zipCode)
        answer = input("Continue logging information?: Y/N\n")
    return

def validateInput(phone, ss, zipC):
    #Using established patterns determine if the data obtained matches the format of a valid phone number, social security number, and zip code
    phoneCode = re.compile(r"(\+\d{1,3)?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
    ssCode = re.compile(r"(?!000|.+0{4})(?:\d{9}|\d{3}-\d{2}-\d{4})")
    zCode = re.compile(r"([0-9]{5}(?:-[0-9]{4})?)")

    #Depending on the success of re.search display if the tested information is valid
    isPhoneValid = re.search(phoneCode, phone)
    if isPhoneValid:
        print("Your phone number is valid")
    else:
        print("That is not a valid phone number")
    isSocialSecValid = re.search(ssCode, ss)
    if isSocialSecValid:
        print("Your social security number is valid")
    else:
        print("That is not a valid social security number")
    isZipCodeValid = re.search(zCode, zipC)
    if isZipCodeValid:
        print("Your zip code is valid")
    else:
        print("That is not a valid zip code")

main()