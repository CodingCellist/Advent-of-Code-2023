import sys

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# PART-1 #

# a symbol point is a character which is not `.` or a digit, along with its
# position in the line
def symbol_points(line: str):
  return [ (i, line[i])
           for i in range(len(line))
           if not line[i].isdigit() and line[i] != '.'
           ]

# get a line's numbers along with their position in the line
def number_points(line: str):
  no_pts = []
  number = None
  pts = []
  for i in range(len(line)):
    c = line[i]
    if c.isdigit() and number is None:
      number = str(c)
      pts.append(i)
    elif c.isdigit() and number is not None:
      number += str(c)
      pts.append(i)
    # c is no longer a digit, and we've accumulated some number in str-form
    elif number is not None:
      # add the new number along with its digit-points...
      no_pts.append(
        (pts, int(number))
      )
      # ... and then

# oh god, 2D grid navigation, noooo!



# SOLUTION #


input = [ "467..114.."
        , "...*......"
        , ".35..633."
        , ".....#..."
        , "17*......"
        , "....+.58."
        , ".592....."
        , ".....755."
        , "..$.*...."
        , "664.598.."
        ]

# there's probably a different way to do this, but this is easy
line_no = 0

prev_line = None
next_line = None
has_symbols = False

for line in input:

  sym_pts = symbol_points(line)
  # if we found a symbol, we need to read the next line to check for
  # surrounding part numbers
  has_symbols = len(sym_pts) != 0

  # final steps in loop
  if has_symbols:
    prev_line = line
  line_no += 1
