import re

file = open("code.py").read()

# Remove quote escapes and multilines
file = file.replace("\\\"", "")
file = file.replace("\\\'", "")
file = file.replace("\\", "")

# Remove double-quoted strings
matches = re.findall("(\"(?:.|\n)*?\")", file)
for match in matches:
  file = file.replace(match, "")
  
# Remove single-quoted strings
matches = re.findall("(\'(?:.|\n)*?\')", file)
for match in matches:
  file = file.replace(match, "")

# Remove single-line comments
matches = re.findall("\#.*", file)
for match in matches:
  file = file.replace(match, "")

# Find all assignments - https://regex101.com/r/dC8lS5/14
matches = re.findall("(?<!\W(?<![;|:|\s]))(?:(?P<var>\w+)\s*?\=\s*?\{(?:.|\s|\n)*?\})", file)

for match in matches:
  print(match)

