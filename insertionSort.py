# insertion sort in the same array
def insertionSort(lst):
  counter=0
  for i in lst:
  	for j in range(counter+1):
  	  if lst[j]>=i:
  	  	position=j
  	  	break
  	lst[position+1:counter+1]=lst[position:counter]
  	lst[position]=i
  	counter+=1

#insertion sort can be done easily in a linked list, just search for the position, and insert it there
# insertion sort can also be implemented using stacks and queues



lst=[5,1,6,11,0, 10, 256,2, 4, 1, 1,7,7,4,8,3,2,9]
insertionSort(lst)
print lst
