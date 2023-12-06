import sys

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# Part 1 #

# speed == time_held
def calc_total_dist(speed: int, time_remaining: int):
  return speed * time_remaining


# Okay so. We have a lower and upper bound, there must be a curve for these

#     distance
#      ^
#   13 |
#   12 |           x   x
#   11 |
#   10 |       x           x
#   *9 |
#    8 |
#    7 |
#    6 |   x                   x
#    5 |
#    4 |
#    3 |
#    2 |
#    1 |
#      +---------------------------x-----> time
#      0   1   2   3   4   5   6   7
#


# SOLUTION #

# FIXME: For testing only
input = ["Time:      7  15   30", "Distance:  9  40  200"]

for line in input:
