end = False  # Flag for controlling the loop
checker1 = True
checker2 = True
checker3 = True
vehicle = True
vehicleList = [["car", "90"], ["motorcyle", "80"], ["bicyle", "25"]]  # List of vehicles

while not end:
    fileCities = open("provinces.txt", "r+")  # Open file for reading and editing
    lister = []
    for line in fileCities:
        upgrade = line.split("\n")[0]
        lister.append(upgrade)

    realCities = []  # Final list
    for city in lister:
        three = city.split(",")
        realCities.append(three)

    invalidChecker = []  # List for checking existence of city
    for index in realCities:
        invalidChecker.append(index[0])

    while checker1:
        cityOne = input("Departure province:\n")  # Input operations

        if cityOne.upper() not in invalidChecker:  # Recommended city design
            recommendCity = ""
            sorter11 = []
            for names in invalidChecker:
                length2 = len(cityOne)
                if names[0:length2].upper() == cityOne.upper():  # Alphabetical sorting operations
                    sorter11.append(names)
            sorter11.sort()
            for names in sorter11:
                recommendCity += f"{names},"
            if len(recommendCity) > 0:
                print("Province not found!")
                if "," in recommendCity[0:-1]:
                    print(f"Possible provinces:{recommendCity[0:-1]}")  # -1 to remove comma
                else:
                    print(f"Possible province:{recommendCity[0:-1]}")
            else:
                print("Province not found!")
        else:
            checker1 = False

    while checker2:
        cityTwo = input("Arrival province:\n")
        if cityOne.upper() == cityTwo.upper():
            print("Enter a different province!")
        elif cityTwo.upper() not in invalidChecker:  # Recommended city design
            recommendCity = ""
            sorter22 = []
            for names in invalidChecker:
                length2 = len(cityTwo)
                if names[0:length2].upper() == cityTwo.upper():
                    sorter22.append(names)
            sorter22.sort()
            for names in sorter22:
                recommendCity += f"{names},"  # Alphabetical sorting operations
            if len(recommendCity) > 0:
                print("Province not found!")
                if "," in recommendCity[0:-1]:
                    print(f"Possible provinces:{recommendCity[0:-1]}")  # -1 to remove comma
                else:
                    print(f"Possible province:{recommendCity[0:-1]}")
            else:
                print("Province not found!")
        elif cityTwo.upper() in invalidChecker:
            checker2 = False

    vCheck = ["CAR", "MOTORCYLE", "BICYLE"]  # Vehicle validation


    while checker3:
        vehicle = input("Enter travel type:\n")
        if vehicle.upper() in vCheck:
            checker3 = False

    for cityName in realCities:
        if cityOne.upper() == cityName[0].upper():      # Distance Calculation
            x1 = float(cityName[1])
            y1 = float(cityName[2])
    for cityName in realCities:
        if cityTwo.upper() == cityName[0].upper():
            x2 = float(cityName[1])
            y2 = float(cityName[2])

    dx = x2 - x1
    dy = y2 - y1
    distance = (((dx * dx) + (dy * dy)) ** (1 / 2)) * 100
    print()
    print(f"I am calculating the distance between {cityOne.upper()} and {cityTwo.upper()} ...\n")
    lastDistance = f"{round(distance, 2)}"
    print(f"Distance: {lastDistance} km")

    for lists in vehicleList:
        if vehicle.upper() == lists[0].upper():  # Speed calculation
            speed = lists[1]

    timeCalculate = float(lastDistance) / float(speed)  # Time calculation
    hour = str(timeCalculate).split(".")[0]
    minutes = (timeCalculate - int(hour)) * 60
    realMinute = str(minutes).split(".")[0]
    time = f"Approximate travel time with {vehicle.upper()}: {hour} hours {realMinute} minutes"
    print(time)

    closeOne = ""  # Closes city suggest
    closeTwo = ""
    closethree = ""
    close1 = 99999999999999
    close2 = 99999999999999
    close3 = 99999999999999
    sorter = []
    for realCitie in realCities:
        if realCitie[0].upper() != cityOne.upper():
            x3 = float(realCitie[1])
            y3 = float(realCitie[2])
            dl = ((((x1 - x3) * (x1 - x3)) + ((y1 - y3) * (y1 - y3))) ** (1 / 2))
            if dl < close1:
                close3 = close2
                close2 = close1
                close1 = dl
                closethree = closeTwo
                closeTwo = closeOne
                closeOne = realCitie[0]
            elif dl < close2:
                close3 = close2
                close2 = dl
                closethree = closeTwo
                closeTwo = realCitie[0]
            elif dl < close2:
                close3 = dl
                close3 = realCitie[0]
            else:
                pass
    sorter = [closeOne, closeTwo, closethree]  # Alphabetical sorting operations
    sorter.sort()
    print(f"Recommended places close to {cityOne.upper()}:{sorter[0]},{sorter[1]},{sorter[2]}")
    break
