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

for line in input:
  print(symbol_points(line))
