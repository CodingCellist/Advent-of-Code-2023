import sys
from math import floor
import numpy as np

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# Part 1 #

def find_refln(pat: np.array):
  pat_size = len(pat)
  prev_row = None

  for row_idx, row in enumerate(pat):
    if np.array_equal(row, prev_row):
      # calculate the max number of rows to compare (indices start at 0)
      rem_ahead = pat_size - (row_idx + 1)
      n_behind = row_idx - 1

      # we want to compare whichever one of those hits the size of the map first
      n_compare = min(n_behind, rem_ahead)

      perfect = True
      # remembering that `range` is exclusive and we're starting at 1
      for refl_idx in range(1, n_compare + 1):
        row_ahead = pat[row_idx + refl_idx]
        # need to subtract 1 more, since we're comparing with the previous row
        row_behind = pat[row_idx - refl_idx - 1]
        perfect = perfect and np.array_equal(row_behind, row_ahead)
      ###print(f"Bound: {bound}   Perfect: {perfect}")
      # if we've confirmed this is a perfect reflection, return the indices
      if perfect:
        ###print(f"{prev_row}\n perfectly matches\n{row}")
        # task requires us to index from 1
        return (row_idx, row_idx + 1)
    else:
      prev_row = row

  # if no reflection has been found, return a nothing-value
  return None


# SOLUTION #

# FIXME: only for testing
###input = [ "#.##..##."
###        , "..#.##.#."
###        , "##......#"
###        , "##......#"
###        , "..#.##.#."
###        , "..##..##."
###        , "#.#.##.#."
###        , ""
###        , "#...##..#"
###        , "#....#..#"
###        , "..##..###"
###        , "#####.##."
###        , "#####.##."
###        , "..##..###"
###        , "#....#..#"
###        ]

pattern = []
patterns = []

for line in input:
  line = line.strip()   # not risking that mistake again
  if line == "":
    patterns.append(np.array(pattern))
    pattern = []
  else:
    pattern.append([c for c in line])

# remember to include the final pattern
patterns.append(pattern)

###print(f"Patterns:\n{patterns}")

p1_summary = 0

for idx, pattern in enumerate(patterns):
  rows = find_refln(pattern)
  cols=None

  # only try columns if we did not find a reflected row
  # "you need to find a perfect reflection across EITHER a horizontal line"
  if rows is None:
    # column-search is just row-search on the transpose
    cols = find_refln(np.transpose(pattern))

    # vertical reflection (i.e. comparing columns) count for 1 each
    p1_summary += cols[0]
  else:
    # horizontal reflection (i.e. comparing rows) counts for 100 each
    p1_summary += rows[0] * 100

  ###print(f"rows, cols: {rows}, {cols}")

print(p1_summary)
