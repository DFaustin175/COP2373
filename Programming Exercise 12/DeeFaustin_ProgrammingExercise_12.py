import numpy as np
import csv

def main():
    with open("C:/Users/deefa/Desktop/GitHub/COP2373/Programming Exercise CSV/Student_Grades.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)
        data = np.array(list(reader))

    arr = np.delete(data, 0, 1)
    arr = arr.astype('float64')
    print(arr)

    mean(arr)
    median(arr)
    stdDeviation(arr)
    minAndMax(arr)
    extraData(arr)


def mean(array):
    dataMean = np.mean(array, axis=0)
    print("\nClass Averages:")
    print("The class average for exam 1 is:", dataMean[0])
    print("The class average for exam 1 is:", dataMean[1])
    print("The class average for exam 1 is:", dataMean[2])
    print("The average grade across all exams is:", np.mean(array))

def median(array):
    dataMedian = np.median(array, axis = 0)
    print("\nExam Medians:")
    print("Exam 1 Median:", dataMedian[0])
    print("Exam 2 Median:", dataMedian[1])
    print("Exam 3 Median:", dataMedian[2])
    print("Median for all three exams:", np.mean(array))

def stdDeviation(array):
    dataMean = np.std(array, axis = 0)
    print("\nExam Standard Deviations:")
    print("Exam 1 STD Deviation:", dataMean[0])
    print("Exam 1 STD Deviation:", dataMean[1])
    print("Exam 1 STD Deviation:", dataMean[2])
    print("Standard Deviation across all three exams:", np.std(array))

def minAndMax(array):
    print("\nLowest and Highest Grades:")
    minData = np.min(array, axis = 0)
    print("Lowest Exam 1 Grade:", minData[0])
    print("Lowest Exam 2 Grade:", minData[1])
    print("Lowest Exam 3 Grade:", minData[2])

    maxData = np.max(array, axis = 0)
    print("Highest Exam 1 Grade:", maxData[0])
    print("Highest Exam 2 Grade:", maxData[1])
    print("Highest Exam 3 Grade:", maxData[2])

    print("Lowest overall exam score:", np.min(array))
    print("Highest overall exam score:", np.max(array))

def extraData(array):
    print("\nExtra Data:")
    passCount = np.flatnonzero(array > 60)
    failCount = np.flatnonzero(array < 60)
    print("Class Exam Pass Count:", len(passCount))
    print("Class Exam Fail Count:", len(failCount))
    passPercent = (float(len(passCount)) / array.size) * 100
    print("Class Pass Percentage: %" + str(passPercent))

main()