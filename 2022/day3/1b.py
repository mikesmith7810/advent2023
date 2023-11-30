rucksacks = []
total_priorities = 0

item_values = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
               "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22,
               "w": 23, "x": 24, "y": 25, "z": 26,
               "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37,
               "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48,
               "W": 49, "X": 50, "Y": 51, "Z": 52, }


def read_contents():
    global lines, rucksacks
    grouper = 0
    lines = open("inputfull.txt").readlines()
    for i, rucksack in enumerate(lines):
        grouper += 1
        if grouper == 3:
            rucksacks.append([lines[i].strip('\n'), lines[i - 1].strip('\n'), lines[i - 2].strip('\n')])
            grouper = 0


read_contents()

items = []
item_found = False
for rucksack in rucksacks:
    for item_a in list(rucksack[0]):
        for item_b in list(rucksack[1]):
            if item_a == item_b:
                for item_c in list(rucksack[2]):
                    if item_a == item_c:
                        item_found = True
                        break
                if item_found:
                    break
        if item_found:
            items.append(item_a)
            item_found = False
            break

for item in items:
    value = item_values.get(item)
    total_priorities += value

print("Total Priorities : %s" % total_priorities)
