import re
from functools import reduce

matched_hands = []

lines = open("inputfull.txt").read().split("\n")

times = re.findall("\d+", lines[0].replace(" ", ""))
distances = re.findall("\d+", lines[1].replace(" ", ""))
total_wins = []
for i in range(0, len(times)):

    race_time = int(times[i])
    race_distance = int(distances[i])
    wins = 0

    for speed in range(0, int(times[i]) + 1):

        time_left = race_time - speed
        distance_travelled = speed * time_left

        if distance_travelled > race_distance:
            wins += 1

    total_wins.append(wins)
    wins = 0
print("Total Wins Together : %s" % reduce(lambda x, y: x * y, total_wins))
