target=-5
nums = [1,2,0,4,-2,0,2,3,1,0,-1,2,5,-10]

#brute force O(n^3) and space o(1)
ans = 0 

for i  in range(len(nums)):
    for j in range(len(nums)):
        sum = 0
        for k in range(i,j+1):
            sum+=nums[k]
        if sum==target:
            ans=max(ans,j-i+1)
print (ans)

#brute force O(n^2) and space O(1)
ans =0
for i in range(len(nums)):
    sum=0 
    for j in range(i,len(nums)):
        sum+=nums[j]
        if sum==target:
            ans=max(ans,j-i+1)
            
print(ans)

'''
at the current index calculate prefix sum(sum of all element before that i including itself)
if prefix sum == target then select max length
if prefix -target in dict i.e. there is a subarray of sum(target) which start from dict[prefix-target] and end with i
add prefix of dict with its index
'''
#optimal O(n) and space O(n) using hashmap(dict)
d =dict()
ans = 0
ps = 0
for i in range(len(nums)):
    ps+=nums[i]
    if ps == target:
        ans = max(ans,i+1)
    if ps-target in d.keys():
        ans = max(ans,i-d[ps-target])
    if ps not in d.keys():
        d[ps]=i
print(ans)


'''
two pointer
'''
#optimal O(n) and space O(1)  
i,j = 0,0
sum=nums[0]
ans = 0
while j<len(nums):
    while i<j and sum>target:
        sum-=nums[i]
        i+=1
    if sum==target:
        ans = max(ans,j-i+1)
    j+=1
    if j<len(nums):
        sum+=nums[j]
        
print(ans)







