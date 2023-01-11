# Muhammed efe İncir

# The conditions for the end of the game:
# 1) Completion of all missions.
# 2) If hero has no Hp.
# 3) Pegasus is not enough to return after going to the (island) first and second missions .
# 4) At the final, the first or second missions remain, but Pegasus does not have enough health to go them.

fileObject = open("TaskList.txt", "r+")  # I opened the file to read tasks
temporaryList = []  # We add the lines to the list
for line in fileObject.readlines():
    temporaryList.append(line.replace("\n", ""))

taskList = []  # I assigned the lines in the desired nested order
for variable in temporaryList:
    appendList = []  # For nested structure
    splittedSentence = variable.split(",")  # I split the line with comma
    for split in splittedSentence:
        if splittedSentence.index(split) == 0:  # The first item should be appended as a string
            appendList.append(str(split))
        else:
            appendList.append(int(split))  # The second item should be appended as a integer
    taskList.append(appendList)  # I assigned inner list into outer list

heroHp = 3000  # Hero's starting values
heroSpeed = 20
pegasusHp = 550  # Pegasus's starting values
pegasusSpeed = 50


def Remove(removeList: list, completeTask: str):  # Recursive structure deletes completed task from task list
    if completeTask.lower() == str(removeList[0]).lower():  # For case insensitive desire
        removeList.clear()
    else:
        for lists in removeList:
            if type(lists) == list:  # When it finds the nested list it recused
                Remove(lists, completeTask)
            else:
                pass
    return removeList


def Printer(printList: list, firstTime=False):  # Recursive Structure that prints the list to the terminal
    if len(printList) > 0 and firstTime == True:
        print(
            f"|  {printList[0]:<8}|  {str(printList[1]) + ' km':<14}|  {str(printList[2]) + ' km':<9}|  {printList[3]:<8}|")

    for lists in printList:
        firstTime = True
        if type(lists) == list:
            Printer(lists, firstTime)


def TimeCalculator(taskContent: list, choice: str):  # The function that calculates the time to pass along the road
    """Time which is returned changes according to choice of way of travel"""
    if choice.lower() == "pegasus":
        time = taskContent[2] / pegasusSpeed
        return round(time)
    else:
        time = taskContent[1] / heroSpeed
        return round(time)


