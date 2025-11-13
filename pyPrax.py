words = {}
data = open("pyData.txt", "r")
for line in data:
    order = line.split(" ")
    words[order[0]] = order[1], order[2]
data.close()

print(words)
loop = input("Wanna while loop? (Y/N)\n")
if loop == "Y":
    loop = True
else:
    print("You rejected while loop")
    loop = False

while loop == True:
    word = input("Name the language: ")
    if word in words:
        print("Short version: ", words[word[1]])
    else:
        print("No idea")
