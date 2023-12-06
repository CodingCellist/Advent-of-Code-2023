import sys
from math import sqrt

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
#   *9 | - - - - - - - - - - - - - - - -
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

# Right then, do I remember any high school maths?...  ^^;;
#
# Yes, but only in Danish somehow?...
#
# dist = holdt * (tid - holdt)
#
# dist = holdt * tid - holdt^{2}
#    0 = - holdt^{2} + tid * holdt - dist   [omskrevet]
#
# `holdt` er vores x-værdi, så vi skal finde rødderne for den
#
# d = b^{2} - 4ac
#
# holdt1, holdt2 = \frac{ -b \pm \sqrt{ d } }{ 2a }
#
#   a := -1
#   b := tid
#   c := dist
#
# Hvordan ser det ud?...

def løs(dist: int, tid: int):
  d = (tid ** 2) - 4 * (-1) * dist
  if d < 0:
    print("Unreal!!")
    exit(1)
  rod1 = ((-tid) - sqrt(d)) / (2 * -1)
  rod2 = ((-tid) + sqrt(d)) / (2 * -1)
  return rod1, rod2



# SOLUTION #

lines = input.readlines()
# FIXME: For testing only
lines = ["Time:      7  15   30", "Distance:  9  40  200"]

# ah Python, I've missed the fun little one-line list comprehension shenanigans
pairs = [(int(t), int(d)) for t, d in zip(lines[0].split()[1:],
                                          lines[1].split()[1:])]
for t, d in pairs:
  print(løs(d, t))
