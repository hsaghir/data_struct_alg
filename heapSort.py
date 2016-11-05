def heapify(lst):
  if len(lst)<2:
    return
  count=0
  while 2*count+2<len(lst):
    if lst[count]<lst[2*count+1] or lst[count]<lst[2*count+2]:
      if lst[2*count+1]>lst[2*count+2]:
        tmp=2*count+1
      else:
        tmp=2*count+2
      lst[count], lst[tmp]=lst[tmp], lst[count]
      tmp=count
      while (tmp-1)/2>=0:
        if lst[tmp]>lst[(tmp-1)/2]:
          lst[tmp], lst[(tmp-1)/2]=lst[(tmp-1)/2],lst[tmp]
        tmp=(tmp-1)/2
    count+=1 #O(N)


def reHeapify(lst):
  if len(lst)<2:
    return

  lst.insert(0,lst.pop())
  count=0
  while 2*count+2 <len(lst):
    if lst[count]<lst[2*count+1] or lst[count]<lst[2*count+2]:
      if lst[2*count+1]>lst[2*count+2]:
        tmp=2*count+1
      else:
        tmp=2*count+2

      lst[tmp], lst[count]=lst[count],lst[tmp]
      count=tmp #O(logN)
    else:
      return


lst=[9,1,6,11,0, 10, 256,5, 4, 1, 1,7,7,4,8,3,2,3]
print lst

heapify(lst)  #O(N)
sortedLst=[]

while len(lst)>0: #O(N)
  sortedLst.insert(0,lst.pop(0))
  reHeapify(lst) #O(logN)

print sortedLst #O(NlogN)
