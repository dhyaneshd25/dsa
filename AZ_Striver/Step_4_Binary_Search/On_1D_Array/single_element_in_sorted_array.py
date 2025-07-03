# approach 1 hashmap and frequency count
# approach 2 take ans as 0 and make xor of all the element
# approach 3 binary search 

def singleNonDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)

    # 1-element list
    if n == 1:
        return nums[0]

    # Unique element is at either end
    if nums[0] != nums[1]:
        return nums[0]
    if nums[-1] != nums[-2]:
        return nums[-1]

    # Binary search between indices 1 and n-2
    left, right = 1, n - 2
    while left < right:
        mid = left + (right - left) // 2

        # Found the singleton
        if nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]:
            return nums[mid]

        # Decide which half still contains the singleton
        if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
            left = mid + 1      # singleton is to the right
        else:
            right = mid         # singleton is to the left (could be mid-1 or mid)
            
nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))