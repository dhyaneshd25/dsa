nums = [2,7,11,15]
target = 9

#brute force O(n^2) and space O(1)
ans=[]
for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    ans.append(i)
                    ans.append(j)
                    break
print(ans)



#optimal O(n) and space O(n)
ans=[]
mp={}
for i in range(len(nums)):
            if nums[i] in mp.keys():
                ans.append(mp[nums[i]])
                ans.append(i)
            else:
                mp[target-nums[i]]=i