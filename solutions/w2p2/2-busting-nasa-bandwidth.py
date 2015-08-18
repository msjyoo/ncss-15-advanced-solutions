import re

minSize = int(input("Minimum response size: "))

data = open("access.log").read()

matches = re.findall(r"\[0[1-9]\/Jul\/1995.*\].*GET\s(?P<path>(?:\/images\/).+(?:\.gif|\.jpeg|\.jpg|\.png))\sHTTP\/1.0\"\s(?P<status>\d+)\s(?P<bytes>\d+)", data, re.IGNORECASE)
"""('/images/NASA-logosmall.gif', '304', '0')"""

x = []
bytes = 0

for match in matches:
  if int(match[1]) == 200 and int(match[2]) >= minSize:
    x.append(match)
    bytes += int(match[2])

print("# requests: {}\n# bytes: {}".format(len(x), bytes))

