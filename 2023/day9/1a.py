lines = open("inputfull.txt").readlines()
directions = []
nodes = {}
for i, line in enumerate(lines):
    stripped_line = line.strip('\n')
    if i == 0:
        for direction in stripped_line:
            directions.append(direction)
    elif i != 1:
        split_line = stripped_line.split("=")
        nodes[split_line[0].strip()] = [split_line[1].strip()[1:4],split_line[1].strip()[6:9]]

# print(directions)
# print(nodes)

current_node = "AAA"
steps = 0
i = 0
j = 0
while current_node != "ZZZ":

    steps += 1
    if directions[i] == "L":
        current_node = nodes[current_node][0]
    elif directions[i] == "R":
        current_node = nodes[current_node][1]

    if current_node == "ZZZ":
        break

    if i+1 < len(directions):
        i += 1
    else:
        i = 0

    j += 1

print(steps)