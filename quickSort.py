import random

def quickSort(lst, f, l):
  if f>=l: return
  
  i,j=f,l
  pvt=lst[random.randint(f,l)]

  while i<j:
    while lst[i]<pvt : i+=1
    while lst[j]>pvt : j-=1
    if i<=j:
      lst[i],lst[j]=lst[j],lst[i]
      i+=1; j-=1
    print "pivot:",pvt,"i:",i,"j:",j,lst[f:l]
  quickSort(lst, f,j)
  quickSort(lst,i,l)


lst=[9,1,6,11,0, 10, 256,5, 4, 1, 1,7,7,4,8,3,2,3]
quickSort(lst, 0,len(lst)-1)
print lst
