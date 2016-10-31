def quickSort(lst):
  if len(lst)<2:
    return
  elif len(lst)==2:
    if lst[0]<=lst[1]:
      return
    else:
      tmp=lst[0]
      lst[0]=lst[1]
      lst[1]=tmp
  else:
    pvt=lst[(len(lst)-1)/2];lst[(len(lst)-1)/2]=None; hole=(len(lst)-1)/2
    idxR=len(lst)-1; idxL=0; counter=0
    while idxR>idxL:
      counter+=1
      if lst[idxL]>pvt and lst[idxR]<pvt and lst[idxR] and lst[idxL] :
        tmp= lst[idxL]
        lst[idxL]=lst[idxR]
        lst[idxR]=tmp
        idxL+=1;idxR-=1;
      elif lst[idxL]>pvt:
        lst[hole]=lst[idxL]
        lst[idxL]=None 
        hole=idxL
        idxR-=1
      elif lst[idxR]<pvt:
        lst[hole]=lst[idxR]
        lst[idxR]=None
        hole=idxR
        idxL+=1
      else:
        if lst[idxL]:
          idxL+=1
        if lst[idxR]:
          idxR-=1
    print "pivot:", pvt, lst
    lst[hole]=pvt


    quickSort(lst[:hole])
    # quickSort(lst[hole:])



lst=[9,1,6,11,0, 10, 256,5, 4, 1, 1,7,7,4,8,3,2,3]
quickSort(lst)
print lst
