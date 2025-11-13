from pyFunctions import *
from tqdm import tqdm, trange

while True:
    optionsList = ["1. Break the loop", "2. Try progress bar"]
    try:
        for i in optionsList:
            print(i)
        userChoice = int(input("Your choice: "))
        if userChoice == 1:
            print("Broke the ", end="loop")
            returnDelay()
            break
        elif userChoice == 2:
            for j in tqdm(range(100)):
                customDelay()
            completionNotification(True)
    except ValueError:
        print("Invalid input!")

