max_calories = 0
loop_max_calories = 0

for i, line in enumerate(open('inputfull.txt', 'r').readlines()):
    strippedLine = line.strip('\n')

    if strippedLine != "":
        loop_max_calories = loop_max_calories + int(strippedLine)
    else:
        if loop_max_calories > max_calories:
            max_calories = loop_max_calories
        loop_max_calories = 0

print(max_calories)
