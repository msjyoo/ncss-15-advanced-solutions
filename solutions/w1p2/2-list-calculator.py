def list_calculator(list1, list2, operator):
  output = []
  if operator == "+":
    for key, value in enumerate(list1):
      output.append(value + list2[key])
  else:
    for key, value in enumerate(list1):
      output.append(value - list2[key])
  return output

