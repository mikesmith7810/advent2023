calibLines = []
calibrations = []
calibrationTotal = 0

def read_calibration():
    global lines, line
    lines = open("inputfull.txt").readlines()
    for i, line in enumerate(lines):
        stripped_line = line.strip('\n')
        calibLines.append(stripped_line)

read_calibration()


calibration = ""
for line in calibLines:
    for digit in line:
        if not digit.isalpha():
            calibration += digit
    calibrations.append(calibration[:1] + calibration[len(calibration) - 1:len(calibration)])
    calibration = ""

for calibration in calibrations:
    calibrationTotal = calibrationTotal + int(calibration)

print("Calibration Total : %s" % calibrationTotal)
