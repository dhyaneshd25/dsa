nums = [777,511,23,15]


#brute force O(n^2)
ans = []
for i in range(len(nums)):
    ck = True
    for j in range(i+1,len(nums)):
        if nums[j]>nums[i]:
            ck=False
            break
    if ck:
        ans.append(nums[i])
print(ans)

ans = []

i=len(nums)-1
mx=nums[i]
ans.append(nums[i])
i-=1
while i>=0:
    if nums[i]>mx:
        ans.append(nums[i])
        mx=nums[i]
    i-=1
print(ans)