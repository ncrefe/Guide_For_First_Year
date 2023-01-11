equation1 = input("Enter the first equation:\n")  # User is asked to input the first equation
equation2 = input("Enter the second equation:\n")  # User is asked to input the second equation
print("Equations in the simplified form:")
list1 = equation1.split("=")
firstside = list1[0].split("+")
secondSide = list1[1].split("+")
negate = []
posit = []
negateX = []
negateY = []
negateConstant = []
positX = []
positY = []
positConstant = []

# Splitting the equation into left and right side and then into terms
for term in firstside:
    if term.count("-") > 1:
        moreThan = term.split("-")
        posit.append(moreThan[0])
        for than in range(1, term.count("-") + 1):
            negate.append(moreThan[than])
    elif "-" in term:
        negativeValues = term.split("-")
        posit.append(negativeValues[0])
        negate.append(negativeValues[1])
    else:
        posit.append(term)
for term in secondSide:
    if term.count("-") > 1:
        moreThan = term.split("-")
        negate.append(moreThan[0])
        for than in range(1, term.count("-") + 1):
            posit.append(moreThan[than])
    elif "-" in term:
        negativeValues = term.split("-")
        negate.append(negativeValues[0])
        posit.append(negativeValues[1])
    else:
        negate.append(term)

# Separating variables and constants
for signLooker in negate:
    if "x" in signLooker:
        negateX.append(signLooker)
    elif "y" in signLooker:
        negateY.append(signLooker)
    else:
        negateConstant.append(signLooker)
for signLooker in posit:
    if "x" in signLooker:
        positX.append(signLooker)
    elif "y" in signLooker:
        positY.append(signLooker)
    else:
        positConstant.append(signLooker)
posit.pop(0)
sumx = 0

#Summing values of x and y
for items in negateX:
    get = items.split("x")
    sumx -= int(get[0])
for items in positX:
    get = items.split("x")
    sumx += int(get[0])
sumy = 0
for items in negateY:
    get = items.split("y")
    sumy -= int(get[0])
for items in positY:
    get = items.split("y")
    sumy += int(get[0])
sumc = 0
for items in negateConstant:
    if items == "":
        pass
    else:
        sumc += int(items)
for items in positConstant:
    if items == "":
        pass
    else:
        sumc -= int(items)

list2 = equation2.split("=")
firstside2 = list2[0].split("+")
secondSide2 = list2[1].split("+")
negate2 = []
posit2 = []
negateX2 = []
negateY2 = []
negateConstant2 = []
positX2 = []
positY2 = []
positConstant2 = []
for term in firstside2:
    if term.count("-") > 1:
        moreThan = term.split("-")
        posit2.append(moreThan[0])
        for than in range(1, term.count("-") + 1):
            negate2.append(moreThan[than])
    elif "-" in term:
        negativeValues = term.split("-")
        posit2.append(negativeValues[0])
        negate2.append(negativeValues[1])
    else:
        posit2.append(term)
for term in secondSide2:
    if term.count("-") > 1:
        moreThan = term.split("-")
        negate2.append(moreThan[0])
        for than in range(1, term.count("-") + 1):
            posit2.append(moreThan[than])
    elif "-" in term:
        negativeValues = term.split("-")
        negate2.append(negativeValues[0])
        posit2.append(negativeValues[1])
    else:
        negate2.append(term)
for signLooker in negate2:
    if "x" in signLooker:
        negateX2.append(signLooker)
    elif "y" in signLooker:
        negateY2.append(signLooker)
    else:
        negateConstant2.append(signLooker)
for signLooker in posit2:
    if "x" in signLooker:
        positX2.append(signLooker)
    elif "y" in signLooker:
        positY2.append(signLooker)
    else:
        positConstant2.append(signLooker)
posit2.pop(0)
sumx2 = 0

for items in negateX2:
    get = items.split("x")
    sumx2 -= int(get[0])
for items in positX2:
    get = items.split("x")
    sumx2 += int(get[0])
sumy2 = 0
for items in negateY2:
    get = items.split("y")
    sumy2 -= int(get[0])
for items in positY2:
    get = items.split("y")
    sumy2 += int(get[0])
sumc2 = 0
for items in negateConstant2:
    if items == "":
        pass
    else:
        sumc2 += int(items)
for items in positConstant2:
    if items == "":
        pass
    else:
        sumc2 -= int(items)

matx = int(sumx2) * int(sumx)
maty = int(sumx2) * int(sumy)
matc = int(sumx2) * int(sumc)
maty2 = int(sumx) * int(sumy2)
matc2 = int(sumx) * int(sumc2)
matx2 = int(sumx) * int(sumx2)
lasty = (matc - matc2) / (maty - maty2)

if sumx == 0:
    lastx = (sumc2 - (lasty * sumy2)) / sumx2
else:
    lastx = (sumc - (lasty * sumy)) / sumx
a = max(sumx, sumy, sumc)
b = max(sumx2, sumy2, sumc2)
ebob = 1
ebob2 = 1
for i in range(1, a + 1):
    if sumx == 0:
        if (sumy % i == 0) and (sumc % i == 0):
            ebob = i
    elif sumy == 0:
        if (sumx % i == 0) and (sumc % i == 0):
            ebob = i
    elif (sumx2 % i == 0) and (sumy2 % i == 0) and (sumc2 % i == 0):
        ebob2 = i
for i in range(1, b + 1):
    if sumx2 == 0:
        if (sumy2 % i == 0) and (sumc2 % i == 0):
            ebob2 = i
    elif sumy2 == 0:
        if (sumx2 % i == 0) and (sumc2 % i == 0):
            ebob2 = i
    elif (sumx2 % i == 0) and (sumy2 % i == 0) and (sumc2 % i == 0):
        ebob2 = i

ebobx = sumx / ebob
eboby = sumy / ebob
ebobc = sumc / ebob
ebobx2 = sumx2 / ebob2
eboby2 = sumy2 / ebob2
ebobc2 = sumc2 / ebob2

if "x" not in equation1:
    if sumy >= 0:
        print(f"0x+{int(sumy)}y={int(sumc)}")
    else:
        print(f"0x{int(sumy)}y={int(sumc)}")
elif "y" not in equation1:
    print(f"{int(sumx)}x+0y={int(sumc)}")
elif eboby >= 0:
    print(f"{int(ebobx)}x+{int(eboby)}y={int(ebobc)}")
else:
    print(f"{int(ebobx)}x{int(eboby)}y={int(ebobc)}")
if "x" not in equation2:
    if sumy2 >= 0:
        print(f"0x+{int(sumy2)}y={int(sumc2)}")
    else:
        print(f"0x{int(sumy2)}y={int(sumc2)}")
elif "y" not in equation2:
    print(f"{int(sumx2)}x+0y={int(sumc2)}")
elif eboby2 >= 0:
    print(f"{int(ebobx2)}x+{int(eboby2)}y={int(ebobc2)}")
else:
    print(f"{int(ebobx2)}x{int(eboby2)}y={int(ebobc2)}")
print("Solution:")
print(f"x={int(lastx)}")
print(f"y={int(lasty)}")
