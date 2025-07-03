nums = [-2,1,-3,4,-1,2,1,-5,4]


ans  = float('-inf')
s,e=-1,-1
#brute force O(n^3)
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        su=0
        for k in range(i,j+1):
            su+=nums[k]
        if su>ans:
            s=i
            e=j
            ans = su
print(ans,nums[s:e+1])
s=-1
e=-1
ans  = float('-inf')
#brute force O(n^2)
for i in range(0,len(nums)):
    su=0
    for j in range(i+1,len(nums)):
        su+=nums[j]
        if su>ans:
            s=i
            e=j
            ans = su
print(ans,nums[s+1:e+1])

#kadane algo O(n)
ans = float('-inf')
su=0
s=0
e=-1
ss=-1
ee=-1
for i in range(len(nums)):
    ee=i
    su+=nums[i]
    if su>ans:
        s=ss
        e=ee
        ans=su
    if su<0:
        ss=i
        su=0
print(ans,nums[s+1:e+1])