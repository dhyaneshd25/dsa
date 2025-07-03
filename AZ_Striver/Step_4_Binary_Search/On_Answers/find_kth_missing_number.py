def findKthPositive(self, arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    n = len(arr)
    i = 0 
    j = n-1
    while i<=j:
        mid = (i+j)//2
        if arr[mid]-mid-1<k:
            i = mid+1
        else:
            j = mid -1
    return i+k