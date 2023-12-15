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
        nodes[split_line[0].strip()] = [split_line[1].strip()[1:4], split_line[1].strip()[6:9]]

current_ghost_nodes = []

for node in nodes:
    if node[2:] == "A":
        current_ghost_nodes.append(node)

steps = 0
i = 0
j = 0
end_of_game = False
while not end_of_game:
    steps += 1

    if directions[i] == "L":
        new_ghost_nodes = []
        for ghost_node in current_ghost_nodes:
            new_ghost_nodes.append(nodes[ghost_node][0])
        current_ghost_nodes = new_ghost_nodes
    elif directions[i] == "R":
        new_ghost_nodes = []
        for ghost_node in current_ghost_nodes:
            new_ghost_nodes.append(nodes[ghost_node][1])
        current_ghost_nodes = new_ghost_nodes

    end_of_game = True

    for ghost_node in current_ghost_nodes:
        if ghost_node[2:] != "Z":

            end_of_game = False
        # else:
            # print(ghost_node)

    if i + 1 < len(directions):
        i += 1
    else:
        i = 0

    j += 1

print(steps)
