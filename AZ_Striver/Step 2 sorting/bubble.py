arr = [7,4,2,5,1,10,8,-1]
#iterative
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

arr = [7,4,2,5,1,10,8,-1]
#recursive
def bubblesort(arr,start):
    if start>=len(arr):
        return
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    bubblesort(arr,start+1)

bubblesort(arr,0)
print(arr)