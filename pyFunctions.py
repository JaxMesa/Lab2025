from time import sleep

def returnDelay():
    print("Returning ", end="back")
    for i in range(3):
        print(".", end=" ")
        sleep(1)    

def customDelay():
    sleep(1)

def completionNotification(completed):
    if completed == True:
        print("Action successfully completed")
    else:
        print("Something went wrong")