TimePassed = []  # To store time passed after the task
GamePlay = True  # To control the main loop
print("Welcome to Hero’s 5 Labors!")
while GamePlay:
    if len(taskList) == 2:  # Some scenarios where the game will end
        if taskList[0][0] == "Task1" and taskList[1][
            0] == "Task2" and pegasusHp < 120:  # If 1 and 2 can not be completed
            print("\n" + "Game over!")
            print("You can't complete missions without Pegasus")
            break
    elif len(taskList) == 1:
        if taskList[0][0] == "Task1" and pegasusHp < 120:  # If Task1 cannot be completed
            print("\n" + "Game over!")
            print("You can't complete last mission without Pegasus")
            break
        elif taskList[0][0] == "Task2" and pegasusHp < 150:  # If Task2 cannot be completed
            print("\n" + "Game over!")
            print("You can't complete last mission without Pegasus")
            break

    print(f"Remaining HP for Hero : {heroHp}")  # Instant information
    print(f"Remaining HP for Pegasus: {pegasusHp}")
    print(f"Here are the tasks left that hero needs to complete:")
    print("""----------------------------------------------------
| TaskName | ByFootDistance | ByPegasus | HPNeeded |
----------------------------------------------------""")
    Printer(taskList)  # Where incomplete tasks are printed
    print("----------------------------------------------------")

    while True:  # Task selection
        taskChoice = input("Where should Hero go next? ")
        taskChecker = []  # Valid choice checker
        taskContent = []  # For the information of the task to be selected
        for innerLists in taskList:
            taskChecker.append(innerLists[0])
        if taskChoice.capitalize() not in taskChecker:
            print("Invalid input")
        elif taskChoice.capitalize() == "Task1" and pegasusHp < 120:  # If there is no life enough for the mission selection
            print("Pegasus has no Hp for this task,so choose another")
        elif taskChoice.capitalize() == "Task2" and pegasusHp < 150:  # If there is no life enough for the mission selection
            print("Pegasus has no Hp for this task,so choose another")
        else:
            for inside in taskList:  # Loading content information to the list if the task is valid
                if inside[0] == taskChoice.capitalize():
                    taskContent = inside
            break

    while True:  # Travel way selection
        travelType = input("How do you want to travel?(Foot/Pegasus) ")
        if "Task1" == taskChoice.capitalize() and travelType.lower() == "foot":  # Warning in places that cannot go on foot
            print("You cannot go there by foot.")
        elif "Task2" == taskChoice.capitalize() and travelType.lower() == "foot":  # Warning in places that cannot go on foot
            print("You cannot go there by foot.")
        elif travelType.lower() == "pegasus":
            time = TimeCalculator(taskContent, travelType)  # Calculation of time that passes on way
            healthNeedPegasus = time * 15
            if pegasusHp > healthNeedPegasus:
                pegasusHp -= healthNeedPegasus  # Hp lose because of travel
                heroHp -= taskContent[3]  # Hp Lose because of monster
                TimePassed.append(time)  # To store the elapsed time
                break
            else:
                print("Pegasus does not have enough HP.")  # If Pegasus has no enough hp for travel

        elif travelType.lower() == "foot":
            time = TimeCalculator(taskContent, travelType)  # Calculation of time that passes on way
            heroHp -= time * 10  # Hp lose because of travel
            heroHp -= taskContent[3]  # Hp Lose because of monster
            TimePassed.append(time)  # To store the elapsed time
            break
        else:
            print("Invalid input")  # If travel type is invalid

    if heroHp > 0:  # If hero lives, printing process
        print("Hero defeated the monster.")
        print(f"Time passed : {time} hour")  # Printing the time which passed
        print()
        print(f"Remaining HP for Hero : {heroHp}")  # Instant information
        print(f"Remaining HP for Pegasus: {pegasusHp}")
        print()
    else:  # If hero is dead
        print("\n" + "Game over!")
        print("The hero has no more life to continue the adventure")
        break

    if "Task1" == taskChoice.capitalize() and pegasusHp < 120:  # Pegasus not having enough Hp after going to Task1 to back home
        print("You stuck in the island.Because of pegasus health,you can't go back with pegasus")
        print("\n" + "Game over!")  # Game ends
        break
    elif "Task2" == taskChoice.capitalize() and pegasusHp < 150:  # Pegasus not having enough Hp after going to Task to back home
        print("You stuck in the island. Because of pegasus health,you can't go back with pegasus")
        print("\n" + "Game over!")  # Game ends
        break

    while True:  # Returning way of home selection
        returnType = input("How do you want to go home?(Foot/Pegasus) ")
        if "Task1" == taskChoice.capitalize() and returnType.lower() == "foot":  # Warning in places that cannot go on foot
            print("You cannot go there by foot.")
        elif "Task2" == taskChoice.capitalize() and returnType.lower() == "foot":  # Warning in places that cannot go on foot
            print("You cannot go there by foot.")
        elif returnType.lower() == "pegasus":
            time = TimeCalculator(taskContent, returnType)  # Calculation of time that passes on way
            pegasusHealthNeed = time * 15
            if pegasusHp > pegasusHealthNeed:
                pegasusHp -= pegasusHealthNeed  # Hp lose because of travel
                TimePassed.append(time)  # To store the elapsed time
                break
            else:
                print("Pegasus does not have enough HP.")  # If Pegasus has no enough Hp for going back to home
        elif returnType.lower() == "foot":
            time = TimeCalculator(taskContent, returnType)  # Calculation of time that passes on way
            heroHealthNeed = time * 10
            TimePassed.append(time)  # To store the elapsed time
            heroHp -= heroHealthNeed  # Hp lose because of travel
            break
        else:
            print("Invalid input")

    if heroHp > 0:  # If hero lives, printing process
        print("Hero arrived home.")
        print(f"Time passed : {time} hour")  # Printing the time which passed
    else:  # If hero is dead
        print("\n" + "Game over!")
        print("The hero has no more life to continue the adventure")
        break

    taskList = Remove(taskList, taskChoice)  # Update list after task done
    for tasks in taskList:  # Making retouch for task list
        if tasks == []:
            taskList.remove(tasks)
    if len(taskList) == 0:  # Win the game by finishing missions
        print()
        print("Congratulations, you have completed the task.")
        break
    else:
        print()

# Hall Of Fame Part
passedTime = 0
for times in TimePassed:  # Calculation of total time that passed
    passedTime += times

name = input("\n" + "What is your name : ")  # Asking players name
fileOpened = open("HallOfFame.txt", "a", encoding="utf-8")  # If file doesn't exist, It create
fileOpened.close()
fileOpened = open("HallOfFame.txt", "r", encoding="utf-8")  # To access the information in HallOfFame.txt
items = [line.replace("\n", "") for line in fileOpened.readlines()]
bestThree = [item.split(",") for item in items]  # [name,score]

if len(bestThree) < 3:  # If there is no three people in the best three,It doesn't need to delete any person on list
    bestThree.append([name, passedTime, "\n"])  # End of line for rewriting to the list


    def sortedKey(list: list):  # Design of Looking for second argument
        return int(list[1])


    bestThree.sort(key=sortedKey, reverse=True)  # The second arguments are scores,so I designed the sort function
else:
    bestThree.append([name, passedTime, "\n"])


    def sortedKey(list: list):  # Design of Looking for second argument
        return int(list[1])


    bestThree.sort(key=sortedKey, reverse=True)  # The second arguments are scores,so I designed the sort function
    bestThree.pop(-1)

print("""Hall Of Fame
------------------------
| Name   | Finish Time |
------------------------""")
for people in bestThree:  # Printing the persons that in hall of fame
    print(f"| {str(people[0]).capitalize():<8}| {people[1]:<11}|")
    print("------------------------")

FileNeed = []  # To store names and scores after updating the sequence of best scores
for line in bestThree:
    backWrite = f"{line[0]},{line[1]}\n"
    FileNeed.append(backWrite)

fileOpened.close()
fileOpened = open("HallOfFame.txt", "w+", encoding="utf-8")  # I cleaned the old text
fileOpened.writelines(FileNeed)  # And I write the new names and scores line by line in update sequence
fileOpened.close()
