numberDict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
              "nine": "9"}


def read_calibration():
    global lines, line
    calibration_lines = []
    lines = open("inputfull.txt").readlines()
    for i, line in enumerate(lines):
        stripped_line = line.strip('\n')
        calibration_lines.append(stripped_line)
    return calibration_lines


def extract_calibration(direction, line):
    calibration = ""
    potential_number = ""
    finished = False

    for digit in line[::direction]:
        if not digit.isalpha():
            calibration += digit
            finished = True
        else:
            potential_number = potential_number + digit
            for i, digit in enumerate(potential_number[::direction]):
                if numberDict.get(potential_number[i:len(potential_number)][::direction]):
                    if numberDict.get(potential_number[i:len(potential_number)][::direction]):
                        calibration += str(numberDict.get(potential_number[i:len(potential_number)][::direction]))
                        potential_number = ""
                        finished = True
        if finished:
            break
    return calibration


calibrations = []
for line in read_calibration():
    line_calibrations = extract_calibration(1, line)
    line_calibrations = line_calibrations + extract_calibration(-1, line)

    calibrations.append(line_calibrations)
    line_calibration = ""

calibrationTotal = 0
for line_calibration in calibrations:
    calibrationTotal = calibrationTotal + int(line_calibration)

print("Calibration Total : %s" % calibrationTotal)
