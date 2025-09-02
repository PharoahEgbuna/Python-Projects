"""Birthday Paradox Simulation by Al Sweigart"""

import datetime
import random

def getBirthdays(numberOfBirthdays):
    # Returns a list of number random date objects for birthdays
    birthdays = []

    for i in range(numberOfBirthdays):
        #The year will be the same for all birthdays
        startOfYear = datetime.date(2001,1,1)

        #Get a random day of the year
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    #Returns the date object of a birthday that occurs more than once in the birthdays list

    if len(birthdays) == len(set(birthdays)):
        return None #If all birthdays are unique None is returned.
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA #Return the matching birthday.

print('''The Birthday Paradox, by Al Sweigart
This paradox shows us that ina  group of N people, the odds that twoof them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random simulations) to explore the concept)
(It is not actually a paradox, just a surprising result)
      ''')

MONTHS = ('January', 'Feburary',  'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December')

while True:
    print("How many birthdays shall I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break #User has entered a valid amount 
print()

#Generate and display the birthdays
print("Here are", numBDays, "birthdays:")
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = "{} {}".format(monthName, birthday.day)
    print(dateText, end='')

print()
print()

#Search for a match
match = getMatch(birthdays)

#Display the results
print("In this simulation, ", end='')
if match != None: 
    monthName = MONTHS[match.month - 1]
    dateText = "{} {}".format(monthName, match.day)
    print("Multiple people have a birthday on", dateText)
else:
    print("There are no matching birthdays.")

print()

print("Generating", numBDays, "random birthdays 100,000 times...")
input("Press enter to begin..")

print("Let\'s run another 100,000 simulations:")
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "simulations run...")

    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None: 
        simMatch = simMatch + 1

probability = round(simMatch / 100_000 * 100, 2)
print("100,000 simulations run.")
print("Out of 100,000 simulations of ", numBDays, "people, there was a matching birthday in that group ", simMatch, "times.")
print("This means that ", numBDays, "people have a ", probability, "% chance of having a matching birthday in their group.")
print('That\'s probably more than you would think!')