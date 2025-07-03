def sumget(self,nums,m):
    s = 0
    for i in range(len(nums)):
        s += (nums[i]+m-1)//2
    return s
def smallestDivisor(self, nums, threshold):
    """
    :type nums: List[int]
    :type threshold: int
    :rtype: int
    """

    
    i = 1

    j = max(nums)

    while (i<=j):
        mid = (i+j)//2
        sume = 0
        k=0
        for k  in range(len(nums)):
            val = nums[k] //mid
            if nums[k]%mid!=0:
                val+=1
            sume+=val
            # print(val," sum",sume)
        print(i," ",mid," ",j," ",sume)
        if sume<=threshold:
            j = mid -1
            
        else:
            i = mid + 1

    return i