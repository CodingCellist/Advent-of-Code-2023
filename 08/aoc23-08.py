import sys
# heck yeah, let's do some streams!
from itertools import cycle

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# Part 1 #

n_steps = 0


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
### input = input6

first_line = True
map_dict = dict()
dirn_cycle = None

lcount = 0

for line in input:
  # Remember that newlines are characters...  -_-
  line = line.strip()
  # initialise the cycle of directions
  if first_line:
    dirn_cycle = cycle(line)
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

if dirn_cycle is None:
  print("FATAL: Never created the directions cycle")
  exit(1)

print("Part 1:", steps_to_dest(map_dict, dirn_cycle))
