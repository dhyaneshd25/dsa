nums1=[1,2,3,0,5]

su=0 
n=len(nums1)
for i in range(n):
    su+=nums1[i]
total_su = int((n*(n+1))/2)
print(total_su-su)