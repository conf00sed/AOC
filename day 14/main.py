from collections import Counter

with open('input.txt') as f:
  file = f.readlines()

S = file[0].strip('\n')
R = {}
for x in file[2:]:
  set = x.strip('\n').split(' -> ')
  R[set[0]] = set[1]

