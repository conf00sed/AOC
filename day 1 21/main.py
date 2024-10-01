def sonarSweep():
  with open('input.txt', 'r') as f:
    scan = []
    for line in f.readlines():
      scan.append(int(line.strip('\n')))

  count = 0
  deeper = 0
  for depth in scan:
    prev = scan[count-1]
    print(prev)
    print(depth)
    if depth > prev:
      deeper += 1
    count+=1

  print(deeper)
sonarSweep()


def windowSweep():
  with open('input.txt', 'r') as f:
    scacn=[]
    for line in f.readlines():
      scan.append(int(line.strip('\n')))

  

windowSweep()