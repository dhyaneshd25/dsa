arr = [7,4,2,5,1,10,8,-1]

for i in range(len(arr)-1):
    min_index = i
    for j in range(i+1,len(arr)):
        if arr[min_index]>arr[j]:
            min_index = j
    arr[min_index],arr[i]=arr[i],arr[min_index]

print(arr)