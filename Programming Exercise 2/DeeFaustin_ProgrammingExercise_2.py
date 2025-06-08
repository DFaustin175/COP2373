#Dee Faustin Assignment 2
#Application that scans an email provided by the user for each of 30 keywords or phrases most likely to be used in an email
#After scanning the email based on the points accumulated during the scan it will receive a spam score. This score describes how likely the email is spam.

#Function that loops through list of spam words and phrases and increase the spam score of the email based on the amount of words and phrases present within it
def spamCheck(email):
    spamPoints = 0
    hitPhrases = []
    for x in spamWords_Phrases:
        if x.lower() in email.lower():
            spamPoints += 1
            hitPhrases.append(x)
    spamCalc(spamPoints, hitPhrases)

#Using the values obtained from the spamCheck function calculate the likelihood of the email being spam
#Then within this function display the spam score, the likelihood of the message being spam and the words/phrases which caused it to be spam
def spamCalc(spamPoints, hitPhrases):
    spamScore = spamPoints/len(spamWords_Phrases)
    print("\nThis email's spam score is " + str(spamPoints))
    print("The phrases responsible for this score are " + str(hitPhrases))
    if spamScore < .25:
        print("Based on this score, this email is not likely spam.")
    elif .25 <= spamScore < .50:
        print("Based on this score, this email is likely spam.")
    elif spamScore >= .50:
        print("Based on this score, this email is very likely to be spam.")



#List of 30 words and phrases most likely to be present in a spam email
spamWords_Phrases = ["Best price", "Act now", "Important information regarding", "Risk-free", "In accordance with laws"
                     "Click here", "Get it now", "Do it today", "Don’t delete", "Exclusive deal", "Get started now",
                     "Information you requested", "Limited time", "Urgent", "You are a winner", "You have been selected",
                     "Check or money order", "Confidentiality", "Pre-approved", "Subject to ", "Contact us immediately",
                     "Confidential", "Take action", "Click below:", "Hi ", "Action required", "Money-back guarantee",
                     "Change password", "Confirm your details", "Immediate action required", "Click to verify"]

exampleEmail = ("Email 1: \n"
          "Hi John, \n"
          "An anonymous colleague has submitted feedback concerning your recent workplace interactions. \n"
          "To protect privacy, the content of this feedback cannot be shared via standard email. To view the feedback and respond confidentially, click below: \n"
          "View Confidential Feedback \n"
          "Your prompt attention demonstrates your commitment to a respectful workplace. \n"
          "Sincerely, Automated HR Solutions Contoso Corp")

print(exampleEmail)
spamCheck(exampleEmail)

userEmail = input("\nPlease input your own email to check its spam score: \n")
spamCheck(userEmail)
