plays = []

def read_plays():
    global lines, line
    lines = open("inputfull.txt").readlines()
    for i, line in enumerate(lines):
        plays.append(line.split())

read_plays()

round_points = 0

def switch(move):
    global round_points
    if move[1] == "X":
        round_points += 1
    elif move[1] == "Y":
        round_points += 2
    elif move[1] == "Z":
        round_points += 3


for move in plays:
    switch(move)
    if move[0] == "A":
        if move[1] == "Y":
            round_points += 6
        elif move[1] == "X":
            round_points += 3
    if move[0] == "B":
        if move[1] == "Z":
            round_points += 6
        elif move[1] == "Y":
            round_points += 3
    if move[0] == "C":
        if move[1] == "X":
            round_points += 6
        elif move[1] == "Z":
            round_points += 3

print("Round Points : %s" % round_points)
