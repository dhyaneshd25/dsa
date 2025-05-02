arr = [7,4,2,5,1,10,8,-1]
#iterative 
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)

#recursive
def insertionsort(arr,start):
    if start>=len(arr):
        return 
    for j in range(start+1,len(arr)):
        if arr[start]>arr[j]:
            arr[start],arr[j]=arr[j],arr[start]
    insertionsort(arr,start+1)
    
arr = [7,4,2,5,1,10,8,-1]
insertionsort(arr,0)
print(arr)


