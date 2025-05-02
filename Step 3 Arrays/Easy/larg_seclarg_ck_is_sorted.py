#find largest element without sorting
arr = [4,11,3,5,9,7,34,2]
larg = arr[0]
for i in range(1,len(arr)):
    if arr[i]>larg:
        larg=arr[i]
print("First largest element of the array :-",larg)


#second largest element without sorting
firstlarg = max(arr[0],arr[1])
secondlarg = min(arr[0],arr[1])
for i in range(2,len(arr)):
    if arr[i]>firstlarg:
        secondlarg = firstlarg
        firstlarg =arr[i]
print("Second largest element of the array :-",secondlarg)
firstlarg = arr[0]
secondlarg = -1
for i in range(1,len(arr)):
    if arr[i]>firstlarg:
        secondlarg=firstlarg
        firstlarg = arr[i]
if secondlarg == -1:
    print("second element does not exit")
else:
    print("second element of the array = ",secondlarg)


# check the array whether it is sorted or not (here sort is in either ascending or descending)
arr=[4,2,3]
is_sorted = True
for i in range(1,len(arr)-1):
    if arr[i-1]>arr[i] and arr[i]<arr[i+1]:
        is_sorted = False
        break
print(is_sorted)


# check if array is sorted and rotated
is_sorted = True
nums = [3,4,5,1,6]
for i in range(1,len(nums)):
    if nums[i-1]>nums[i]:
        is_rotated = True
        f = i
        n = i+1
        if n>=len(nums):
            n=0
        for j in range(0,len(nums)-1):
            if nums[f]>nums[n]:
                is_rotated = False
                break
            else:
                f=n
                n+=1
                if n>=len(nums):
                    n=0
        if not is_rotated:
               is_sorted = False
               break 
        
print("second => ",is_sorted)
