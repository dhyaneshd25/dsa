nums = [5,7,7,8,8,10]
target = 8
def searchRange(nums, target):
        i=0
        j=len(nums)-1
        l=-1
        r=-1
        #find first occurence
        while i<=j:
            mid = i + (j-i)//2
            if nums[mid]==target:
                l=mid
                j=mid-1
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        i=0
        j=len(nums)-1
        #last occurances
        while i<=j:
            mid = i + (j-i)//2
            if nums[mid]==target:
                r=mid
                i=mid+1
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        return [l,r]


def countoccurrance(nums,target):
        ans =searchRange(nums,target)
        return ans[1]-ans[0]+1

print(countoccurrance(nums,target))