# pivot can be any (it may first ,last or mid element)
'''
in partition ,we divide the array into two part where left side element are less than pivot and viceversa.
logic take two pointer i,j
find the first element from starting which is greater than pivot (i)
find the first element from ending which is lesser than pivot(j)
if i<j swap i,j
else swap with pivot and change the pivot index
'''
def partitionwrtpivot(arr,start,end):
    pivot = arr[start]
    pivot_index = start
    i,j= start,end-1
    while(i<j):
        while i<end and arr[i]<=pivot:
            i+=1
        while j>start and arr[j]>=pivot:
            j-=1
        
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            arr[j],arr[pivot_index]=arr[pivot_index],arr[j]
            pivot_index=j
    return pivot_index

def quicksort(arr,start,end):
    if start>=end:
        return
    
    partition_index = partitionwrtpivot(arr,start,end)
    
    quicksort(arr,start,partition_index) 
    quicksort(arr,partition_index+1,end)  
arr = [11,7,4,2,5,1,10,8,-1]
quicksort(arr,0,len(arr))
print(arr)