def selectionSort(lst):
  for j in range(len(lst)-1):
    idx=j;minIdx=j
    minNum=lst[minIdx]
    for i in lst[j+1:]:
      idx+=1
      if i<minNum:
        minNum=i
        minIdx=idx
    lst[minIdx]=lst[j]
    lst[j]=minNum

lst=[5,1,6,11,0, 10, 256,2, 4, 1, 1,7,7,4,8,3,2,9]
selectionSort(lst)
print lst
