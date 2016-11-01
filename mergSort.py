def mergeSort(lst):
  l=len(lst)
  if l<2:
    return
  mergeSort(lst[:l/2])
  mergeSort(lst[l/2:])
  ls=[]
  Rhalf=lst[:l/2]
  Lhalf=lst[l/2:]
  while Rhalf or Lhalf:
    if Rhalf[0]>Lhalf[0]:
      ls.append(Lhalf.pop(0))
    else:
      ls.append(Rhalf.pop(0))



lst=[9,1,6,11,0, 10, 256,5, 4, 1, 1,7,7,4,8,3,2,3]
mergeSort(lst)
print lst
