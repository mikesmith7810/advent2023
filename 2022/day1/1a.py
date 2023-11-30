elfCalories = []


def read_calories():
    global lines, line
    calories = 0
    lines = open("inputfull.txt").readlines()
    for i, line in enumerate(lines):
        stripped_line = line.strip('\n')
        if stripped_line != "":
            calories = calories + int(stripped_line)
            if i == len(lines) - 1:
                elfCalories.append(calories)
        else:
            elfCalories.append(calories)
            calories = 0


read_calories()

print("Max Calories : %s" % max(elfCalories))


