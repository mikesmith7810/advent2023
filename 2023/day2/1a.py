import re

max_red = 12
max_green = 13
max_blue = 14

valid_games = []


def match_colour(line, regex, max):
    for match in re.finditer(regex, line):
        if int(match.group()) > max:
            return True
    return False


for i, line in enumerate(open("inputfull.txt").readlines()):
    if match_colour(line, "..(?= red)", max_red):
        continue
    if match_colour(line, "..(?= green)", max_green):
        continue
    if match_colour(line, "..(?= blue)", max_blue):
        continue
    valid_games.append(i + 1)

print("Valid Games Total : %s" % sum(valid_games))
