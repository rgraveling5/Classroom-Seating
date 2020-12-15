def lornshill():
  name = []
  atNumber = 0
  higherCount=0
  n5Count=0
  spareAllocated =0
  posNumber =0

  response = input('Would you like to start program? Y or N: ').upper()
  print()
  while response == 'Y':
    types = input('Higher(H) or Nat5(N)? X to exit: ').upper()
    name.append(types)
    atNumber = atNumber + 1
    if types == 'H':
      higherCount = higherCount +1
    if types == 'N':
      n5Count = n5Count +1
    if types == 'X':
      break
  
  if higherCount <10 and response == 'Y':
    print('Not enough higher pupils')
    exit()
  
  if atNumber ==20:
    print('Class allocated successfully')

  if atNumber > 20:
    sparePlaces = 20 - higherCount
    spareAllocated = 0
    posNumber = 0
    while spareAllocated < sparePlaces:
      if name[posNumber] == 'N':
        print()
        print('Number', posNumber + 1, 'is allocated a seat')
        spareAllocated = spareAllocated + 1
      posNumber = posNumber + 1
      if sparePlaces <= 0:
        print('No spaces left')
    exit()

    
  if response != ('Y'):
    exit()

def exit():
  print()
  print('End of Program')

lornshill()


