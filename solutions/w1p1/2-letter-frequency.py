input = input("Enter some text: ")

letterCounts = {}

for char in input:
   if char.isalpha():
      char = char.lower()
      if not char in letterCounts:
        letterCounts[char] = 1
      else:
        letterCounts[char] = letterCounts[char] + 1

for key, value in letterCounts.items():
    print("{} {}".format(key, value))

