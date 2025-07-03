nums = [3,1,-2,-5,2,-4]


#brute force O(n^2)
i=0
while i<len(nums):
            if i%2!=0:
                if nums[i]<0:
                    i+=1
                else:
                    k=i+1
                    while k<len(nums) and nums[k]>=0:
                        k+=1
                    if k>=len(nums):
                        continue
                    t=nums[k]
                    while k>i:
                        nums[k]=nums[k-1]
                        k-=1
                    nums[i]=t
                    i+=1
            else:
                if nums[i]>=0:
                    i+=1
                else:
                    k=i+1
                    while k<len(nums) and nums[k]<0:
                        k+=1
                        if k>=len(nums):
                            continue
                    t=nums[k]
                    while k>i:
                        nums[k]=nums[k-1]
                        k-=1
                    nums[i]=t
                    i+=1
                    
print(nums)


nums = [3,1,-2,-5,2,-4]
#optimal O(n) and space O(n)
ans=[0]*len(nums)
i,j=0,1
for  k in range(len(nums)):
            if nums[k]>=0:
                ans[i]=nums[k]
                i+=2
            else:
                ans[j]=nums[k]
                j+=2
print(ans)
