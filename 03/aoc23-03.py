import re
import sys

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# PART-1 #

# a symbol-point is a character which is not `.` or a digit, along with its
# position in the line
def symbol_points(line: str):
  return [ (i, c)
           for i, c in enumerate(line)
           if not c.isdigit() and c != '.'
           ]


# oh god, 2D grid navigation, noooo!

# idea: Store a list of numbers in a list along with their positions,
#       then remove from the list as we find things relative to the
#       symbol-points.
#       I _believe_ that should prevent counting duplicates...

def number_points(line: str):
  no_pts = []
  pts = []
  number_str = ""
  is_fst_digit = True

  for i, c in enumerate(line):
    if c.isdigit():
      number_str += c
      pts.append(i)
      if is_fst_digit:
        is_fst_digit = False
    else:
      # if c is not a digit, but we have accumulated a number
      if number_str != "":
        # add the new number-point to the list
        no_pts.append(
          (pts, int(number_str))
        )
        # reset the accumulators and flag
        pts = []
        number_str = ""
        is_fst_digit = True

  return no_pts


# SOLUTION #

# for testing
input = [ "467..114.."
        , "...*......"
        , "..35..633."
        , "......#..."
        , "617*......"
        , ".....+.58."
        , "..592....."
        , "......755."
        , "...$.*...."
        , ".664.598.."
        ]

### # there's probably a different way to do this, but this is easy
### line_no = 0
input_array = []

### has_symbols = False

# forget about streaming the file, I want the whole 2D array
for line in input:

  sym_pts = symbol_points(line)
  no_pts = number_points(line)

  print(f"Sym: {sym_pts}\nNo: {no_pts}\n")

  # TODO: do I still need this with the new idea?
  # store the line
  input_array.append(line)

  ### # if we found a symbol, we need to read the next line to check for
  ### # surrounding part numbers
  ### has_symbols = len(sym_pts) != 0
  ###
  ### line_no += 1

