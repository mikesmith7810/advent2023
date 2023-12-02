import re

games_powers = []


def match_colour(line, regex, ):
    max_cubes = 0
    for match in re.finditer(regex, line):
        if int(match.group()) > max_cubes:
            max_cubes = int(match.group())
    return max_cubes


for i, line in enumerate(open("inputfull.txt").readlines()):
    max_red = match_colour(line, "..(?= red)")
    max_green = match_colour(line, "..(?= green)")
    max_blue = match_colour(line, "..(?= blue)")

    games_powers.append(max_red * max_green * max_blue)

print("Total Game Powers : %s" % sum(games_powers))
