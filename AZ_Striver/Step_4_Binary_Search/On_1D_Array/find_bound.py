#O(logN)



def lower_bound(nums,target):
    i=0
    ans = float('inf')
    j=len(nums)-1
    while i<=j:
        mid= i + (j-i)//2
        if nums[mid]>=target:
            ans = min(ans,mid)
            j=mid-1
        else:
            i=mid+1
    ck=float('inf')
    if ans==ck:
        return -1
    return ans

nums = [1,2,2,3]
target = 2
print(lower_bound(nums,target))


def upper_bound(nums,target):
    i=0
    ans = float('inf')
    j=len(nums)-1
    while i<=j:
        mid= i + (j-i)//2
        if nums[mid]>target:
            ans = min(ans,mid)
            j=mid-1
        else:
            i=mid+1
    ck=float('inf')
    if ans==ck:
        return -1
    return ans

nums = [1,2,2,3]
target = 2
print(upper_bound(nums,target))




def findFloor(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] <= x:
            ans = arr[mid]
            # look for smaller index on the left
            low = mid + 1
        else:
            high = mid - 1  # look on the right

    return ans


def findCeil(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = arr[mid]
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans


def floorandceil(arr, n, x):
    f = findFloor(arr, n, x)
    c = findCeil(arr, n, x)
    return [f,c]
arr=[3, 4, 4, 7, 8, 10]
t=5
print(floorandceil(arr,len(arr),t))