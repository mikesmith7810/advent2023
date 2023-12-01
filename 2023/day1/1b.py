calibLines = []
line_calibrations = []
calibrations = []
calibrationTotal = 0


def read_calibration():
    global lines, line
    lines = open("inputfull.txt").readlines()
    for i, line in enumerate(lines):
        stripped_line = line.strip('\n')
        calibLines.append(stripped_line)


read_calibration()

numberDict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
              "nine": "9"}

calibration = ""
potentialNumber = ""
finished = False
for line in calibLines:
    finished = False
    for digit in line:
        if not digit.isalpha():
            calibration += digit
            finished = True
        else:
            potentialNumber = potentialNumber + digit
            if numberDict.get(potentialNumber):
                calibration += numberDict.get(potentialNumber)
                finished = True
                potentialNumber = ""
                break
            else:
                for i, digit in enumerate(potentialNumber):
                    if numberDict.get(potentialNumber[i:len(potentialNumber)]):
                        if numberDict.get(potentialNumber[i:len(potentialNumber)]):
                            calibration += str(numberDict.get(potentialNumber[i:len(potentialNumber)]))
                            potentialNumber = ""
                            finished = True
        if finished == True:
            break

    finished = False
    for digit in line[::-1]:
        if not digit.isalpha():
            calibration += digit
            finished = True
        else:
            potentialNumber = potentialNumber + digit
            if numberDict.get(potentialNumber):
                calibration += numberDict.get(potentialNumber)
                finished = True
                potentialNumber = ""
                break
            else:
                for i, digit in enumerate(potentialNumber[::-1]):
                    if numberDict.get(potentialNumber[i:len(potentialNumber)][::-1]):
                        if numberDict.get(potentialNumber[i:len(potentialNumber)][::-1]):
                            calibration += str(numberDict.get(potentialNumber[i:len(potentialNumber)][::-1]))
                            potentialNumber = ""
                            finished = True
        if finished == True:
            break

    calibrations.append(calibration)
    calibration = ""

for calibration in calibrations:
    calibrationTotal = calibrationTotal + int(calibration)

print("Calibration Total : %s" % calibrationTotal)
