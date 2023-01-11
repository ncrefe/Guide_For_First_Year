fileObject = open("users.txt", "r+")  # open our file
sentences = [file for file in fileObject.readlines()]
actualList = list()
for person in sentences:  # create sublists in actualList for flexibility
    replaced = person.replace("\n", "")
    splitPerson = replaced.split(";")
    information = [splitPerson[0], splitPerson[1], splitPerson[2]]  # sublist = person,password,friend
    actualList.append(information)
userName = ""
password = ""


def mainMenu():
    answer = input("1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit\n")
    return answer


def login():  # 1
    userName = input("Please enter username:\n")
    password = input("Please enter password:\n")
    if userName == "" or password == "":
        print("Wrong password or username\n")
        userName = ""
        password = ""
        return userName, password
    else:
        logChecker = 0
        for names in actualList:
            if userName.upper() == names[0].upper():
                logChecker += 1
            if password == names[1]:
                logChecker += 1
        if logChecker == 2:
            print("Logged in\n")

            # use these in memory
            return userName, password
        else:
            userName = ""
            password = ""
            print("Wrong password or username\n")
            return userName, password


def validationName(paramet: str):  # 2
    if paramet == "":
        return False
    for letter in paramet:
        if letter.isalpha() == False and letter.isdigit() == False:  # number and alphabet case
            return False
        elif letter.lower() != letter:  # lower case
            return False
    for namer in actualList:  # already exist case
        if paramet == namer[0]:
            return False
    return True


def validationPassword(paramet2: str):  # 2
    lCheck = 0
    nCheck = 0
    if not 4 <= len(paramet2) <= 8:
        return False
    for letter in paramet2:
        if letter.isalpha():
            lCheck += 1
        elif letter.isdigit():
            nCheck += 1
    if not lCheck >= 1:
        return False
    elif not nCheck >= 1:
        return False
    else:
        return True


def theCreator():  # 2
    newName = input("Please enter username:\n")
    newPassword = input("Please enter password:\n")
    if not validationName(newName):
        print("Username not valid\n")
        return False
    if not validationPassword(newPassword):
        print("Password not valid\n")
        return False
    else:
        actualList.append([str(newName), str(newPassword), str("")])



def addFriend():  # 3
    if userName == "":
        print("You need to log in first\n")
    else:
        friendName = input("Please enter the name of your new friend:\n")
        a = False
        for lists in actualList:
            if friendName == lists[0]:
                for findUser in actualList:
                    if userName == findUser[0]:
                        if findUser[2] != "":
                            findUser[2] = findUser[2] + f",{friendName}"
                        else:
                            findUser[2] = findUser[2] + f"{friendName}"
                a = True
        if not a:
            print("Friend not found\n")


def whoIsMyFriend():  # 4
    if userName == "":
        print("You need to log in first\n")
    else:
        for lists in actualList:
            if lists[0] == userName:
                print(lists[2])


def getOut():  # 5
    newFile = []
    for lists in actualList:
        appender = f"{lists[0]};{lists[1]};{lists[2]}\n"
        newFile.append(appender)
    fileObject.close()
    a = open("users.txt", "w")
    a.writelines(newFile)


while True:
    answer = mainMenu()
    if answer == str(1):
        userName, password = login()
    elif answer == str(2):
        theCreator()
    elif answer == str(3):
        addFriend()
    elif answer == str(4):
        whoIsMyFriend()
    elif answer == str(5):
        getOut()
        exit()
    else:
        print("Invalid option\n")
