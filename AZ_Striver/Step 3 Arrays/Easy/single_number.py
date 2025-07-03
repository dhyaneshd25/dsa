nums = [4,1,2,1,2]

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
'''

#brute force O(n^2) and space O(1)
ans=-1
for i in range(len(nums)):
    ck=True
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            ck=False
            break
    if ck:
        ans = nums[i]
        break
print(ans)

#optimal O(n) and space O(n)
c= dict()
for i in range(len(nums)):
            if nums[i] not in c.keys():
                c[nums[i]]=1
            else:
                c[nums[i]]+=1
ans =-1
for item in c:
            if c[item]==1:
                ans=item
print(ans)


'''
xor of element with zero is the same element i.e. x^0=x
xor of element with itself is zero i.e. x^x=0

duplicate element will be removed

'''
#optimal O(n) and space O(1)
ans = 0
for i in range(len(nums)):
    ans=ans^nums[i]
print(ans)

