from time import sleep
import os

while True:
    optionsList = ["1. Break the loop", "2. Open loading bar"]
    try:
        for i in optionsList:
            print(i)
        userChoice = int(input("Your choice: "))
        if userChoice == 1:
            print("Broke the loop ", end="loop")
            returnDelay()
            break
        elif userChoice == 2:
            print("Sleeping", end=" ")
            print("\n")
        else:
            print("Null")
    except ValueError:
        print("Invalid input!")

def returnDelay():
    print("Returning ", end="back")
    for i in range(3):
        print(".\b")    