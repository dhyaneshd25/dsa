nums1=[1,2,3,4,5]
nums2=[1,2,7]

n=[]
i,j=0,0
while i<len(nums1) and j<len(nums2):
    if nums1[i]==nums2[j]:
        n.append(nums1[i])
        i+=1
        j+=1
    elif nums1[i]>nums2[j]:
        n.append(nums2[j])
        j+=1
    else:    
        n.append(nums1[i])
        i+=1
while i<len(nums1):
    n.append(nums1[i])
    i+=1
while j<len(nums2):
    n.append(nums2[j])
    j+=1
print(n)