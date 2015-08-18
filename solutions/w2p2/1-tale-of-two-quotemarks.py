import re

regex = re.compile(r"\"(.+?)\"")
file = open("atotc.txt").read()

matches = regex.findall(file)
print("\n".join(matches), end="")

if matches:
  print()

