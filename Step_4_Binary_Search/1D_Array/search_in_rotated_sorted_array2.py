nums = [4,5,6,7,0,1,2]
target = 0
# here we have to find the element is present or not

def search(nums, target):

    # n = len(nums)  # size of the array
    # low, high = 0, n - 1

    # while low <= high:
    #     mid = (low + high) // 2

    #     # if mid points to the target
    #     if nums[mid] == target:
    #         return True

    #     # Edge case:
    #     if nums[low] == nums[mid] and nums[mid] == nums[high]:
    #         low += 1
    #         high -= 1
    #         continue

    #     # if left part is sorted
    #     if nums[low] <= nums[mid]:
    #         if nums[low] <= target <= nums[mid]:
    #             # element exists
    #             high = mid - 1
    #         else:
    #             # element does not exist
    #             low = mid + 1
    #     else:  # if right part is sorted
    #         if nums[mid] <= target <= nums[high]:
    #             # element exists
    #             low = mid + 1
    #         else:
    #             # element does not exist
    #             high = mid - 1

    # return False
    # accepted code
    # co=0
    # i=0
    # j=len(nums)-1
    # while i<=j:
    #     mid = i + (j-i)//2
    #     print(i,mid,j)
        
    #     if nums[mid]==target or nums[i]==target or nums[j]==target:
    #         co+=1
    #         i+=1
    #         return True
    #     # 183/196 test cases pass
    #     # elif nums[i]>target and nums[mid]>=target:
    #     #     i=mid+1
    #     # elif nums[j]<target and nums[mid]<=target:
    #     #     j=mid-1
    #     # elif nums[mid]>target:
    #     #     j=mid-1
    #     # else:
    #     #     i=mid+1
    #     elif target>nums[i] and nums[mid]>target:
    #         j = mid -1
    #     else:
    #         i = i + 1
        
    # if co>=1:
    #     return True
    # return False
    i=0
    j=len(nums)-1
    while(i<=j):
        m = i + (j-i)//2
        if nums[m]==target:
            return True
        elif nums[i]==nums[m] and nums[m]==nums[j]:
            i+=1
            j-=1
            continue
        elif nums[i]<=nums[m]:
            if target>=nums[i] and nums[m]>=target:
                    j = m -1
            else:
                i=m+1
        else:
            if target>=nums[m] and target<=nums[j]:
                i=m+1
            else:
                j=m -1
    return False



print(search(nums,target))