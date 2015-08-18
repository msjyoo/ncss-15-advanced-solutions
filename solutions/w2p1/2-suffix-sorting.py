lines = []

for line in open("words.txt"):
  lines.append(line.strip())

reversed = [word[::-1] for word in lines]

for key, value in enumerate(sorted(reversed)):
  print(value[::-1])

