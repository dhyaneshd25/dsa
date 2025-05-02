
arr = [1,1,2,3,3,3,4,4,5]
#brute force O(n2) and space O(1)
i=0
ans,c=0,0
j=len(arr)-1
while i<j:
    if arr[i]!=arr[i+1]:
        i+=1
    else:
        temp=arr[i+1]
        for k in range(i,j):
            arr[k]=arr[k+1]
        arr[j]=temp
        j-=1
            
    print(i,"=>",arr,j)
       
        
print(arr,ans,c)
            


#optimal O(n) but space O(n)
st=set() # here we use dictionary also(hashmap) [rather than set(hashset)]
arr = [-1,0,0,0,0,3,3]
for i in range(0,len(arr)):
    if arr[i] not in st:
        st.add(arr[i])
co = 0
st = sorted(st)
for i in st:
    arr[co]=i
    co+=1
    print(i,end=" ")
print()


#optimal O(n) and space O(1)
nums = [-1,0,0,0,0,3,3]
i,j=0,1
while j<len(nums):
    if nums[i] != nums[j]:
        nums[i+1],nums[j]=nums[j],nums[i+1]
        i+=1
        j+=1
    else:
        j+=1
print("nums2",nums,i)


# first optimal solution is better than second one in terms of time
# second optimal solution is better than first one in terms of space

