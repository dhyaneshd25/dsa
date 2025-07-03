nums = [4,5,6,7,0,1,2]
target = 0
# here we have to find index
def search(nums, targett):
        i=0
        j=len(nums)-1
        while i<=j:
            mid = i + (j-i)//2
            print(i,mid,j)
          
            if nums[mid]==target:
                return mid
            # 183/196 test cases pass
            # elif nums[i]>target and nums[mid]>=target:
            #     i=mid+1
            # elif nums[j]<target and nums[mid]<=target:
            #     j=mid-1
            # elif nums[mid]>target:
            #     j=mid-1
            # else:
            #     i=mid+1
            if nums[i]<=nums[mid]:
                if target>=nums[i] and nums[mid]>=target:
                    j=mid-1
                else:
                    i=mid+1
            else:
                if target<=nums[j] and nums[mid]<=target:
                    i=mid+1
                else:
                    j=mid-1
        return -1
print(search(nums,target))