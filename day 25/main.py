import numpy as np

with open("Input.txt") as f:
  file = f.read().split("\n")

matrix = []
for i in range(len(file)):
  temp = []
  
  for l in file[i].split(","):
    temp.append(int(l))
    
  matrix.append(temp)

a = np.array(matrix)
for i in range(len(matrix)-1):
  