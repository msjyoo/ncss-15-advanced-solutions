with open("lines.txt") as f:
  lineCount = 0
  for line in f:
    words = line.split()
    lineCount = lineCount + 1;
    if line.strip() == "":
      print("Line {} is ascending.".format(lineCount))
    elif words == sorted(words):
      fail = False
      for key, value in enumerate(words):
        if key+1 < len(words) and value == words[key+1]:
          fail = True
          break
      if fail == False:
        print("Line {} is ascending.".format(lineCount))

