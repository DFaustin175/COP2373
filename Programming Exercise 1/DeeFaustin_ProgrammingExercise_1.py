# Dee Faustin Assignment 1
# Program for selling a limited number of cinema tickets maximum 4 tickets per buyer

# Function used to return the new amount of tickets available after purchase
def purchase_function(tickets, purchases):
    return tickets - purchases

# Main function where input output and accumulator is present
def main():

    #initialization of buyer count to display total amount of buyers once all tickets are sold
    amountOfBuyers = int(0)

    #initialization of ticket counts keeping track of the amount of tickets available to be sold
    ticketCount = int(20)

    print('Welcome to the cinema!')

    # Displaying how many tickets are available
    print('We currently have ' + str(ticketCount) + ' tickets available for purchase.')

    # Taking in user input for if they would like to purchase
    answer = str(input('Would you like to purchase tickets?: '))

    # A while loop that continues to allow user to purchase more tickets as long as user input remains positive
    while answer.lower() == 'yes':

        # A try loop to catch errors in the event that the user inputs anything other than a whole number
        try:
            # Takes in user input for how many tickets the user wishes to purchase
            purchaseCount = int(input('How many tickets would you like to purchase?: '))

            # Buyers are limited to 4 tickets per purchases this if statement ensures that they do not buy more tickets than permitted
            if purchaseCount > 4:
                print('Maximum 4 tickets per order!')
                purchaseCount = int(input('How many tickets would you like to purchase?: '))

            # Elif statement to ensure that the user does not purchase more tickets than there are currently on hand
            elif purchaseCount > ticketCount:
                print('Requested ticket amount exceeds currently available tickets.')
                print('Tickets remaining ' + str(ticketCount))
                purchaseCount = int(input('How many tickets would you like to purchase?: '))

            # Confirmation of the purchase being successful
            print('Purchasing ' + str(purchaseCount) + ' ticket(s).')

            #Reduce ticket count based on the amount purchased by the user
            ticketCount = purchase_function(ticketCount, purchaseCount)
            amountOfBuyers += 1

            # Breaks the while loop once all tickets are sold
            if ticketCount <= 0:
                break

        except ValueError:
            print('Error: Please input a whole number')

        print('Thank you for your purchase!')

        # Ask for user input on if the would like to purchase more tickets
        answer = str(input('Would you like to purchase more tickets? Remaining tickets: ' + str(ticketCount) + ' '))

    # Once all tickets are sold display the total number of buyers
    if ticketCount <= 0:
        print('Total number of buyers: ' + str(amountOfBuyers))
        print('We have sold out of tickets. Thank you for coming!')


main()