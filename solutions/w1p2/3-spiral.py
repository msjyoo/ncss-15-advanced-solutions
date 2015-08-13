output = ""

size = int(input("Enter size: "))

output += "-"*(size-1)
output += "\\"

iterations = 2
for _ in range(size-1):
    output += "|"*(size-iterations)
    output += "/"
    output += "-"*(size-iterations)
    output += "\\"
    iterations = iterations + 1
    
def generateMatrixSpiralCoordTuples(size):
  stepsRemaining = steps = ((size-1)*2)/4
  list = []
  
  for _ in range(size):
    list.append([_, 0])
  
  while stepsRemaining > 0:
    """ y-incr (South) """
    while list[-1][0] > list[-1][1]:
      list.append([list[-1][0], list[-1][1]+1])
      
    """ x-decr (West) """
    while list[-1][0] > (steps - stepsRemaining):
      list.append([list[-1][0] - 1, list[-1][1]])
      
    """ y-decr (North) """
    while list[-1][0]+1 < list[-1][1]:
      list.append([list[-1][0], list[-1][1]-1])
    
    """ x-incr (East) """
    while list[-1][0] < (size - (steps - stepsRemaining + 2)):
      list.append([list[-1][0] + 1, list[-1][1]])
      
    stepsRemaining -= 1
    
  return list
  
def stringToMatrix(string, mSize):
  matrix = {}
  for _ in range(mSize):
    matrix[_] = {}
  
  template = generateMatrixSpiralCoordTuples(mSize)
  
  counter = 0
  for coord in template:
    matrix[coord[1]][coord[0]] = string[counter]
    counter += 1
  
  return matrix

def printMatrix(matrix):
  for key, y in matrix.items():
    for key2, x in y.items():
        if key2 == len(y)-1:
          print("{}".format(x), end="")
        else:
          print("{} ".format(x), end="")
    print("")
  return

m = stringToMatrix(output, size)

printMatrix(m)

