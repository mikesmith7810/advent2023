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
        round_points += 0
    elif move[1] == "Y":
        round_points += 3
    elif move[1] == "Z":
        round_points += 6


for move in plays:
    switch(move)

    if move[1] == "Y":
        if move[0] == "A":
            round_points += 1
        elif move[0] == "B":
            round_points += 2
        elif move[0] == "C":
            round_points += 3

    if move[1] == "X":
        if move[0] == "A":
            round_points += 3
        elif move[0] == "B":
            round_points += 1
        elif move[0] == "C":
            round_points += 2

    if move[1] == "Z":
        if move[0] == "A":
            round_points += 2
        elif move[0] == "B":
            round_points += 3
        elif move[0] == "C":
            round_points += 1

print("Round Points : %s" % round_points)
