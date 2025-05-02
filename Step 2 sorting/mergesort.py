import math

def merge(arr,start,mid,end):
    left=[]
    for i in range(start,mid+1):
        left.append(arr[i])
    right=[]
    for i in range(mid+1,end+1):
        right.append(arr[i])
    
    i,j,k=0,0,start
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k]=right[j]
            j+=1
            k+=1
    while i<len(left):
        arr[k]=left[i]
        k+=1
        i+=1 
    while j<len(right):
        arr[k]=right[j]
        k+=1
        j+=1
    print("merge",arr,left,right)


#recursive       
def mergesort(arr,start,end):
    if start<end:
        mid = math.floor((start+end)/2)
        mergesort(arr,start,mid)
        mergesort(arr,mid+1,end)
        merge(arr,start,mid,end)
    return

arr = [11,7,4,2,-4,66,5,1,10,8,-1,-3]
mergesort(arr,0,len(arr)-1)
print(arr)


arr = [11,7,4,2,-4,66,5,1,10,8,-1,-3]
#iterative

n=len(arr)
m=n//2
i=1
#window size is 1,2,4,8,16,....
while(i<=m):
        s=0
        mid=s+i-1
        e=mid+i
        
        while(e<n):
            print("val",s,mid,e)
            merge(arr,s,mid,e)
            s=e+1
            mid=s+i-1
            e=mid +i
        #here while merging ensure we use previous merged subarray 
        if s<n:
            e=s-1
            mid=e-i
            s=mid-i+1
            mid=e
            merge(arr,s,mid,n-1)
        i*=2

print(arr)