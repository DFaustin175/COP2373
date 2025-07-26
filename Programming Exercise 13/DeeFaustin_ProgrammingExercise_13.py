#Dee Faustin Programming Exercise 13
#Program that creates a database of florida cities and their populations. Using the database it calculates the rise and fall of the population for the next 20 years

import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import math

def main():
    createDatabase()
    print("\nOf the cities displayed above ")
    cityName = input("Which city would you like to simulate population growth: ")
    growthRate = float(input("At what rate would you like to simulate population growth: "))
    populationSim(cityName, growthRate)
    plotPoints(cityName)

def createDatabase():
    con = sqlite3.connect("population_DF.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS population(city, year, population)")
    data = [
        ('Sarasota', 2023, 57602),
        ('Palmetto', 2023, 13577),
        ('Fort Lauderdale', 2023, 184255),
        ('Fort Myers', 2023, 97372),
        ('Tampa', 2023, 403364),
        ('Bartow', 2023, 20584),
        ('Mulberry', 2023, 4346),
        ('Delray Beach', 2023, 67536),
        ('LaCrosse', 2023, 25103),
        ('Ocala', 2023, 68426)
    ]

    cur.executemany("INSERT INTO population VALUES (?, ?, ?)", data)
    con.commit()
    con.close()

    for row in data:
        print("City:",row[0], "| Year:", row[1], "| Population:", row[2])
    return

def populationSim(city, rate):
    con = sqlite3.connect("population_DF.db")
    cur = con.cursor()

    cur.execute(f"SELECT * FROM population WHERE city = '{city}'")
    initialPopulation = cur.fetchone()[2]

    #Simulate population growth and decay
    growth = []
    for i in range(1, 21):
        year = 2023 + i
        growthData = math.floor(initialPopulation * np.exp(rate * i))
        newGrowth = (city, year, growthData)
        growth.append(newGrowth)

    cur.executemany("INSERT INTO population VALUES (?, ?, ?)", growth)

    con.commit()
    con.close()
    return

def plotPoints(city):
    con = sqlite3.connect("population_DF.db")
    cur = con.cursor()
    cur.execute(f"SELECT year, population FROM population WHERE city = '{city}'")
    data = cur.fetchall()

    year = [row[0] for row in data]
    population = [row[1] for row in data]

    print("Plotting points\n")
    plt.plot(year, population)
    plt.show()


    return

main()