import random


foundNameCounter = 0
foundNameAgain = True
arraySize = 0
ix = 0

namesArray = ["damian", "stanisław", "karol", "bartosz", "dariusz", "tomasz", "daniel", "jakub", "wojciech", "piotr", "sandra", "karolina", "anna"]

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

try:
    while arraySize <= 0:
        print("Enter list size: ")
        arraySize = int(input())
        if arraySize <= 0:
         print("List size must be bigger then 0!")

    personsList = []

    for i in range(arraySize):
        personsList.append(Person(namesArray[random.randint(0, len(namesArray) - 1)], random.randint(0, 100)))

    print("This are all persons names and ages that has been generated:")
    nameNumber = 1
    for names in personsList:
        print("Person " + str(nameNumber) + " name is:", names.name + ", and persons age is:", names.age)
        nameNumber += 1

    while foundNameAgain == True:
        ix = 0
        foundNameCounter = 0
        foundNameAgain = True

        print("Enter name to found and I will count how many times it has been found in persons list: ")
        nameToFound = input()
        nameToFound = nameToFound.upper()

        for i in personsList:
            personsList[ix].name = i.name.upper()
            ix += 1

        for x in personsList:
            if x.name.upper() == nameToFound:
             foundNameCounter += 1

        print("Name " + nameToFound + " has been found: " + str(foundNameCounter) + " times in all generated persons.")
        print("Do You want to found other name? (Y/N)")
        againFounder = input()
        againFounder = againFounder.upper()
    if againFounder == "N":
        foundNameAgain = False
except:
    print("An exception occurred")