def mergeSort(lst):
  l=len(lst)
  if l<2:
    return lst
  ls=[]
  Lhalf=lst[:l/2]
  Rhalf=lst[l/2:]
  Lhalf=mergeSort(Lhalf)
  Rhalf=mergeSort(Rhalf)

  while len(Rhalf)>0 or len(Lhalf)>0:
    if len(Rhalf)>0 and len(Lhalf)>0:
      if Rhalf[0]>Lhalf[0]:
        ls.append(Lhalf.pop(0))
      else:
        ls.append(Rhalf.pop(0))
    elif len(Rhalf)>0:
      ls.append(Rhalf.pop(0))
    else:
      ls.append(Lhalf.pop(0))
    print ls
  return ls





lst=[9,1,6,11,0, 10, 256,5, 4, 1, 1,7,7,4,8,3,2,3]
print lst
print mergeSort(lst)