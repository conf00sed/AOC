def calories():
  
  with open("Input.txt") as f:
    file = f.read().split('\n\n')
    file = [[int(j) for j in i.splitlines()] for i in file]

  calList = []
  for elf in file:
    calSum = 0
    
    for cals in elf:
      calSum += cals
      
    calList.append(calSum)

  return sorted(calList, reverse = True)

print(calories()[0])
print(sum(calories()[:3]))
