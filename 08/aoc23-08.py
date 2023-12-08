import sys
# heck yeah, let's do some streams!
from itertools import cycle
import math

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# Part 1 #

def add_map_entry(the_map: dict[str, (str, str)], raw_entry: str):
  # we can get the raw entries by splitting on whitespace, and removing the '='
  parts = [part for part in raw_entry.split() if part != '=']

  starting_pt = parts[0]
  # and the left/right can be extracted with a bit of string/list hacking  ^^
  left = (parts[1])[1:-1]
  right = (parts[2])[0:-1]
  the_map[starting_pt] = (left, right)


def steps_to_dest(our_map: dict[str, (str, str)], inf_dirns: cycle,
                  curr_posn="AAA", destn="ZZZ"):
  steps_taken = 0
  for dirn in inf_dirns:
    # If we've arrived, yay! We made it!
    if curr_posn == destn:
      return steps_taken

    # Otherwise, update our position by looking up our next options,
    # and moving according to the direction given to us
    lr_idx = 0 if dirn == 'L' else 1
    curr_posn = our_map[curr_posn][lr_idx]
    steps_taken += 1


# Part 2 #

def get_starting_posns(our_map: dict[str, (str, str)]):
  return [k for k in our_map.keys() if k[-1] == 'A']


# Slightly different from `steps_to_dest`, since the destination does not
# have to be triple 'Z', it just has to end in 'Z'.
# **AND** since the directions stream needs to be restarted at each step
# (fortunately small enough that that's not bad).
def ghost_n_steps(our_map: dict[str, (str, str)], raw_dirns: cycle, posn: str):
  n_steps = 0
  for dirn in cycle(raw_dirns):
    if posn[-1] == 'Z':
      return n_steps

    lr_idx = 0 if dirn == 'L' else 1
    posn = our_map[posn][lr_idx]
    n_steps += 1


#
def ghost_traverse(our_map: dict[str, (str, str)], raw_dirns: str):
  start_posns = get_starting_posns(our_map)
  # Not all paths sync up at the same time, but surely we can cache/record
  # the length of the ones we've encountered?...
  # Hey! Hey hey hey! The paths which do not sync up immediately seem to repeat!
  path_cycles = dict()    # using starting position as key?
  while start_posns != []:
    start_posn = start_posns.pop(0)
    path_len = ghost_n_steps(our_map, raw_dirns, start_posn)

    print(f"Cycle of {path_len} found for {start_posn}!")

    path_cycles[start_posn] = path_len

  return path_cycles

# SOLUTION #

### # FIXME: only for testing
### input2 = [ "RL"
###          , ""
###          , "AAA = (BBB, CCC)"
###          , "BBB = (DDD, EEE)"
###          , "CCC = (ZZZ, GGG)"
###          , "DDD = (DDD, DDD)"
###          , "EEE = (EEE, EEE)"
###          , "GGG = (GGG, GGG)"
###          , "ZZZ = (ZZZ, ZZZ)"
###          ]
###
### input6 = [ "LLR"
###          , ""
###          , "AAA = (BBB, BBB)"
###          , "BBB = (AAA, ZZZ)"
###          , "ZZZ = (ZZZ, ZZZ)"
###          ]
###
part2_input = [ "LR"
              , ""
              , "11A = (11B, XXX)"
              , "11B = (XXX, 11Z)"
              , "11Z = (11B, XXX)"
              , "22A = (22B, XXX)"
              , "22B = (22C, 22C)"
              , "22C = (22Z, 22Z)"
              , "22Z = (22B, 22B)"
              , "XXX = (XXX, XXX)"
              ]
# input = part2_input

first_line = True
map_dict = dict()
dirn_cycle = None
raw_dirns = None

lcount = 0

for line in input:
  # Remember that newlines are characters...  -_-
  line = line.strip()
  # initialise the cycle of directions
  if first_line:
    dirn_cycle = cycle(line)
    raw_dirns = line
    first_line = False
    lcount += 1
    continue
  # skip the blank line
  if line == "":
    lcount += 1
    continue

  # parse the dictionary of map entries
  add_map_entry(map_dict, line)
  lcount += 1

if dirn_cycle is None or raw_dirns is None:
  print(f"[FATAL] dirn_cycle={dirn_cycle}  raw_dirns={raw_dirns}")
  exit(1)

### print("Part 1:", steps_to_dest(map_dict, dirn_cycle))

part2_cycles = ghost_traverse(map_dict, raw_dirns)
print("Part 2 cycles:", part2_cycles)
# I love the python stdlib  <3
# (Oh and I hate the cryptic asterisk operator; very useful for unpacking the
# values here, absolutely, but also very cursed...)
print("Part 2:", math.lcm(*part2_cycles.values()))
