'''
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index where it would be if it were inserted in order
'''
#O(logN)
def searchInsert(nums, target):
        ans = 0
        i=0
        j=len(nums)-1
        while i<=j:
            mid = i + (j-i)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
                ans =i
        return ans
nums = [1,3,5,6]
target = 5