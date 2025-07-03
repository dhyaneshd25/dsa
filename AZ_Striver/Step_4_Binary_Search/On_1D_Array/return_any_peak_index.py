def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>=nums[n-2]:
            return n-1
        i = 1
        j = n-2
        while(i<=j):
            m = i + (j - i)//2
            if nums[m]>nums[m+1] and nums[m]>nums[m-1]:
                return m
            elif nums[m]>nums[m-1]:
                i = m+1
            else:
                j = m-1
        return -1
    
nums = [1,2,1,3,5,6,4]

print(findPeakElement(nums))