import re
import sys

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# PART 1 #

def get_game_no(line: str):
  # search returns a Match object, which we can index (why, python?) to get
  # the first matching string (subsequent indices returns parenthesised
  # subgroups; none used here)
  return int(re.search(r"\d+", line)[0])


# only to be used on list of matches
def matches_to_cube_nos(matches: list):
  # extract the numbers from each match, and convert to an integer
  return [int(re.match(r"\d+", m)[0]) for m in matches]


def get_highest_blue(line: str):
  blues = re.findall(r"\d+ blue", line)
  blue_nos = matches_to_cube_nos(blues)
  return max(blue_nos)


def get_highest_green(line: str):
  greens = re.findall(r"\d+ green", line)
  green_nos = matches_to_cube_nos(greens)
  return max(green_nos)


def get_highest_red(line: str):
  reds = re.findall(r"\d+ red", line)
  red_nos = matches_to_cube_nos(reds)
  return max(red_nos)


max_red = 12
max_green = 13
max_blue = 14


# SOLUTION #

game_sum = 0

power_sum = 0

for line in input:
  game_no = get_game_no(line)
  blue = get_highest_blue(line)
  green = get_highest_green(line)
  red = get_highest_red(line)

  # PART-2 #
  power = blue * green * red
  power_sum += power
  # /PART-2 #

  # if any of the highest number of cubes is greater than its maximum
  # theoretical number of cubes, the game wasn't possible; move on
  if blue > max_blue or green > max_green or red > max_red:
    continue

  game_sum += game_no

print(f"Part 1: {game_sum}")
print(f"Part 2: {power_sum}")
