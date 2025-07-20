#Dee Faustin Assignment CSV
#A program that creates a csv file for an instructor. The CVS file allows the instructor to log the students first and last name as well as three exam scores
import csv

#Take in user input for how many students to log and their information
def createFile():
    studentCount = int(input("Welcome, How many student grades will you be submitting? "))

    #Initialze table of information with a header for data points
    data = []

    #Continue taking in information until all students are logged
    for x in range(studentCount):
        fullName = str(input("Enter the student's first and last name: "))
        exam1, exam2, exam3 = map(int, input("Enter the students 3 test scores: ").split())
        newData = {"Full Name": fullName, "Exam 1": exam1, "Exam 2": exam2, "Exam 3": exam3}
        data.append(newData)
        print("Data successfully added. \n")

    #Using the data submitted create a csv file and populate it with the data
    keys = data[0].keys()

    with open("Student_Grades.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, keys)
        writer.writerows(data)

#Read and display the contents of previously created csv file
def displayGrades():
    print("Displaying data: \n")
    with open("Student_Grades.csv", mode="r") as file:
        csvfile = csv.reader(file)
        #For each line in csv file print it
        for lines in csvfile:
            print(lines)




createFile()
displayGrades()