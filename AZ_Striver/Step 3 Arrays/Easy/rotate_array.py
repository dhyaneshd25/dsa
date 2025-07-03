nums = [4,3,5,1]

# right rotate by k place

#borute force(O(n^k))  space O(1)
def rightrotatebyk1(nums,k):
    n=len(nums)
    k=k%n
    for i in range(k):
            temp=nums[n-1]
            j=n-1
            while j>0:
                nums[j]=nums[j-1]
                j-=1
            nums[0]=temp

#optimal (O(n))   space O(n)
def rightrotatebyk2(nums,k):
        n=len(nums)
        k=k%n
        last = []
        j=n-1
        while k>0:
            last.append(nums[j])
            k-=1
            j-=1
        l=n-1
        while j>=0:
            nums[l]=nums[j]
            j-=1
            l-=1
        j=0
        p=len(last)-1
        for it in range(len(last)):
            nums[j]=last[p]
            j+=1
            p-=1

#optimal (O(n))   space O(1)
'''
here reverse the hold array then reverse the left part and right part
'''
def reverse(arr,start,end):
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def rightrotatebyk3(nums,k):
    reverse(nums,0,len(nums)-1)
    reverse(nums,0,k-1)
    reverse(nums,k,len(nums)-1)
print(nums)
rightrotatebyk3(nums,2)
print(nums)


#left rotate
#optimal O(n)  space O(1)

def leftrotatebyk1(nums,k):
    k=k%len(nums)
    reverse(nums,0,k-1)
    reverse(nums,k,len(nums)-1)
    reverse(nums,0,len(nums)-1)

leftrotatebyk1(nums,2)
print(nums)

