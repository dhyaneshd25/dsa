def findMin(nums):
    i = 0
    j = len(nums)-1
    # ans = nums[0]
    # for  i in range(len(nums)-1):
    #     if nums[i]>nums[i+1]:
    #         return nums[i+1]
    # return ans
    ans = 5001
    while(i<=j):
        m = i + (j-i)//2
        ans = min(ans,nums[i])
        ans = min(ans,nums[m])
        ans = min(ans,nums[j])
        if nums[i]<=nums[m]:
            i = m +1
        else:
            j = m-1
    return ans
    
 
nums = [4,5,6,7,0,1,2]
print(findMin(nums))
    