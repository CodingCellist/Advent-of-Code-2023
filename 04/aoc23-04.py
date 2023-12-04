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

def parse_card(line: str):
  # start by splitting into winning and haves
  raw_wins, raw_haves = line.split('|')
  # then remove the "Card \d+:" part from `raw_wins`
  raw_wins = raw_wins.split(':')[-1]
  # finally, cast to a list of actual numbers
  wins = [ int(n) for n in raw_wins.split(' ') if n != '' ]
  haves = [ int(n) for n in raw_haves.split(' ') if n != '' ]
  # and return as a dict with sensibly named keys
  return {"wins": wins, "haves": haves}


# SOLUTION #

### # FIXME: only for testing
### input = [ "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
###         , "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"
###         , "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"
###         , "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"
###         , "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36"
###         , "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
###         ]

total_pts = 0

for line in input:
  # get the winning and obtained numbers
  card = parse_card(line)

  # count the number of winning cards
  n_winning = len([ x for x in card["haves"] if x in card["wins"] ])

  # and at this point, if we have any winning numbers, the points are just
  # powers of 2 (`n_wins - 1` since first power is 2^0)
  if n_winning != 0:
    total_pts += pow(2, n_winning - 1)

print(f"Part 1: {total_pts}")
